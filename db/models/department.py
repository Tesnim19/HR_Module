from sqlalchemy import Column, Integer, String

from db.base_class import Base

class Department(Base):
    __tablename__ = 'departments'

    department_id = Column(Integer, primary_key=True, index=True)
    department_name = Column(String, nullable=False)