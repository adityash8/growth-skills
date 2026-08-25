from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate.py"
SPEC = importlib.util.spec_from_file_location("growth_validate", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATE)


class ValidateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.name = "sample-growth"
        self.description = "Run a small growth diagnostic."
        self.skill = self.root / "skills" / self.name / "SKILL.md"
        self.skill.parent.mkdir(parents=True)
        self.write_catalog(self.description)
        self.write_skill(self.description)

    def tearDown(self):
        self.temp.cleanup()

    def write_catalog(self, description: str):
        (self.root / "catalog.json").write_text(
            json.dumps([{"name": self.name, "description": description}]),
            encoding="utf-8",
        )

    def write_skill(self, description: str):
        self.skill.write_text(
            f'---\nname: {self.name}\ndescription: "{description}"\n---\n\n# Sample\n',
            encoding="utf-8",
        )

    def test_valid_repository(self):
        self.assertEqual([], VALIDATE.validate(self.root))

    def test_missing_skill(self):
        self.skill.unlink()
        errors = VALIDATE.validate(self.root)
        self.assertTrue(any("missing directories" in error for error in errors))

    def test_malformed_frontmatter(self):
        self.skill.write_text("# Missing frontmatter\n", encoding="utf-8")
        errors = VALIDATE.validate(self.root)
        self.assertTrue(any("frontmatter" in error for error in errors))

    def test_too_long_description(self):
        description = "x" * 201
        self.write_catalog(description)
        self.write_skill(description)
        errors = VALIDATE.validate(self.root)
        self.assertTrue(any("maximum is 200" in error for error in errors))

    def test_private_leakage(self):
        blocked = "Coo" + "kUnity"
        (self.root / "README.md").write_text(blocked, encoding="utf-8")
        errors = VALIDATE.validate(self.root)
        self.assertTrue(any("blocked private pattern" in error for error in errors))

    def test_absolute_home_path(self):
        blocked = "/" + "Users" + "/someone/private.txt"
        (self.root / "README.md").write_text(blocked, encoding="utf-8")
        errors = VALIDATE.validate(self.root)
        self.assertTrue(any("absolute home path" in error for error in errors))

    def test_symlink_is_rejected(self):
        target = self.root / "outside.txt"
        target.write_text("public text", encoding="utf-8")
        link = self.root / "skills" / self.name / "references"
        link.symlink_to(target)
        errors = VALIDATE.validate(self.root)
        self.assertTrue(any("symlink is not allowed" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
