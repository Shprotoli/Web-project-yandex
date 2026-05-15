import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from backend.other.extensions import db
from backend.web.app import create_app
from backend.db.models.blitz import Blitz
from backend.db.models.question import Question
from backend.db.models.answer import Answer


def create_physics_blitz_tests():
    app = create_app()

    with app.app_context():
        existing = Blitz.query.filter_by(id_subject="4").first()
        if existing:
            return

        blitz_data = [
            {
                "id_subject": "4",
                "title": "Механика",
                "description": "Кинематика и динамика",
                "path_file_blitz": "blitz/physics_mechanics.json"
            },
            {
                "id_subject": "4",
                "title": "Теплота",
                "description": "Термодинамика и тепловые явления",
                "path_file_blitz": "blitz/physics_heat.json"
            },
            {
                "id_subject": "4",
                "title": "Электричество",
                "description": "Электрические явления и цепи",
                "path_file_blitz": "blitz/physics_electricity.json"
            }
        ]

        blitzes = []
        for data in blitz_data:
            blitz = Blitz(**data)
            db.session.add(blitz)
            db.session.flush()
            blitzes.append(blitz)

        questions_data = [
            (blitzes[0], "Единица измерения скорости в СИ?", [
                ("м/с", True),
                ("км/ч", False),
                ("м/с²", False),
                ("Н", False)
            ]),
            (blitzes[0], "Что такое ускорение?", [
                ("Изменение скорости за единицу времени", True),
                ("Расстояние за единицу времени", False),
                ("Сила, действующая на тело", False),
                ("Масса тела", False)
            ]),
            (blitzes[0], "Формула второй закона Ньютона?", [
                ("F = ma", True),
                ("F = mg", False),
                ("P = Fv", False),
                ("E = mc²", False)
            ]),
            (blitzes[0], "Единица силы в СИ?", [
                ("Ньютон (Н)", True),
                ("Джоуль (Дж)", False),
                ("Ватт (Вт)", False),
                ("Паскаль (Па)", False)
            ]),
            (blitzes[0], "Что такое вес тела?", [
                ("Сила притяжения Земли", True),
                ("Масса тела", False),
                ("Сила трения", False),
                ("Сила упругости", False)
            ]),

            (blitzes[1], "Единица количества теплоты в СИ?", [
                ("Джоуль (Дж)", True),
                ("Кельвин (К)", False),
                ("Ватт (Вт)", False),
                ("Градус Цельсия", False)
            ]),
            (blitzes[1], "Формула количества теплоты при нагревании?", [
                ("Q = cmΔt", True),
                ("Q = λm", False),
                ("Q = r m", False),
                ("Q = F s", False)
            ]),
            (blitzes[1], "Что такое удельная теплоёмкость?", [
                ("Теплота на 1 кг вещества на 1°С", True),
                ("Теплота плавления", False),
                ("Температура кипения", False),
                ("Коэффициент расширения", False)
            ]),
            (blitzes[1], "При какой температуре вода кипит при нормальном давлении?", [
                ("100°C", True),
                ("0°C", False),
                ("273 K", False),
                ("373 K", False)
            ]),
            (blitzes[1], "Что такое удельная теплота парообразования?", [
                ("Теплота на превращение 1 кг жидкости в пар", True),
                ("Теплота на нагрев 1 кг вещества", False),
                ("Теплота на плавление", False),
                ("Работа расширения", False)
            ]),

            (blitzes[2], "Единица электрического тока в СИ?", [
                ("Ампер (А)", True),
                ("Вольт (В)", False),
                ("Ом (Ом)", False),
                ("Кулон (Кл)", False)
            ]),
            (blitzes[2], "Закон Ома для участка цепи?", [
                ("I = U/R", True),
                ("U = IR", False),
                ("P = UI", False),
                ("R = U/I", False)
            ]),
            (blitzes[2], "Единица электрического сопротивления?", [
                ("Ом (Ом)", True),
                ("Вольт (В)", False),
                ("Ампер (А)", False),
                ("Джоуль (Дж)", False)
            ]),
            (blitzes[2], "Что такое напряжение?", [
                ("Работа по перемещению заряда 1 Кл", True),
                ("Сила тока", False),
                ("Сопротивление участка", False),
                ("Мощность", False)
            ]),
            (blitzes[2], "Мощность электрического тока рассчитывается по формуле...", [
                ("P = UI", True),
                ("P = Fv", False),
                ("P = mgh", False),
                ("P = cmΔt", False)
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
    create_physics_blitz_tests()