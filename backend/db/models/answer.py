from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from backend.other.extensions import db


class Answer(db.Model):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"), nullable=False)
    text = Column(String(255), nullable=False)
    is_correct = Column(Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"<Answer {self.id} for Q{self.question_id} (correct: {self.is_correct})>"