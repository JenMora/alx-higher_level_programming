-- a script that uses the hbtn_0d_tvshows database to list all
-- genres not linked to the show DextSELECT DISTINCT tg.name
FROM tv_genres AS tg
LEFT JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id
LEFT JOIN tv_shows AS ts ON tsg.show_id = ts.id
WHERE NOT EXISTS (
  SELECT 1
  FROM tv_show_genres AS tsg2
  INNER JOIN tv_shows AS ts2 ON tsg2.show_id = ts2.id
  WHERE tsg2.genre_id = tg.id
    AND ts2.title = 'Dexter'
)
ORDER BY tg.name;
