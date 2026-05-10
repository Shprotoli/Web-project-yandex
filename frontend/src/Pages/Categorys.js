import {useState, useEffect} from "react";

import Header from "../Components/header";

import "../styles/page/categorys/banner.scss"
import "../styles/page/categorys/subobjects.scss"
import "../styles/page/categorys/blitzs.scss"
import "../styles/page/categorys/categorys-main.scss"

import rusTestImg from '../assets/img/category/hero/rus_test.png';
import {BlackBackground} from "../Components/black_background";

function BlitzCard({idBlitz, title, description}) {
    return (
        <li className={"blitzs__list-element"}>
            <article className={"blitz-card"}>
                <ul className={"tag__list"}>
                    <li className={"tag__list-element"}>9 заданий</li>
                    <li className={"tag__list-element"}>{`#NBLITZ${idBlitz}`}</li>
                </ul>
                <p className={"title"}>{title}</p>
                <p className={"description"}>{description}</p>
                <ul className={"button__list"}>
                    <button className={"button__list-element"}>
                        Решать
                        <svg style={{
                            marginLeft: "36px",
                        }} width="30" viewBox="0 0 26 26" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <rect width="26" height="26" rx="5" fill="white"/>
                            <path d="M8.05124 16.7199C7.71278 17.0583 7.71278 17.6071 8.05124 17.9455C8.38969 18.284 8.93843 18.284 9.27689 17.9455L8.66406 17.3327L8.05124 16.7199ZM18.1974 8.66602C18.1974 8.18737 17.8094 7.79935 17.3307 7.79935H9.53073C9.05208 7.79935 8.66406 8.18737 8.66406 8.66602C8.66406 9.14466 9.05208 9.53268 9.53073 9.53268H16.4641V16.466C16.4641 16.9447 16.8521 17.3327 17.3307 17.3327C17.8094 17.3327 18.1974 16.9447 18.1974 16.466V8.66602ZM8.66406 17.3327L9.27689 17.9455L17.9436 9.27884L17.3307 8.66602L16.7179 8.05319L8.05124 16.7199L8.66406 17.3327Z" fill="#7E14FF"/>
                        </svg>
                    </button>
                    <button className={"button__list-element"} onClick={() => navigator.clipboard.writeText(`https://blitz.ru/blitz/${idBlitz}`)}>
                        Поделиться
                        <svg style={{
                            marginLeft: "24px",
                        }} width="34" height="30" viewBox="0 0 26 26" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <rect width="26" height="26" rx="5" fill="#7E14FF"/>
                            <path d="M10.75 8.16667L13 6M13 6L15.25 8.16667M13 6V13.2222M9.25017 11.0556C8.55126 11.0556 8.20181 11.0556 7.92614 11.1655C7.55861 11.3121 7.26642 11.5935 7.11418 11.9474C7 12.2128 7 12.5492 7 13.2222V16.6889C7 17.4978 7 17.9021 7.16349 18.211C7.3073 18.4828 7.5366 18.7042 7.81885 18.8427C8.1394 19 8.55924 19 9.39768 19H16.6027C17.4411 19 17.8604 19 18.1809 18.8427C18.4631 18.7042 18.6929 18.4828 18.8366 18.211C19 17.9024 19 17.4985 19 16.6911V13.2222C19 12.5492 18.9999 12.2128 18.8858 11.9474C18.7335 11.5935 18.4415 11.3121 18.074 11.1655C17.7983 11.0556 17.4489 11.0556 16.75 11.0556" stroke="white" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </button>
                </ul>
            </article>
        </li>
    )
}

function BannerElement() {
    return (
        <>
            <aside className={"banner"}>
                <article className={"banner-objects"}>
                    <svg className={"banner-objects__left"} width="200px" viewBox="0 0 192 131" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M-50.8516 18L2.75934 20.8594C22.0905 21.8905 38.9749 34.2746 45.7658 52.4031L67.6634 110.86C72.8748 124.772 84.1523 135.544 98.2886 140.113L173.279 164.349" stroke="white" stroke-width="36" stroke-linecap="round"/>
                    </svg>

                    <svg className={"banner-objects__right"} width="140px" viewBox="0 0 115 108" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M165.945 86.3809L129.241 88.8954C100.354 90.8744 72.7472 76.6884 57.5376 52.0495L18 -12" stroke="white" stroke-width="36" stroke-linecap="round"/>
                    </svg>
                </article>
                <article className={"banner-text"}>
                    <p className={"banner-text__subject"}>
                        Русский язык
                        <div className={"banner-text__citata-block"}>
                            <p className={"banner-text__citata"}>
                                «У каждой части речи свои достоинства» - А.М.Пешковский
                            </p>
                        </div>
                    </p>
                </article>
                <article className={"banner-heros"}>
                    <article className={"banner-heros__obj-first"}>
                        <img src={rusTestImg} alt="" />
                        <p>И. Н. Горелов</p>
                    </article>
                    <article className={"banner-heros__obj-second"}>
                        <img src={rusTestImg} alt="" />
                        <p>И. Н. Горелов</p>
                    </article>
                </article>
            </aside>
        </>
    )
}

