import Header from "../Components/header";

import "../styles/page/categorys/banner.scss"
import "../styles/page/categorys/subobjects.scss"
import "../styles/page/categorys/blitzs.scss"
import "../styles/page/categorys/categorys-main.scss"

import rusTestImg from '../assets/img/category/hero/rus_test.png';

function BlitzCard() {
    return (
        <li className={"blitzs__list-element"}>
            <article className={"blitz-card"}>
                <ul className={"tag__list"}>
                    <li className={"tag__list-element"}>9 заданий</li>
                    <li className={"tag__list-element"}>#NBLITZ1</li>
                </ul>
                <p className={"title"}>Синонимы</p>
                <p className={"description"}>Проверь свои знания слов и их значений: подбери правильные синонимы и расширь свой словарный запас!</p>
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
                    <button className={"button__list-element"}>
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

function SubjectsElement() {
    const subobjects = [
        {title: "Русский язык", modif: "--active"},
        {title: "Геометрия", modif: ""},
        {title: "Алгебра", modif: ""},
        {title: "Физика", modif: ""},
        {title: "Информатика", modif: ""},
        {title: "История", modif: ""},
        {title: "Биология", modif: ""},
        {title: "География", modif: ""},
        {title: "ОБЖ", modif: ""},
        {title: "Английский язык", modif: ""},
        {title: "Немецкий язык", modif: ""},
        {title: "Обществознание", modif: ""},
    ]
    return (
        <>
            <aside className={"subobjects"}>
                <p className={"subobjects__title"}>Выберите предмет:</p>
                <ul className={"subobjects__list"}>
                    {subobjects.map((subobject, index) => (
                        <li className={"subobjects__list-element"+subobject.modif}>
                            <button>{subobject.title}</button>
                        </li>
                    ))}
                </ul>
            </aside>
        </>
    )
}

function BlitzsElement() {
    return (
        <>
            <aside className={"blitzs"}>
                <ul className={"blitzs__list"}>
                    <BlitzCard />
                </ul>
            </aside>
        </>
    )
}

function CategorysPage() {
    return (
        <>
            <Header />
            <main>
                <BannerElement />
                <SubjectsElement />
                <BlitzsElement />
            </main>
        </>
    )
}

export default CategorysPage;