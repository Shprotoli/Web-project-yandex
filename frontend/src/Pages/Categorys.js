import Header from "../Components/header";

import "../styles/page/categorys/banner.scss"
import "../styles/page/categorys/subobjects.scss"
import "../styles/page/categorys/categorys-main.scss"

import rusTestImg from '../assets/img/category/hero/rus_test.png';

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

function CategorysPage() {
    return (
        <>
            <Header />
            <main>
                <BannerElement />
                <SubjectsElement />
            </main>
        </>
    )
}

export default CategorysPage;