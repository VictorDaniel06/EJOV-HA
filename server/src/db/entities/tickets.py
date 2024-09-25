from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship
from src.db.config import Base

class Tickets(Base):
    """ Ticket Entity """

    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    status = Column(String, nullable=False)
    #After insertion of birthdate on register page, modify the 'nullable=True' to 'nullable=False'

    def __rep__(self):
        return f"ticket [name={self.ticket}]"
    