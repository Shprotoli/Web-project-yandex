from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from backend.other.extensions import db


class Question(db.Model):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    blitz_id = Column(Integer, ForeignKey("blitz.id", ondelete="CASCADE"), nullable=False)
    text = Column(Text, nullable=False)
    order_num = Column(Integer, default=1, nullable=False)

    blitz = relationship("Blitz", backref="questions")
    answers = relationship("Answer", backref="question", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Question {self.id} (Blitz {self.blitz_id})>"