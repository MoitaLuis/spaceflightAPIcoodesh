from typing import Optional
from pydantic import BaseModel

class t1(BaseModel):
    id: str
    provider: Optional[str]

class artigo(BaseModel):
    id: int
    featured: Optional[bool] = False
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: Optional[str]
    publishedAt: str
    launches: Optional[t1]
    events: Optional[t1]


