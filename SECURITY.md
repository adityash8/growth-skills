# Security

These skills are instructions, not trusted data boundaries. Review generated actions before changing production systems, spending money, publishing, or modifying accounts.

## Reporting

Report suspected credential exposure, private-data leakage, or unsafe action guidance through a private security advisory on the repository. Do not include live secrets in the report.

## Maintainer response

Maintainers will:

1. remove exposed material from the current tree;
2. assess whether history cleanup is required;
3. rotate affected credentials outside the repository when applicable;
4. add a regression case to the validator when the pattern can be detected safely.

The repository validator blocks known private names and absolute home paths, but it is not a substitute for human review.
