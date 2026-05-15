import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from backend.other.extensions import db
from backend.web.app import create_app
from backend.db.models.blitz import Blitz
from backend.db.models.question import Question
from backend.db.models.answer import Answer


def create_algebra_blitz_tests():
    app = create_app()

    with app.app_context():
        existing = Blitz.query.filter_by(id_subject="3").first()
        if existing:
            return

        blitz_data = [
            {
                "id_subject": "3",
                "title": "Основы алгебры",
                "description": "Выражения, степени, модуль, линейные уравнения.",
                "path_file_blitz": "blitz/algebra_basics.json"
            },
            {
                "id_subject": "3",
                "title": "Квадратные уравнения",
                "description": "Решение квадратных уравнений, формула Виета, дискриминант.",
                "path_file_blitz": "blitz/algebra_quadratic.json"
            },
            {
                "id_subject": "3",
                "title": "Функции",
                "description": "Линейные и квадратичные функции, системы уравнений.",
                "path_file_blitz": "blitz/algebra_functions.json"
            }
        ]

        blitzes = []
        for data in blitz_data:
            blitz = Blitz(**data)
            db.session.add(blitz)
            db.session.flush()
            blitzes.append(blitz)

        questions_data = [
            (blitzes[0], "Упростите выражение: 3a + 5a - 2a", [
                ("6a", True),
                ("8a", False),
                ("5a", False),
                ("4a", False)
            ]),
            (blitzes[0], "Значение выражения 2³ + 3²", [
                ("17", True),
                ("12", False),
                ("25", False),
                ("10", False)
            ]),
            (blitzes[0], "Решение уравнения x + 7 = 12", [
                ("x = 5", True),
                ("x = 19", False),
                ("x = -5", False),
                ("x = 7", False)
            ]),
            (blitzes[0], "Модуль числа -8 равен...", [
                ("8", True),
                ("-8", False),
                ("0", False),
                ("16", False)
            ]),
            (blitzes[0], "Что такое коэффициент?", [
                ("Числовой множитель при переменной", True),
                ("Степень переменной", False),
                ("Свободный член", False),
                ("Корень уравнения", False)
            ]),

            (blitzes[1], "Дискриминант квадратного уравнения ax² + bx + c = 0 равен...", [
                ("b² - 4ac", True),
                ("b² + 4ac", False),
                ("2b - 4ac", False),
                ("a + b + c", False)
            ]),
            (blitzes[1], "Решите уравнение x² - 9 = 0", [
                ("x = ±3", True),
                ("x = 9", False),
                ("x = 3", False),
                ("x = -9", False)
            ]),
            (blitzes[1], "Количество корней уравнения x² + 4 = 0", [
                ("0 корней", True),
                ("1 корень", False),
                ("2 корня", False),
                ("Бесконечно много", False)
            ]),
            (blitzes[1], "По формуле Виета сумма корней x² - 5x + 6 = 0 равна...", [
                ("5", True),
                ("6", False),
                ("-5", False),
                ("30", False)
            ]),
            (blitzes[1], "Уравнение x² + 6x + 9 = 0 имеет...", [
                ("Один корень (двойной)", True),
                ("Два разных корня", False),
                ("Нет корней", False),
                ("Три корня", False)
            ]),

            (blitzes[2], "Область определения функции y = 1/x", [
                ("Все x, кроме 0", True),
                ("Все действительные x", False),
                ("x ≥ 0", False),
                ("x ≤ 0", False)
            ]),
            (blitzes[2], "Решите систему: x + y = 7, x - y = 3", [
                ("x=5, y=2", True),
                ("x=4, y=3", False),
                ("x=7, y=0", False),
                ("x=3, y=4", False)
            ]),
            (blitzes[2], "График линейной функции — это...", [
                ("Прямая", True),
                ("Парабола", False),
                ("Гипербола", False),
                ("Окружность", False)
            ]),
            (blitzes[2], "Вершина параболы y = x² - 4x + 3 находится в точке...", [
                ("(2, -1)", True),
                ("(0, 3)", False),
                ("(4, 3)", False),
                ("(-2, 7)", False)
            ]),
            (blitzes[2], "Функция y = kx + b называется...", [
                ("Линейной", True),
                ("Квадратичной", False),
                ("Обратной пропорциональностью", False),
                ("Постоянной", False)
            ]),
        ]

        for blitz, text, answers in questions_data:
            max_order = db.session.query(db.func.max(Question.order_num)) \
                            .filter(Question.blitz_id == blitz.id).scalar() or 0

            question = Question(
                blitz_id=blitz.id,
                text=text,
                order_num=max_order + 1
            )
            db.session.add(question)
            db.session.flush()

            for ans_text, is_correct in answers:
                answer = Answer(
                    question_id=question.id,
                    text=ans_text,
                    is_correct=is_correct
                )
                db.session.add(answer)

        db.session.commit()


if __name__ == "__main__":
    create_algebra_blitz_tests()