import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from backend.other.extensions import db
from backend.web.app import create_app
from backend.db.models.blitz import Blitz
from backend.db.models.question import Question
from backend.db.models.answer import Answer


def create_russian_blitz_tests():
    app = create_app()

    with app.app_context():
        existing = Blitz.query.filter_by(id_subject="russian_language").first()
        if existing:
            return

        blitz_data = [
            {
                "id_subject": "1",
                "title": "Русский язык: Орфография и пунктуация",
                "description": "Проверьте знание правил русского языка: орфография, пунктуация, склонение.",
                "path_file_blitz": "blitz/russian_orthography.json"
            },
            {
                "id_subject": "1",
                "title": "Русский язык: Лексика и стилистика",
                "description": "Тест на знание синонимов, антонимов, паронимов и стилей речи.",
                "path_file_blitz": "blitz/russian_lexis.json"
            },
            {
                "id_subject": "1",
                "title": "Русский язык: Синтаксис",
                "description": "Проверьте умение строить предложения и определять виды связи.",
                "path_file_blitz": "blitz/russian_syntax.json"
            }
        ]

        blitzes = []
        for data in blitz_data:
            blitz = Blitz(**data)
            db.session.add(blitz)
            db.session.flush()
            blitzes.append(blitz)

        questions_data = [
            (blitzes[0], "Как правильно пишется слово «...рассчитывать»?", [
                ("расчитывать", False), ("рассчитывать", True),
                ("расчитавать", False), ("рассчитавать", False)
            ]),
            (blitzes[0], "Где нужна запятая в предложении: «Он сказал что придёт поздно»?", [
                ("После «сказал»", True), ("Перед «что»", False),
                ("После «придёт»", False), ("Запятая не нужна", False)
            ]),
            (blitzes[0], "Какое слово пишется слитно?", [
                ("Всё таки", False), ("По моему", False),
                ("Неужели", True), ("Во первых", False)
            ]),
            (blitzes[0], "Выберите правильный вариант: «...положить на стол»", [
                ("положить", True), ("ложить", False),
                ("ложыть", False), ("положыть", False)
            ]),
            (blitzes[0], "Как правильно: «Мы с ...»", [
                ("друзьями", True), ("друзям", False),
                ("друзьям", False), ("друзей", False)
            ]),

            (blitzes[1], "Какой синоним слова «красивый»?", [
                ("уродливый", False), ("прекрасный", True),
                ("страшный", False), ("обычный", False)
            ]),
            (blitzes[1], "Паронимы: «эффектный» и ...", [
                ("эффективный", True), ("эфективный", False),
                ("аффектный", False), ("эфектный", False)
            ]),
            (blitzes[1], "Какой стиль речи используется в художественной литературе?", [
                ("Научный", False), ("Официально-деловой", False),
                ("Художественный", True), ("Публицистический", False)
            ]),
            (blitzes[1], "Антоним к слову «богатый»?", [
                ("бедный", True), ("богат", False),
                ("роскошный", False), ("щедрый", False)
            ]),
            (blitzes[1], "Что означает фразеологизм «бить баклуши»?", [
                ("работать усердно", False), ("бездельничать", True),
                ("драться", False), ("готовить еду", False)
            ]),

            (blitzes[2], "Какой вид придаточного предложения в: «Я знаю, что ты придёшь»?", [
                ("изъяснительное", True), ("определительное", False),
                ("обстоятельственное", False), ("присоединительное", False)
            ]),
            (blitzes[2], "Согласование: «Группа студентов ...»", [
                ("пришла", True), ("пришли", False),
                ("пришёл", False), ("пришло", False)
            ]),
            (blitzes[2], "Что такое «однородные члены предложения»?", [
                ("члены, отвечающие на один вопрос и относящиеся к одному слову", True),
                ("главные члены предложения", False),
                ("второстепенные члены", False),
                ("придаточные предложения", False)
            ]),
            (blitzes[2], "Правильное управление: «гордиться ...»", [
                ("своим успехом", True), ("своим успехам", False),
                ("своего успеха", False), ("своими успехами", False)
            ]),
            (blitzes[2], "Какой тип предложения: «Какой сегодня прекрасный день!»", [
                ("восклицательное", True), ("повествовательное", False),
                ("вопросительное", False), ("побудительное", False)
            ]),
        ]

        for blitz, text, answers in questions_data:
            question = Question(blitz_id=blitz.id, text=text, order_num=1)
            db.session.add(question)
            db.session.flush()

            for ans_text, is_correct in answers:
                answer = Answer(question_id=question.id, text=ans_text, is_correct=is_correct)
                db.session.add(answer)

        db.session.commit()


if __name__ == "__main__":
    create_russian_blitz_tests()
