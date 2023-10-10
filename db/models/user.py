from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base
from enum import Enum

class UserStatus(str, Enum):
    active = "active"
    inactive = "inactive"
    suspended = "suspended"
    pending = "pending"

class User(Base):
  __tablename__ = 'users'

  user_id = Column(Integer, primary_key=True, index=True)
  user_name = Column(String, index=True, nullable=False)
  password = Column(String, nullable=False)
  email = Column(String, unique=True, index=True, nullable=False)
  employment_start_date = Column(DateTime)
  created_at = Column(DateTime, default=datetime.utcnow)
  updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
  status = Column(String, Enum(UserStatus))
  image = Column(String, nullable=True)
  