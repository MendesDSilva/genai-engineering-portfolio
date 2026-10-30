"""Validate this hub's local documentation without third-party dependencies."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md", "README.pt-BR.md", "LICENSE", ".gitignore", ".editorconfig",
    ".gitattributes", "CONTRIBUTING.md", "SECURITY.md", "CHANGELOG.md",
    "docs/architecture/ecosystem.md", "docs/architecture/architecture-decisions.md",
    "docs/architecture/integration-contracts.md", "docs/competencies/skills-matrix.md",
    "docs/projects/customer-service.md", "docs/projects/enterprise-rag.md",
    "docs/projects/ticket-classifier.md", "docs/learning-roadmap.md",
    "docs/interview-preparation.md", ".github/ISSUE_TEMPLATE/feature_request.md",
    ".github/ISSUE_TEMPLATE/bug_report.md", ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/docs-validation.yml", "assets/diagrams/.gitkeep",
    "assets/screenshots/.gitkeep",
)


def validate(root=ROOT):
    errors = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f"Missing required file: {name}")
    documents = sorted(p for p in root.rglob("*.md") if ".git" not in p.parts)
    for path in documents:
        name = path.relative_to(root)
        text = path.read_text(encoding="utf-8")
        if not text.endswith("\n"):
            errors.append(f"{name}: missing final newline")
        if not text.strip():
            errors.append(f"{name}: empty Markdown document")
        if "\ufffd" in text or "\x00" in text:
            errors.append(f"{name}: invalid text content")
        fence = None
        visible = []
        for number, line in enumerate(text.splitlines(), 1):
            match = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
            if match:
                marker, tail = match.groups()
                if fence is None:
                    fence = marker
                elif marker[0] == fence[0] and len(marker) >= len(fence) and not tail.strip():
                    fence = None
                continue
            if fence is not None:
                continue
            visible.append(line)
            if line.rstrip() != line:
                errors.append(f"{name}:{number}: trailing whitespace")
            if re.match(r"^\s*(<<<<<<<|=======|>>>>>>>)", line):
                errors.append(f"{name}:{number}: possible conflict marker")
        if fence:
            errors.append(f"{name}: unclosed code fence")
        content = "\n".join(visible)
        if not re.search(r"^#\s+\S", content, re.M):
            errors.append(f"{name}: missing level-one heading")
        # Inline code is not a Markdown link container.
        content = re.sub(r"`[^`\n]+`", "", content)
        definitions = {
            " ".join(label.lower().split()): target
            for label, target in re.findall(
                r'^\s{0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)', content, re.M
            )
        }
        targets = re.findall(r'!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+"[^"\n]*")?\s*\)', content)
        targets.extend(definitions.values())
        for label, ref in re.findall(r'!?\[([^\]\n]+)\]\[([^\]\n]*)\]', content):
            key = " ".join((ref or label).lower().split())
            if key not in definitions:
                errors.append(f"{name}: undefined link reference: {key}")
        for target in targets:
            target = target.strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            if not destination.is_relative_to(root.resolve()):
                errors.append(f"{name}: link escapes repository: {target}")
            elif not destination.exists():
                errors.append(f"{name}: broken local link: {target}")
    return documents, errors


if __name__ == "__main__":
    documents, errors = validate()
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        sys.exit(1)
    print(f"Validated {len(documents)} Markdown files and required structure.")
    print("External URLs, heading anchors and Mermaid rendering require separate review.")
