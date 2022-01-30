import models, schemas
from sqlalchemy.orm import Session

def novo_filme(db: Session, filme: schemas.Filmes):
    db_filmes = models.Filmes(**filme.dict())
    db.add(db_filmes)
    db.commit()
    db.refresh(db_filmes)
    return db_filmes

def listar_filme_id(db: Session, filme_id: int):
    return db.query(models.Filmes).filter(models.Filmes.id == filme_id).first()

def listar_filmes(db: Session):
    return db.query(models.Filmes).all()
