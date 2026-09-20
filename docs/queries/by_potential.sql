SELECT value, count(*) AS n FROM tag WHERE facet='pr_potential' GROUP BY value ORDER BY n DESC, value;
