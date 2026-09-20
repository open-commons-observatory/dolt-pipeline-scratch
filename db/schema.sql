-- Data dictionary (the taxonomy) as tables, so the database itself enforces it.
CREATE TABLE facet (
  name  text PRIMARY KEY,
  multi boolean NOT NULL,
  doc   text NOT NULL
);
CREATE TABLE facet_value (
  facet text NOT NULL REFERENCES facet(name),
  value text NOT NULL,
  doc   text NOT NULL,
  PRIMARY KEY (facet, value)
);
-- Every issue and PR in the corpus.
CREATE TABLE issue (
  n        int PRIMARY KEY,
  title    text NOT NULL,
  is_pr    boolean NOT NULL,
  state    text NOT NULL CHECK (state IN ('OPEN','CLOSED','MERGED')),
  created  date NOT NULL,
  comments int NOT NULL CHECK (comments >= 0)
);
-- One row per analysed issue (reading result).
CREATE TABLE analysis (
  issue_n int PRIMARY KEY REFERENCES issue(n),
  batch   text NOT NULL,
  depth   text NOT NULL CHECK (depth IN ('title','thread','full','source')),
  summary text NOT NULL
);
-- facet:value tags; a tag outside the taxonomy cannot be inserted.
CREATE TABLE tag (
  issue_n int  NOT NULL REFERENCES analysis(issue_n),
  facet   text NOT NULL,
  value   text NOT NULL,
  PRIMARY KEY (issue_n, facet, value),
  FOREIGN KEY (facet, value) REFERENCES facet_value(facet, value)
);
