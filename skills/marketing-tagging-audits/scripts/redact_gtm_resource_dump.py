#!/usr/bin/env python3
"""Summarize saved GTM MCP payloads without leaking constant credentials."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

SECRET_RE = re.compile(
    r"(?:api[_ -]?key|api[_ -]?token|access[_ -]?token|refresh[_ -]?token|auth[_ -]?token|"
    r"client[_ -]?secret|private[_ -]?key|password|credential|secret|capi[_ -]?token|"
    r"linkedin[_ -]?api[_ -]?token)",
    re.IGNORECASE,
)
RESOURCE_IDS = {
    "tag": "tagId",
    "trigger": "triggerId",
    "variable": "variableId",
    "client": "clientId",
    "transformation": "transformationId",
}


def decode_payload(path: Path) -> dict[str, Any]:
    text = path.read_text(errors="replace")
    decoder = json.JSONDecoder()

    candidates = [0]
    candidates.extend(match.start() for match in re.finditer(r'\{"result"', text))
    for position in candidates:
        try:
            outer, _ = decoder.raw_decode(text[position:])
        except json.JSONDecodeError:
            continue
        if isinstance(outer, dict) and isinstance(outer.get("result"), str):
            try:
                inner = json.loads(outer["result"])
            except json.JSONDecodeError:
                continue
            if isinstance(inner, dict):
                return inner
        if isinstance(outer, dict):
            return outer
    raise ValueError(f"Could not decode GTM MCP JSON from {path}")


def redact(node: Any, inherited_name: str = "") -> Any:
    if isinstance(node, list):
        return [redact(item, inherited_name) for item in node]
    if not isinstance(node, dict):
        return node

    name = str(node.get("name") or inherited_name)
    credential_variable = bool(SECRET_RE.search(name))
    output: dict[str, Any] = {}
    for key, value in node.items():
        if SECRET_RE.search(str(key)) and not isinstance(value, (dict, list)):
            output[key] = "[REDACTED]"
        elif credential_variable and key == "parameter":
            output[key] = redact_parameter_values(value)
        else:
            output[key] = redact(value, name)
    return output


def redact_parameter_values(node: Any) -> Any:
    if isinstance(node, list):
        return [redact_parameter_values(item) for item in node]
    if isinstance(node, dict):
        return {
            key: ("[REDACTED]" if key == "value" else redact_parameter_values(value))
            for key, value in node.items()
        }
    return node


def summarize(payload: dict[str, Any], source: str) -> dict[str, Any]:
    # quick_preview returns resources under ``containerVersion`` while some MCP
    # exports place them at the top level. Support both without requiring the
    # caller to rewrite the saved payload.
    resource_root = payload.get("containerVersion")
    if not isinstance(resource_root, dict):
        resource_root = payload
    version_root = resource_root.get("version")
    if not isinstance(version_root, dict):
        version_root = resource_root
    result: dict[str, Any] = {
        "source": source,
        "version": {
            key: version_root.get(key)
            for key in ("accountId", "containerId", "containerVersionId", "name")
        },
        "resources": {},
    }
    for resource, id_key in RESOURCE_IDS.items():
        rows = resource_root.get(resource) or []
        safe_rows = []
        for row in rows:
            name = str(row.get("name") or "")
            item = {
                "id": row.get(id_key),
                "name": name,
                "type": row.get("type"),
            }
            if resource == "tag":
                item.update(
                    {
                        "paused": bool(row.get("paused", False)),
                        "firingTriggerId": row.get("firingTriggerId") or [],
                        "consentSettings": row.get("consentSettings"),
                    }
                )
            if resource == "variable":
                item["credential_risk"] = bool(SECRET_RE.search(name))
            safe_rows.append(item)
        result["resources"][resource] = safe_rows
    for key in ("tagPagination", "triggerPagination", "variablePagination"):
        if key in payload:
            result[key] = payload[key]
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument(
        "--redacted-json",
        action="store_true",
        help="Emit the full payload after redacting credential-like fields.",
    )
    args = parser.parse_args()

    output = []
    for path in args.paths:
        payload = decode_payload(path)
        output.append(redact(payload) if args.redacted_json else summarize(payload, str(path)))
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
