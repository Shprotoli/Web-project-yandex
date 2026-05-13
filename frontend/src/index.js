import { createRoot } from 'react-dom/client';
import { BrowserRouter, Routes, Route, NavLink } from 'react-router-dom';

import CategorysPage from "./Pages/Categorys";
import BlitzPage from "./Pages/Blitz";
import "./styles/main.scss";

const root = createRoot(document.getElementById('root'));

root.render(
    <BrowserRouter>
        <Routes>
            <Route path="/" element={<CategorysPage />} />
            <Route path="/blitz" element={<BlitzPage />} />
        </Routes>
    </BrowserRouter>
);