from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass

class UserInDBBase(UserBase):
    id: int
    appointments: List['AppointmentBase'] = []

    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass

class UserInDB(UserInDBBase):
    pass

class MedicalCenterBase(BaseModel):
    name: str
    opening_hours: str
    opening_days: datetime

class MedicalCenterCreate(MedicalCenterBase):
    pass

class MedicalCenterUpdate(MedicalCenterBase):
    pass

class MedicalCenterInDBBase(MedicalCenterBase):
    id: int
    rooms: List['RoomBase'] = []
    administrators: List['AdministratorBase'] = []

    class Config:
        orm_mode = True

class MedicalCenter(MedicalCenterInDBBase):
    pass

class MedicalCenterInDB(MedicalCenterInDBBase):
    pass

class ProfessionalBase(BaseModel):
    name: str
    google_calendar_link: str

class ProfessionalCreate(ProfessionalBase):
    pass

class ProfessionalUpdate(ProfessionalBase):
    pass

class ProfessionalInDBBase(ProfessionalBase):
    id: int
    appointments: List['AppointmentBase'] = []

    class Config:
        orm_mode = True

class Professional(ProfessionalInDBBase):
    pass

class ProfessionalInDB(ProfessionalInDBBase):
    pass

class AdministratorBase(BaseModel):
    name: str
    email: str
    medical_center_id: int

class AdministratorCreate(AdministratorBase):
    password: str

class AdministratorUpdate(AdministratorBase):
    pass

class AdministratorInDBBase(AdministratorBase):
    id: int
    medical_center: MedicalCenter

    class Config:
        orm_mode = True

class Administrator(AdministratorInDBBase):
    pass

class AdministratorInDB(AdministratorInDBBase):
    pass

class AppointmentBase(BaseModel):
    start_time: datetime
    end_time: datetime
    appointment_date: datetime
    appointment_status: str

class AppointmentCreate(AppointmentBase):
    professional_id: int
    room_id: int
    user_id: int

class AppointmentUpdate(AppointmentBase):
    pass

class AppointmentInDBBase(AppointmentBase):
    id: int
    professional: Professional
    room: 'Room'
    user: User

    class Config:
        orm_mode = True

class Appointment(AppointmentInDBBase):
    pass

class AppointmentInDB(AppointmentInDBBase):
    pass

class RoomBase(BaseModel):
    room_number: int
    medical_center_id: int

class RoomCreate(RoomBase):
    pass

class RoomUpdate(RoomBase):
    pass

class RoomInDBBase(RoomBase):
    id: int
    medical_center: MedicalCenter

    class Config:
        orm_mode = True

class Room(RoomInDBBase):
    pass

class RoomInDB(RoomInDBBase):
    pass
