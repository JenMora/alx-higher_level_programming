-- a script that lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT ts.title, IFNULL(SUM(tsr.rate), 0) AS rating
FROM tv_shows AS ts
LEFT JOIN tv_show_ratings AS tsr ON tsr.show_id = ts.id
GROUP BY ts.title
ORDER BY rating DESC;

