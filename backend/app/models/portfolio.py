
from sqlalchemy import Column, Integer, ForeignKey, Float
from app.db.base import Base

class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    balance = Column(Float, default=0.0)
