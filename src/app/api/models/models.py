from sqlalchemy.orm import Mapped, mapped_column
from src.app import db


class User(db.Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, nullable=False)
    username: Mapped[str] = mapped_column(index=True, nullable=False)
    email: Mapped[str] = mapped_column(index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(index=True, nullable=False)
