-- a script that uses the hbtn_0d_tvshows database to lists all genres
-- of the show Dexter
SELECT ts.title, tsg.genre_id
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tsg
ON ts.id = tsg.show_id 
WHERE NOT EXISTS (
  SELECT 1
  FROM tv_show_genres AS tsg2
  WHERE tsg2.show_id = ts.id
)
ORDER BY ts.title, tsg.genre_id;
