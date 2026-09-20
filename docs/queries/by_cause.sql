SELECT value, count(*) AS n FROM tag WHERE facet='cause' GROUP BY value ORDER BY n DESC, value;
