-- a script that lists all shows, and all genres linked
-- to that show, from the database hbtn_0d_tvshows
SELECT tg.name
FROM tv_genres AS tg
INNER JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id
INNER JOIN tv_shows AS ts ON tsg.show_id = ts.id
WHERE ts.title = "Dexter"
ORDER BY tg.name;
