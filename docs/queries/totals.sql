SELECT (SELECT count(*) FROM issue) AS total, (SELECT count(*) FROM issue WHERE is_pr) AS prs, (SELECT count(*) FROM analysis) AS analysed, (SELECT count(*) FROM tag) AS tags;
