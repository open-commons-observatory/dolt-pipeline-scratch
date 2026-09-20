# dolt-pipeline-scratch

Scratch repo testing: a **Doltgres** (Postgres-compatible, version-controlled) database stored in this repo's hidden
ref `refs/dolt/data`, rendered to Markdown and HTML by `tools/render.py` (SQL files + Jinja templates) in GitHub Actions.

- `db/` schema, seed generator, seed data (the database itself lives in `refs/dolt/data`, not in files)
- `docs/pages.yaml`, `docs/queries/*.sql`, `docs/templates/*.j2`: what to render
- `docs/generated/`: rendered Markdown (viewable on GitHub as-is)
- `.github/workflows/docs.yml`: clone DB, render, build HTML, deploy Pages
