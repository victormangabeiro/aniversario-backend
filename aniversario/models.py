from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Invitation(Base):
    __tablename__ = "invitations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False)
    phone = Column(String, unique=True, index=True)
    family = Column(String)
    family2 = Column(String)
    family3 = Column(String)
    family4 = Column(String)
