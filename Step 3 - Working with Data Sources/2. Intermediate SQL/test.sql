SELECT i.invoice_id, t.track_id, t.album_id
FROM invoice_line AS i
INNER JOIN track AS t ON i.track_id = t.track_id


