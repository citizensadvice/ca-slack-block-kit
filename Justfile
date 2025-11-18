# Show the list of available commands
@help:
    just --list

# Install project dependencies and configure development environment
[group("Housekeeping")]
setup:
    brew bundle
    uv sync
    pre-commit install

# Lint and typecheck the codebase
[group("Code Quality")]
lint *paths:
    uv run ruff check {{ paths }}
    uv run ruff format --check {{ paths }}
    uv run ty check {{ paths }}

# Format the codebase
[group("Code Quality")]
format *paths:
    uv run ruff format {{ paths }}
    uv run ruff check --fix {{ paths }}
    just --fmt --unstable

# Run the test suite
[group("Testing")]
test:
    uv run pytest tests

# Bump version, push and create draft release
[confirm("Are you sure you want to draft a release? [y/N]")]
[group("release")]
draft-release bump='patch': (_bump_version bump) _push_version _create_draft_release

_bump_version bump:
    git checkout main
    git pull origin main
    git reset # Unstage all files
    @just build
    uv version --bump {{ bump }}
    git add pyproject.toml uv.lock

[confirm("Are you sure you want to push the version change? [y/N]")]
_push_version:
    git commit -m "Bumped version to $(uv version --short)"
    git push origin main

_create_draft_release:
    gh release create $(uv version --short)--draft --generate-notes
    echo "> Follow the link to review and publish the release"
