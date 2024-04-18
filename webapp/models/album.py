from pydantic import BaseModel


class Album(BaseModel):
    id: str
    artist_name: str
    title: str
