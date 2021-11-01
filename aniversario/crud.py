from sqlalchemy.orm import Session

from . import models, schemas


def get_invitations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Invitation).offset(skip).limit(limit).all()

def get_invitation_by_phone(db: Session, phone: str):
    return db.query(models.Invitation).filter(models.Invitation.phone == phone).first()

def create_invitation(db: Session, invitation: schemas.InvitationCreate):
    # family = Column(String, unique=True, index=True)
    # family2 = Column(String, unique=True, index=True)
    # family3 = Column(String, unique=True, index=True)
    # family4 = Column(String, unique=True, index=True)
    db_invitation = models.Invitation(name=invitation.name, phone=invitation.phone, family=invitation.family, family2=invitation.family2, family3=invitation.family3, family4=invitation.family4)
    db.add(db_invitation)
    db.commit()
    db.refresh(db_invitation)
    return db_invitation

