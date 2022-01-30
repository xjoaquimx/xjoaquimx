from pydantic import BaseModel

class Filmes(BaseModel):
    id: int
    nome_filme: str
    genero: str

    class Config:         
        orm_mode = True

lista_filmes = []
