-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_show_genres
FULL JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id;
WHERE tv_show_genres.show_id IS NULL OR tv_shows.id IS NULL;
ORDER BY tv_shows.title, tv_show_genres.genre_id;
