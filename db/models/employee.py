from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class Employee(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    mother_name = Column(String)
    date_of_birth = Column(DateTime)
    gender = Column(String)
    marital_status = Column(String)
    address = Column(String)
    phone_number = Column(String)
    user_id = Column(Integer, ForeignKey('users.user_id'))  # ForeignKey to User

    # Establish a relationship with User
    user = relationship("User", back_populates="employees")