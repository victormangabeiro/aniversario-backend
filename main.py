from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from aniversario import crud, models, schemas
from aniversario.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/create/", response_model=schemas.Invitation)
def create_user(invitation: schemas.InvitationCreate, db: Session = Depends(get_db)):
    db_invitation = crud.get_invitation_by_phone(db, phone=invitation.phone)
    if db_invitation:
        raise HTTPException(status_code=400, detail="Phone already registered")
    return crud.create_invitation(db=db, invitation=invitation)


@app.get("/invitations/", response_model=List[schemas.Invitation])
def read_invitations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    invitations = crud.get_invitations(db, skip=skip, limit=limit)
    return invitations
