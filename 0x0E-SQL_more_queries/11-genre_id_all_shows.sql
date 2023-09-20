-- a script that lists all shows contained in the database hbtn_0d_tvshows
SELECT ts.title, tsg.genre_id
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tsg
ON tsg.show_id = ts.id
ORDER BY ts.title, tsg.genre_id;