from typing import Dict

from backend.db.repositories.question_repository import QuestionRepository
from backend.db.repositories.answer_repository import AnswerRepository


class BlitzService:

    @staticmethod
    def check_blitz_answers(
            blitz_id: int,
            user_answers: Dict[int, int]
    ) -> Dict:
        questions = QuestionRepository.get_by_blitz(blitz_id)

        if not questions:
            return {"error": "Блиц не найден или в нём нет вопросов"}

        total = len(questions)
        correct_count = 0
        results = []

        for question in questions:
            user_answer_id = user_answers.get(question.id)

            if user_answer_id is None:
                results.append({
                    "question_id": question.id,
                    "question_text": question.text,
                    "user_answer_id": None,
                    "user_answer_text": None,
                    "is_correct": False,
                    "correct_answer_ids": [a.id for a in question.answers if a.is_correct],
                    "correct_answer_texts": [a.text for a in question.answers if a.is_correct]
                })
                continue

            user_answer = AnswerRepository.get_by_id(user_answer_id)
            user_answer_text = user_answer.text if user_answer else None

            is_correct = AnswerRepository.check_user_answer(question.id, user_answer_id)

            if is_correct:
                correct_count += 1

            results.append({
                "question_id": question.id,
                "question_text": question.text,
                "user_answer_id": user_answer_id,
                "user_answer_text": user_answer_text,
                "is_correct": is_correct,
                "correct_answer_ids": [a.id for a in question.answers if a.is_correct],
                "correct_answer_texts": [a.text for a in question.answers if a.is_correct]
            })

        score_percent = round((correct_count / total) * 100, 1) if total > 0 else 0

        return {
            "total_questions": total,
            "correct_answers": correct_count,
            "score_percent": score_percent,
            "results": results
        }