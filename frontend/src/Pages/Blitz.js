import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";

import Header from "../Components/header";
import "../styles/page/blitz/blitz.scss";


function Question({
                      number,
                      title,
                      options = []   // теперь это массив объектов {id, text, is_correct, ...}
                  }) {
    return (
        <li className="blitz--card">
            <h2 className="blitz--question">
                {number}. {title}
            </h2>

            <ul className="blitz--options">
                {options.map((answer, index) => {
                    const letter = String.fromCharCode(65 + index); // A, B, C...
                    const optionId = `q${number}o${answer.id || index}`;

                    return (
                        <li key={answer.id || index} className="option">
                            <input
                                type="radio"
                                name={`question${number}`}
                                id={optionId}
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

    useEffect(() => {
        const fetchBlitz = async () => {
            try {
                setLoading(true);
                const response = await fetch(`http://127.0.0.1:8080/api/v1/blitzes/${id}`);

                if (!response.ok) {
                    throw new Error("Блиц не найден");
                }

                const result = await response.json();
                console.log(result);

                setBlitz(result.data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        if (id) fetchBlitz();
    }, [id]);

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
                    <div className="blitz__header">
                        <h1 id="blitz-title">{blitz.title}</h1>
                    </div>

                    <ul className="blitz--questions">
                        {blitz.questions?.map((q, index) => (
                            <Question
                                key={q.id}
                                number={q.order_num || index + 1}
                                title={q.text}
                                options={q.answers}
                            />
                        ))}
                    </ul>
                </article>
            </main>
        </>
    );
}

export default BlitzPage;