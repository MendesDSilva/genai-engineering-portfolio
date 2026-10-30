# Contributing

[Portfolio](README.md)

This repository accepts documentation, architecture and portfolio presentation changes. Application code belongs in the three independent repositories described in the README.

## Branches and commits

- `main`: stable, reviewed documentation.
- `develop`: integration of reviewed work.
- `feature/*`: new portfolio capabilities or supporting assets.
- `fix/*`: corrections.
- `docs/*`: documentation updates.

These are proposed conventions; no remote branches or protection settings are created automatically. Create working branches from develop after it exists, open PRs into develop, and promote reviewed releases to main. Bootstrap develop from main once the initial commit exists. Urgent corrections follow the same review path unless maintainers explicitly agree otherwise.

Use Conventional Commits: `type(scope): imperative summary`. Types include `feat`, `fix`, `docs`, `test`, `ci`, `chore`; examples: `docs(rag): clarify abstention policy`, `ci(docs): validate local links`. Use `!` and a `BREAKING CHANGE:` footer for incompatible contract changes.

## Pull requests

1. Describe the concrete problem and resulting behavior.
2. Keep the change focused and preserve existing work.
3. Update relative links, bilingual READMEs and the changelog when relevant.
4. Run `python3 scripts/validate_docs.py` from the repository root.
5. Include evidence of checks and disclose checks not run.
6. Request review; do not merge solely because CI passed.

Never add credentials, private datasets or unlicensed images. Keep project status evidence-based. Mermaid diagrams must be reviewed in GitHub's rendered view; the local checker checks fences and references, not Mermaid semantics.

## Local documentation validation

Python 3.12 is the CI target. The validator uses only the standard library. It checks local Markdown file/directory references (including reference-style links), repository boundaries, basic structure and required files. It deliberately does not check external URLs or heading anchors. GitHub execution is required before claiming that the workflow passed remotely.
