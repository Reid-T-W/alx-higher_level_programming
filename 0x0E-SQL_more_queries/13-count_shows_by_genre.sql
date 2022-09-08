-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name, COUNT(tv_show_genres.genre.id)
FROM tv_show_genres
INNER JOIN tv_genres
ON tv_show_genres.genre.id = tv_genres.id
GROUP BY tv_genres.name;
