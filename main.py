import crud, models, schemas
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

def get_db():     
    db = SessionLocal()     
    try:         
        yield db     
    finally:
        db.close()

@app.get("/filmes/{filme_id}", response_model = schemas.Filmes)
def retorna_filme(filme_id: int, db: Session = Depends(get_db)):
    db_filmes = crud.listar_filme_id(db, filme_id)

    if db_filmes is None:
        raise HTTPException(
            status_code = 404,
            detail = "Filme não encontrado no banco de dados!")
    return db_filmes 

@app.get('/filmes', response_model = schemas.lista_filmes)
def retorna_todos_filmes(db: Session = Depends(get_db)):
    db_filmes = crud.listar_filmes(db)

    lista_filmes = []
    for filme in db_filmes:
        lista_filmes.append(filme)
    return lista_filmes   

@app.post("/filmes", response_model = schemas.Filmes, status_code = 201) 
def cadastra_filme(filme: schemas.Filmes, db: Session = Depends(get_db)):
    db_filmes = crud.listar_filme_id(db, filme.id) 

    if db_filmes:
        raise HTTPException(
            status_code = 400, 
            detail = "Filme já existe no banco de dados!")
    return crud.novo_filme(db = db, filme = filme)
