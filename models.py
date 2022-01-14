from typing import Optional
from pydantic import BaseModel

class artigo(BaseModel):
    id: int
    featured: Optional[bool] = False
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: Optional[str]
    publishedAt: str
    launches: Optional[list]
    events: Optional[list]


