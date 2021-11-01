from typing import List, Optional

from pydantic import BaseModel


class InvitationBase(BaseModel):
    name: str
    phone: str
    family: Optional[str] = None
    family2: Optional[str] = None
    family3: Optional[str] = None
    family4: Optional[str] = None


class InvitationCreate(InvitationBase):
    pass


class Invitation(InvitationBase):
    id: int

    class Config:
        orm_mode = True
