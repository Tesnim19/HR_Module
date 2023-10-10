from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class EmployeeHistory(Base):
    __tablename__ = 'employee_history'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))  # ForeignKey to User
    department_id = Column(Integer, ForeignKey('departments.department_id'))  # ForeignKey to Department
    role_id = Column(Integer, ForeignKey('roles.role_id'))  # ForeignKey to Role
    from_date = Column(DateTime)
    to_date = Column(DateTime)
    supervisor_id = Column(Integer, ForeignKey('employee_history.id'))  # ForeignKey to EmployeeHistory

    # Establish a relationship with User
    user = relationship("User", back_populates="employee_history")

    # Establish a relationship with Department
    department = relationship("Department", back_populates="employee_history")

    # Establish a relationship with Role
    role = relationship("Role", back_populates="employee_history")

    # Establish a relationship with Supervisor (self-referential)
    supervisor = relationship("EmployeeHistory", remote_side=[id], back_populates="subordinates")

    # Establish a relationship with Subordinates (self-referential)
    subordinates = relationship("EmployeeHistory", back_populates="supervisor")