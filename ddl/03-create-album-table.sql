CREATE TABLE example.album (
    id uuid primary key default gen_random_uuid(),
    artist_id uuid references example.artist(id),
    title text not null
);

GRANT ALL ON TABLE example.album TO example_user;
