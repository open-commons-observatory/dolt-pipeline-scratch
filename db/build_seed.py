"""Generate db/seed.sql from the analysis repo's files (taxonomy, issue list, batch files).
Deterministic: rows sorted by primary key. Malformed 'facet=value' tags are repaired to 'facet:value' and reported."""
import json, glob, re, sys
SRC = sys.argv[1]   # path to the input-remapper-prior-art checkout
q = lambda s: "'" + str(s).replace("'", "''") + "'"
out, fixed = [], []
tax = json.load(open(f"{SRC}/taxonomy/facets.json"))["facets"]
out.append("-- facets")
for name in sorted(tax):
    out.append(f"INSERT INTO facet VALUES ({q(name)}, {str(bool(tax[name]['multi'])).lower()}, {q(tax[name]['doc'])});")
out.append("-- facet values")
for name in sorted(tax):
    for val in sorted(tax[name]["values"]):
        out.append(f"INSERT INTO facet_value VALUES ({q(name)}, {q(val)}, {q(tax[name]['values'][val])});")
items = sorted(json.load(open(f"{SRC}/data/issues-list.json")), key=lambda x: x["n"])
out.append("-- issues")
for x in items:
    state = "MERGED" if x.get("merged") else x["state"]
    out.append(f"INSERT INTO issue VALUES ({x['n']}, {q(x['title'])}, {str(bool(x['pr'])).lower()}, {q(state)}, {q(x['created'])}, {x['comments']});")
rows = {}
for f in sorted(glob.glob(f"{SRC}/batches/*.tsv")):
    batch = f.split("/")[-1][:4]
    for line in open(f, encoding="utf-8"):
        if not line.strip() or line.startswith("#"): continue
        p = [s.strip() for s in line.split(" | ", 3)]
        if len(p) < 4: continue
        n = int(p[0].lstrip("i")); depth = "full"; tags = []
        for t in p[2].split():
            if t.startswith("depth="): depth = t.split("=", 1)[1]; continue
            if ":" not in t and "=" in t:
                fixed.append((n, t)); t = t.replace("=", ":", 1)
            tags.append(tuple(t.split(":", 1)))
        rows[n] = (batch, depth, p[3], tags)
out.append("-- analyses")
for n in sorted(rows):
    b, d, s, _ = rows[n]
    out.append(f"INSERT INTO analysis VALUES ({n}, {q(b)}, {q(d)}, {q(s)});")
out.append("-- tags")
for n in sorted(rows):
    for fa, va in sorted(set(rows[n][3])):
        out.append(f"INSERT INTO tag VALUES ({n}, {q(fa)}, {q(va)});")
open("db/seed.sql", "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"seed.sql: {len(items)} issues, {len(rows)} analyses, {sum(len(set(r[3])) for r in rows.values())} tags")
for n, t in fixed: print(f"  repaired malformed tag on #{n}: {t!r}")
