/*
3.The With Clause
*/
-- WITH playlist_info AS
--     (
--     SELECT pl.playlist_id AS playlist_id,
--            pl.name AS playlist_name,
--            t.name AS track_name,
--            (t.milliseconds / 1000) AS track_length
--     FROM playlist AS pl 
--     LEFT JOIN playlist_track AS pt ON pt.playlist_id = pl.playlist_id
--     LEFT JOIN track AS t ON t.track_id = pt.track_id
--     )

-- SELECT playlist_id,
--        playlist_name,
--        COUNT(track_name) AS number_of_tracks,
--        SUM(track_length) AS length_seconds
-- FROM playlist_info
-- GROUP BY 1, 2
-- ORDER BY 1;

/*
4.Creating Views
*/

