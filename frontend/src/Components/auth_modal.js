import { createPortal } from 'react-dom';
import { useState, useRef, useEffect } from "react";

import { BlackBackground } from "./black_background";
import "../styles/auth-modal.scss";

function ModalInputComponent({ titleInput, typeInput = "text", inputRef }) {
    return (
        <li className="input-list__item">
            <aside>
                <p>{titleInput}</p>
                <input
                    ref={inputRef}
                    required
                    type={typeInput}
                />
            </aside>
        </li>
    );
}

function AuthModal({ isOpen, onClose }) {
    const [mode, setMode] = useState('auth');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const emailRef = useRef(null);
    const passwordRef = useRef(null);
    const regEmailRef = useRef(null);
    const nicknameRef = useRef(null);
    const regPasswordRef = useRef(null);
    const confirmPasswordRef = useRef(null);

    const handleLogin = async () => {
        setError(null);
        setLoading(true);

        const username = emailRef.current?.value?.trim();
        const password = passwordRef.current?.value;

        if (!username || !password) {
            setError("Заполните email и пароль");
            setLoading(false);
            return;
        }

        try {
            const res = await fetch('http://127.0.0.1:8080/auth/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password }),
            });

            const data = await res.json();

            if (!res.ok) {
                throw new Error(data.message || data.error || "Ошибка входа");
            }

            const token = data.data.session?.token;

            if (!token) {
                throw new Error("Токен не найден в ответе");
            }

            localStorage.setItem('authToken', token);
            window.location.reload();
            onClose();

        } catch (err) {
            setError(err.message || "Не удалось войти");
        } finally {
            setLoading(false);
        }
    };

    const handleRegister = async () => {
        setError(null);
        setLoading(true);

        const username = nicknameRef.current?.value?.trim();
        const email = regEmailRef.current?.value?.trim();
        const password = regPasswordRef.current?.value;
        const confirmPassword = confirmPasswordRef.current?.value;

        if (!username || !email || !password || !confirmPassword) {
            setError("Заполните все поля");
            setLoading(false);
            return;
        }

        if (password !== confirmPassword) {
            setError("Пароли не совпадают");
            setLoading(false);
            return;
        }

        try {
            const res = await fetch('http://127.0.0.1:8080/auth/register', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    username,
                    email,
                    password,
                    confirm_password: confirmPassword,
                }),
            });

            const data = await res.json();

            if (!res.ok) throw new Error(data.message || "Ошибка регистрации");

            alert("Регистрация прошла успешно! Теперь можете войти.");
            setMode('auth');
            setError(null);

            regEmailRef.current.value = '';
            nicknameRef.current.value = '';
            regPasswordRef.current.value = '';
            confirmPasswordRef.current.value = '';
        } catch (err) {
            setError(err.message || "Не удалось зарегистрироваться");
        } finally {
            setLoading(false);
        }
    };

    const toggleMode = () => {
        setMode(prev => prev === 'auth' ? 'register' : 'auth');
        setError(null);
    };

    if (!isOpen) return null;

    return createPortal(
        <>
            <BlackBackground onClose={onClose} />

            <div className="auth-modal">
                <aside className="background-items" />

                <aside className="body">
                    <ul className="input-list">
                        <aside className="input-list__item-auth" style={{ display: mode === "auth" ? "block" : "none" }}>
                            <ModalInputComponent titleInput="Введите почту" inputRef={emailRef} />
                            <ModalInputComponent titleInput="Введите пароль" typeInput="password" inputRef={passwordRef} />
                        </aside>

                        <aside className="input-list__item-register" style={{ display: mode === "register" ? "block" : "none" }}>
                            <ModalInputComponent titleInput="Введите регистрационную почту" inputRef={regEmailRef} />
                            <ModalInputComponent titleInput="Введите желаемый ник" inputRef={nicknameRef} />
                            <ModalInputComponent titleInput="Введите пароль" typeInput="password" inputRef={regPasswordRef} />
                            <ModalInputComponent titleInput="Повторите пароль" typeInput="password" inputRef={confirmPasswordRef} />
                        </aside>
                    </ul>

                    {error && <p style={{ color: 'red', textAlign: 'center', margin: '10px 0' }}>{error}</p>}

                    <ul className="button-list">
                        <li className="button-list__auth">
                            <button onClick={mode === "auth" ? handleLogin : handleRegister} disabled={loading}>
                                {loading ? "Загрузка..." : mode === "auth" ? "Войти" : "Зарегистрироваться"}
                            </button>
                        </li>

                        <li className="button-list__register" onClick={toggleMode}>
                            <button>
                                {mode === "auth" ? "Зарегистрировать аккаунт" : "Войти в аккаунт"}
                            </button>
                        </li>
                    </ul>
                </aside>
            </div>
        </>,
        document.body
    );
}

export default AuthModal;