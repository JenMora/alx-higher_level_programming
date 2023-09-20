-- a script that uses the hbtn_0d_tvshows database to list all genres
-- not linked to the show Dexter
SELECT genre_id
FROM tv_show_genres
WHERE show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter' LIMIT 1);
-- List genres not linked to "Dexter"
SELECT tg.name
FROM tv_genres AS tg
LEFT JOIN (
ELECT genre_id
FROM tv_show_genres
WHERE show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter' LIMIT 1)
) AS linked_genres ON tg.id = linked_genres.genre_id
WHERE linked_genres.genre_id IS NULL
ORDER BY tg.name;