function SubjectsElement({idActiveSubject, setIdActiveSubject}) {
    const subobjects = [
        {title: "Русский язык", modif: "--active", id: "russian-lang"},
        {title: "Геометрия", modif: "", id: "geometry"},
        {title: "Алгебра", modif: "", id: "algebra"},
        {title: "Физика", modif: "", id: "physics"},
        {title: "Информатика", modif: "", id: "informatic"},
        {title: "История", modif: "", id: "history"},
        {title: "Биология", modif: "", id: "biology"},
        {title: "География", modif: "", id: "geography"},
        {title: "ОБЖ", modif: "", id: "obz"},
        {title: "Английский язык", modif: "", id: "anglish-lang"},
        {title: "Немецкий язык", modif: "", id: "german-lang"},
        {title: "Обществознание", modif: "", id: "social"},
    ]
    return (
        <aside className="subobjects">
            <p className="subobjects__title">Выберите предмет:</p>
            <ul className="subobjects__list">
                {subobjects.map((subject) => {
                    const isActive = subject.id === idActiveSubject;

                    return (
                        <li
                            key={subject.id}
                            id={subject.id}
                            className={`subobjects__list-element ${isActive ? 'subobjects__list-element--active' : ''}`}
                        >
                            <button onClick={() => setIdActiveSubject(subject.id)
                            }>
                                {subject.title}
                            </button>
                        </li>
                    );
                })}
            </ul>
        </aside>
    );
}

function BlitzSharedModal({isOpen, onClose}) {
    if (!isOpen) return null;

    return (
        <>
            <BlackBackground onClose={onClose}></BlackBackground>
            <article className={"shared"}>
                <aside className={"qr"}>
                    <img
                        src="https://avatars.mds.yandex.net/i?id=a2616b197111e665538889af97c5977e263ce881-10640589-images-thumbs&n=13"
                        alt="QRCode"
                    />
                </aside>
                <aside className={"body"}>
                    <ul className={"body--tags"}>
                        <li id={"shared-subject"} className={"body--tags-element"}>
                            <p>Французский язык</p>
                        </li>
                        <li id={"count-question"} className={"body--tags-element"}>
                            <p>39 заданий</p>
                        </li>
                        <li id={"blitz-id"} className={"body--tags-element"}>
                            <p>#NBLITZ5821</p>
                        </li>
                    </ul>
                    <p className={"body--title"}>Поделись Blitz-ом с другими!</p>
                    <div className={"body--link"}>
                        <p>https://blitz.ru/blitz/russ-lang/5821</p>
                        <svg width="34" viewBox="0 0 26 26" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <rect width="26" height="26" rx="5" fill="#7E14FF"/>
                            <path d="M15.16 6.33398H12.5639C11.3877 6.33398 10.4561 6.33396 9.72703 6.43238C8.97667 6.53367 8.36935 6.74708 7.89039 7.22796C7.41145 7.70883 7.19889 8.3186 7.09801 9.07196C6.99998 9.80398 6.99999 10.7393 7 11.9202V15.8119C7 16.8173 7.6133 17.6789 8.48478 18.0401C8.43993 17.4339 8.43996 16.5831 8.44 15.8753V12.5991V12.5356C8.43995 11.6811 8.43991 10.9449 8.51885 10.3554C8.60346 9.72357 8.79426 9.11793 9.28353 8.62669C9.77281 8.13544 10.376 7.94388 11.0053 7.85894C11.5925 7.77968 12.3258 7.77972 13.1768 7.77976L13.24 7.77977H15.16L15.2232 7.77976C16.0742 7.77972 16.8059 7.77968 17.3931 7.85894C17.0418 6.96584 16.1744 6.33398 15.16 6.33398Z" fill="white"/>
                            <path d="M9.39844 12.5976C9.39844 10.7801 9.39844 9.87141 9.96079 9.3068C10.5231 8.74219 11.4282 8.74219 13.2384 8.74219H15.1584C16.9686 8.74219 17.8737 8.74219 18.4361 9.3068C18.9984 9.87141 18.9984 10.7801 18.9984 12.5976V15.8105C18.9984 17.6279 18.9984 18.5367 18.4361 19.1013C17.8737 19.6659 16.9686 19.6659 15.1584 19.6659H13.2384C11.4282 19.6659 10.5231 19.6659 9.96079 19.1013C9.39844 18.5367 9.39844 17.6279 9.39844 15.8105V12.5976Z" fill="white"/>
                        </svg>
                    </div>
                </aside>
            </article>
        </>
    )
}

function BlitzsElement({idActiveSubject}) {
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        if (isModalOpen) {
            document.body.style.overflow = 'hidden';
        } else {
            document.body.style.overflow = 'visible';
        }

        return () => {
            document.body.style.overflow = 'visible';
        };
    }, [isModalOpen]);

    useEffect(() => {
        const fetchData = async () => {
            setLoading(true);
            setError(null);
            setData([]);

            try {
                const response = await fetch(`http://127.0.0.1:8080/blitzes/subject/${idActiveSubject}`);

                if (!response.ok) {
                    throw new Error(`Ошибка: ${response.status}`);
                }

                const json = await response.json();
                setData(json.data);
                console.log(json.data);
            } catch (err) {
                setError(err instanceof Error ? err.message : 'Неизвестная ошибка');
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, [idActiveSubject]);

    return (
        <>
            <aside className={"blitzs"}>
                <ul className={"blitzs__list"}>
                    {data && data.length > 0 && (
                        <ul className="blitzs__list">
                            {data.map((blitz) => (
                                <BlitzCard
                                    idBlitz={blitz.id}
                                    title={blitz.title}
                                    description={blitz.description}
                                    key={blitz.id || `blitz-${Math.random()}`}
                                    blitz={blitz}
                                />
                            ))}
                        </ul>
                    )}
                </ul>
            </aside>
        </>
    )
}

function CategorysPage() {
    const [idActiveSubject, setIdActiveSubject] = useState("russian-lang");

    return (
        <>
            <Header />
            <main>
                <BannerElement />
                <SubjectsElement idActiveSubject={idActiveSubject} setIdActiveSubject={setIdActiveSubject} />
                <BlitzsElement idActiveSubject={idActiveSubject}/>
            </main>
        </>
    )
}

export default CategorysPage;