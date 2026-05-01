from sqlalchemy import Column, Integer, String, DateTime, func

from backend.other.extensions import db


class Blitz(db.Model):
    __tablename__ = "blitz"

    id = Column(Integer, primary_key=True)
    id_subject = Column(String(50), nullable=False)
    title = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=False)
    path_file_blitz = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    def __repr__(self):
        return f"<Blitz {self.title}>"
