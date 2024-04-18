create table example.artist (
    id uuid primary key default gen_random_uuid(),
    name text not null
);

grant all on table example.artist to example_user;
