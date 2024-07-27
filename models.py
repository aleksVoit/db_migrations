from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean

from sqlalchemy.orm import relationship, DeclarativeBase, Mapped

from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime


class Base(DeclarativeBase):
    pass


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    fullname = Column(String(100), nullable=False)
    group_id = Column(Integer, ForeignKey(Group.id, ondelete='CASCADE'))
    relationship('Group', backref='groups', cascade='all')


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    fullname = Column(String(100), nullable=False)


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    teacher_id = Column(Integer, ForeignKey(Teacher.id, ondelete='CASCADE'))
    relationship('Teacher', backref='teachers', cascade='all')


class Mark(Base):
    __tablename__ = 'marks'
    id = Column(Integer, primary_key=True)
    note = Column(Integer, nullable=False)
    date = Column(DateTime, default=datetime.now())
    student_id = Column(Integer, ForeignKey(Student.id, ondelete='CASCADE'))
    subject_id = Column(Integer, ForeignKey(Subject.id, ondelete='CASCADE'))
    student = relationship('Student', backref='students', cascade='all')
    subject = relationship('Subject', backref='subjects', cascade='all')
