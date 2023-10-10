from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class Role(Base):
  __tablename__ = 'roles'

  role_id = Column(Integer, primary_key=True, index=True)
  role_title = Column(String, nullable=False)
  department_id = Column(Integer, ForeignKey('departments.department_id'))  

  
  department = relationship("Department", back_populates="roles")
