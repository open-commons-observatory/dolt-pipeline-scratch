#!/usr/bin/env python3
"""Render Markdown pages from a Postgres-compatible database (Doltgres) using SQL files + Jinja templates.
Usage: render.py [output_dir]      Connection via PG* env vars (PGHOST, PGPORT, PGUSER, PGPASSWORD, PGDATABASE).
Deterministic: same database commit + same templates => byte-identical output (no timestamps)."""
import os, sys, shutil, pathlib, yaml, psycopg, jinja2
from psycopg.rows import dict_row

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else DOCS / "generated"

def cell(s, n=None):
    s = " ".join(str(s if s is not None else "").split()).replace("|", "\\|")
    return s if not n or len(s) <= n else s[: n - 1].rstrip() + "…"

def main():
    spec = yaml.safe_load((DOCS / "pages.yaml").read_text())
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(DOCS / "templates"),
                             trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True,
                             undefined=jinja2.StrictUndefined)
    env.filters["cell"] = cell
    conn = psycopg.connect(host=os.environ.get("PGHOST", "127.0.0.1"), port=os.environ.get("PGPORT", "5432"),
                           user=os.environ.get("PGUSER", "postgres"), password=os.environ.get("PGPASSWORD", "password"),
                           dbname=os.environ.get("PGDATABASE", "ba"), row_factory=dict_row, autocommit=True)
    def q(name, params=None):
        return conn.execute((DOCS / "queries" / name).read_text(), params or {}).fetchall()
    if OUT.exists(): shutil.rmtree(OUT)          # stale pages must disappear when data disappears
    written = []
    for page in spec["pages"]:
        tpl = env.get_template(page["template"])
        if "for_each" in page:
            jobs = [(r["value"], {"value": r["value"]}) for r in q(page["for_each"]["query"])]
        else:
            jobs = [(None, {})]
        for param, params in jobs:
            ctx = {k: q(f, params) for k, f in page["queries"].items()}
            out = OUT / page["out"].format(**params)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(tpl.render(vars=spec.get("vars", {}), param=param, **ctx), encoding="utf-8")
            written.append(out)
    print(f"rendered {len(written)} pages into {OUT}")

if __name__ == "__main__":
    main()
