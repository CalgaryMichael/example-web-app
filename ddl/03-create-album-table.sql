CREATE TABLE example.album (
    id varchar(36) primary key default gen_random_uuid(),
    artist_id varchar(36) references example.artist(id),
    title text not null
);

GRANT ALL ON TABLE example.album TO example_user;
