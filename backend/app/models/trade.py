
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    side = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    mode = Column(String)
    created_at = Column(DateTime, server_default=func.now())
