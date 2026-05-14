import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";

import Header from "../Components/header";
import "../styles/page/blitz/blitz.scss";

function Question({
                      number,
                      title,
                      options = [],
                      selectedAnswer,
                      onSelect
                  }) {
    return (
        <li className="blitz--card">
            <h2 className="blitz--question">
                {number}. {title}
            </h2>

            <ul className="blitz--options">
                {options.map((answer, index) => {
                    const letter = String.fromCharCode(65 + index);
                    const optionId = `q${number}o${answer.id || index}`;

                    return (
                        <li key={answer.id || index} className="option">
                            <input
                                type="radio"
                                name={`question${number}`}
                                id={optionId}
                                checked={selectedAnswer === answer.id}
                                onChange={() => onSelect(answer.id)}
                            />
                            <label htmlFor={optionId}>
                                <span className="option-letter">{letter}</span>
                                <span className="option-text">{answer.text}</span>
                            </label>
                        </li>
                    );
                })}
            </ul>
        </li>
    );
}

function BlitzPage() {
    const { id } = useParams();

    const [blitz, setBlitz] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [selectedAnswers, setSelectedAnswers] = useState({});
    const [submitting, setSubmitting] = useState(false);
    const [submitResult, setSubmitResult] = useState(null);

    useEffect(() => {
        const fetchBlitz = async () => {
            try {
                setLoading(true);
                const response = await fetch(`/api/v1/blitzes/${id}`);
                if (!response.ok) throw new Error("Блиц не найден");
                const result = await response.json();
                setBlitz(result.data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        if (id) fetchBlitz();
    }, [id]);

    const handleSelect = (questionId, answerId) => {
        setSelectedAnswers(prev => ({
            ...prev,
            [questionId]: answerId
        }));
    };

    const handleSubmit = async () => {
        if (!blitz) return;

        setSubmitting(true);
        setSubmitResult(null);

        try {
            const response = await fetch(`/api/v1/blitzes/${id}/submit`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ answers: selectedAnswers }),
            });

            if (!response.ok) throw new Error("Ошибка при отправке");

            const result = await response.json();
            setSubmitResult(result.data);
        } catch (err) {
            console.error(err);
            alert("Не удалось отправить решение");
        } finally {
            setSubmitting(false);
        }
    };

    if (loading) {
        return (
            <>
                <Header />
                <main className="blitz-loading">
                    <p>Загрузка блица...</p>
                </main>
            </>
        );
    }

    if (error || !blitz) {
        return (
            <>
                <Header />
                <main className="blitz-error">
                    <h2>Ошибка</h2>
                    <p>{error || "Блиц не найден"}</p>
                </main>
            </>
        );
    }

    return (
        <>
            <Header />
            <main>
                <article className="blitz">
                    <ul className="blitz--questions">
                        {blitz.questions?.map((q, index) => (
                            <Question
                                key={q.id}
                                number={q.order_num || index + 1}
                                title={q.text}
                                options={q.answers || []}
                                selectedAnswer={selectedAnswers[q.id]}
                                onSelect={(answerId) => handleSelect(q.id, answerId)}
                            />
                        ))}
                    </ul>

                    <button
                        className="submit-button"
                        onClick={handleSubmit}
                        disabled={submitting}
                    >
                        {submitting ? "Отправка..." : "Сдать решение"}
                    </button>

                    {submitResult && (
                        <div style={{
                            marginTop: "40px",
                            padding: "25px",
                            border: "1px solid #e5e7f1",
                            borderRadius: "12px",
                        }}>
                            <h2 style={{
                                marginBottom: "20px",
                                color: "#333",
                                fontFamily: 'Roboto',
                            }}>Результат блица</h2>

                            <p style={{
                                fontSize: "16px",
                                marginBottom: "25px",
                                padding: "15px",
                                backgroundColor: "#7E14FF10",
                                borderRadius: "8px",
                                border: "1px solid #7E14FF",
                                fontFamily: 'Roboto',
                                fontWeight: "400",
                                color: "#7E14FF",
                            }}>
                                Правильных: <strong>{submitResult.correct_answers}</strong> из{" "}
                                <strong>{submitResult.total_questions}</strong> —
                                <strong style={{ color: "#7E14FF" }}> {submitResult.score_percent}%</strong>
                            </p>

                            <div>
                                {submitResult.results?.map((q, idx) => (
                                    <div key={idx} style={{
                                        padding: "18px",
                                        marginBottom: "15px",
                                        fontFamily: 'Roboto',
                                        backgroundColor: q.is_correct ? "#7E14FF10" : "#ffebee",
                                        borderLeft: `4px solid ${q.is_correct ? "#7E14FF" : "#f44336"}`,
                                        borderRadius: "6px"
                                    }}>
                                        <p style={{ fontWeight: "bold", marginBottom: "10px" }}>
                                            {idx + 1}. {q.question_text}
                                        </p>
                                        <p>
                                            <strong>Ваш ответ:</strong> {q.user_answer_text || "—"}
                                        </p>
                                        {!q.is_correct && q.correct_answer_texts?.length && (
                                            <p>
                                                <strong>Правильный ответ:</strong>{" "}
                                                {q.correct_answer_texts.join(", ")}
                                            </p>
                                        )}
                                    </div>
                                ))}
                            </div>
                        </div>
                    )}
                </article>
            </main>
        </>
    );
}

export default BlitzPage;