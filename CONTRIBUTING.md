# Contributing

Contributions should make a skill more executable, more evidence-aware, or safer to use.

## Before opening a change

1. Keep the scope to one skill or one shared guardrail.
2. Put the trigger and boundary in the frontmatter description.
3. Keep `SKILL.md` under 250 lines. Move optional depth into `references/`.
4. Separate facts, assumptions, recommendations, and unknowns.
5. Avoid universal benchmarks. Attach segment, date, source, and sample caveats.
6. Remove account names, private paths, identifiers, credentials, and vendor-specific secrets.
7. Paraphrase source concepts and update `SOURCES.md` when adding a material framework.

## Required checks

```bash
make validate
make test
```

A useful pull request explains:

- the failure mode being fixed;
- why the new procedure is better;
- the smallest example that proves it;
- any new source or maintenance burden.

Do not add a new skill when an existing skill can absorb the procedure cleanly.
