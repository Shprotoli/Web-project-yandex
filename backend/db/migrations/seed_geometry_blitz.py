import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from backend.other.extensions import db
from backend.web.app import create_app
from backend.db.models.blitz import Blitz
from backend.db.models.question import Question
from backend.db.models.answer import Answer


def create_geometry_blitz_tests():
    app = create_app()

    with app.app_context():
        existing = Blitz.query.filter_by(id_subject="geometry").first()
        if existing:
            return

        blitz_data = [
            {
                "id_subject": "2",
                "title": "Основные понятия и углы",
                "description": "Тест на знание базовых понятий геометрии, видов углов и их свойств.",
                "path_file_blitz": "blitz/geometry_basics.json"
            },
            {
                "id_subject": "2",
                "title": "Треугольники",
                "description": "Виды треугольников, свойства, признаки равенства и неравенства.",
                "path_file_blitz": "blitz/geometry_triangles.json"
            },
            {
                "id_subject": "2",
                "title": "Четырёхугольники",
                "description": "Параллелограммы, трапеции, ромбы, прямоугольники, квадрат, окружность.",
                "path_file_blitz": "blitz/geometry_quadrangles.json"
            }
        ]

        blitzes = []
        for data in blitz_data:
            blitz = Blitz(**data)
            db.session.add(blitz)
            db.session.flush()
            blitzes.append(blitz)

        questions_data = [
            (blitzes[0], "Что такое отрезок?", [
                ("Часть прямой, ограниченная двумя точками", True),
                ("Прямая без начала и конца", False),
                ("Луч с началом в одной точке", False),
                ("Множество всех точек", False)
            ]),
            (blitzes[0], "Какой угол называется прямым?", [
                ("90°", True),
                ("Меньше 90°", False),
                ("Больше 90°, но меньше 180°", False),
                ("180°", False)
            ]),
            (blitzes[0], "Сколько градусов в развёрнутом угле?", [
                ("180°", True),
                ("90°", False),
                ("360°", False),
                ("270°", False)
            ]),
            (blitzes[0], "Какие углы называются вертикальными?", [
                ("Углы, образованные пересекающимися прямыми, с общей вершиной", True),
                ("Углы, сумма которых 90°", False),
                ("Углы, сумма которых 180°", False),
                ("Смежные углы", False)
            ]),
            (blitzes[0], "Сколько градусов в полном угле?", [
                ("360°", True),
                ("180°", False),
                ("90°", False),
                ("270°", False)
            ]),

            (blitzes[1], "Какой треугольник называется равносторонним?", [
                ("Все стороны равны", True),
                ("Две стороны равны", False),
                ("Все углы разные", False),
                ("Один угол 90°", False)
            ]),
            (blitzes[1], "Сумма углов треугольника равна...", [
                ("180°", True),
                ("360°", False),
                ("90°", False),
                ("270°", False)
            ]),
            (blitzes[1], "В каком треугольнике все углы острые?", [
                ("Остроугольном", True),
                ("Прямоугольном", False),
                ("Тупоугольном", False),
                ("Равнобедренном", False)
            ]),
            (blitzes[1], "Признак равенства треугольников по двум сторонам и углу между ними — это...", [
                ("Признак SAS", True),
                ("Признак SSS", False),
                ("Признак ASA", False),
                ("Признак AAS", False)
            ]),
            (blitzes[1], "Треугольник, в котором один угол 90°, называется...", [
                ("Прямоугольным", True),
                ("Остроугольным", False),
                ("Тупоугольным", False),
                ("Равносторонним", False)
            ]),

            (blitzes[2], "Какой четырёхугольник имеет все стороны равными?", [
                ("Ромб", True),
                ("Прямоугольник", False),
                ("Трапеция", False),
                ("Параллелограмм", False)
            ]),
            (blitzes[2], "Сумма внутренних углов четырёхугольника равна...", [
                ("360°", True),
                ("180°", False),
                ("540°", False),
                ("720°", False)
            ]),
            (blitzes[2], "У квадрата все углы...", [
                ("Прямые (90°)", True),
                ("Острые", False),
                ("Тупые", False),
                ("Разные", False)
            ]),
            (blitzes[2], "Какой четырёхугольник имеет только одну пару параллельных сторон?", [
                ("Трапеция", True),
                ("Параллелограмм", False),
                ("Ромб", False),
                ("Прямоугольник", False)
            ]),
            (blitzes[2], "Диаметр окружности — это...", [
                ("Отрезок, соединяющий две точки окружности и проходящий через центр", True),
                ("Радиус, умноженный на 2", True),
                ("Хорда", False),
                ("Касательная", False)
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
    create_geometry_blitz_tests()
