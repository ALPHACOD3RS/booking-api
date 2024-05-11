from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    appointments = relationship("Appointment", back_populates="users")


class MedicalCenter(Base):
    __tablename__ = "medical_centers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    adminstrators = relationship("Adminstrator", back_populates="medical_centers")
    rooms = relationship("Room", back_populates="medical_centers")
    opening_hours = Column(String)
    opening_days = Column(DateTime)


class Profesional(Base):
    __tablename__ = "professionals"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    google_calendar_link = Column(String)
    appointments = relationship("Appointment", back_populates="professional")


class Adminstrator(Base):
    __tablename__ = "adminstrators"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    medical_center_id = Column(Integer, ForeignKey('medical_centers.id'))
    medical_center = relationship("MedicalCenter", back_populates="administrators")

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    proffestion_id = Column(Integer, ForeignKey('professionals.id'))
    room_id = Column(Integer, ForeignKey('rooms.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    appointment_date = Column(DateTime) 
    appointment_status = Column(String)
    room = relationship("Room", back_populates="appointment")
    professional = relationship("Professional", back_populates="appointments")
    # user = relationship("User", back_populates="appointments")


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    room_number = Column(Integer)
    medical_center_id = Column(Integer, ForeignKey('medical_centers.id'))
    medical_center = relationship("MedicalCenter", back_populates="rooms")
    appointment = relationship("Appointment", uselist=False, back_populates="room")


