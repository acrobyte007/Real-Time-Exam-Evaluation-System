from typing import List
from typing import Optional
from sqlalchemy import String,Boolean,ForeignKey,JSON
from sqlalchemy.orm import Mapped 
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.db.base import Base

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_email: Mapped[str] = mapped_column(String, unique=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    email_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    password: Mapped[str] = mapped_column(String)
    role: Mapped[str] = mapped_column(String)
    exams: Mapped[List["Exams"]] = relationship(back_populates="user")


class Exams(Base):
    __tablename__ = "exams"

    id: Mapped[int] = mapped_column(primary_key=True)
    exam_name: Mapped[str] = mapped_column(String)
    exam_code: Mapped[str] = mapped_column(String)
    exam_duration: Mapped[int] = mapped_column(String)
    user_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )
    user: Mapped[Optional["Users"]] = relationship(back_populates="exams")
    questions: Mapped[List["Questions"]] = relationship(
        back_populates="exam",
        cascade="all"
    )

class Questions(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str] = mapped_column(String)
    options: Mapped[dict] = mapped_column(JSON)
    exam_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("exams.id"),
        nullable=True
    )

    exam: Mapped[Optional["Exams"]] = relationship(back_populates="questions")
