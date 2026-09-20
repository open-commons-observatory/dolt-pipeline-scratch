SELECT value, count(*) AS n FROM tag WHERE facet='layer' GROUP BY value ORDER BY n DESC, value;
