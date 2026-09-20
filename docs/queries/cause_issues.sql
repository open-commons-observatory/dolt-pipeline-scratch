SELECT a.issue_n AS n, i.title, i.state, a.summary
FROM tag t JOIN analysis a ON a.issue_n = t.issue_n JOIN issue i ON i.n = t.issue_n
WHERE t.facet='cause' AND t.value=%(value)s
ORDER BY a.issue_n;
