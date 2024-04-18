INSERT INTO example.artist (name)
VALUES
    ('Miles Davis'),
    ('John Coltrane'),
    ('Nina Simone')
;

INSERT INTO example.album (artist_id, title)
VALUES
    ((select id from example.artist where name = 'Miles Davis'), 'In A Silent Way'),
    ((select id from example.artist where name = 'Miles Davis'), 'On the Corner'),
    ((select id from example.artist where name = 'John Coltrane'), 'Cosmic Music'),
    ((select id from example.artist where name = 'John Coltrane'), 'Meditations'),
    ((select id from example.artist where name = 'John Coltrane'), 'A Love Supreme'),
    ((select id from example.artist where name = 'Nina Simone'), 'Silk & Soul'),
    ((select id from example.artist where name = 'Nina Simone'), 'Pastel Blues')
;
