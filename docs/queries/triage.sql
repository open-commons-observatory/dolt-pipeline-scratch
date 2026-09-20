SELECT a.issue_n AS n, i.title, p.value AS pr_potential,
       (SELECT string_agg(t.value, ', ' ORDER BY t.value) FROM tag t WHERE t.issue_n = a.issue_n AND t.facet='layer') AS layers,
       a.summary
FROM analysis a JOIN issue i ON i.n = a.issue_n
JOIN tag p ON p.issue_n = a.issue_n AND p.facet='pr_potential' AND p.value IN ('code-fix','docs-fix')
ORDER BY p.value, a.issue_n;
