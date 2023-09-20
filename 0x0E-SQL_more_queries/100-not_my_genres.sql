-- a script that uses the hbtn_0d_tvshows database to list all
-- genres not linked to the show Dexter
SELECT DISTINCT tg.name
FROM tv_genres AS tg
LEFT JOIN tv_show_genres AS tsg ON tsg.genre_id = tg.id
LEFT JOIN tv_shows AS ts ON ts.id = tsg.show_id
WHERE ts.title <> "Dexter"
   OR ts.title IS NULL
ORDER BY tg.name;
