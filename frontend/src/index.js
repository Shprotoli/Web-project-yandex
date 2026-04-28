import React from 'react';
import ReactDOM from 'react-dom/client';
import reportWebVitals from "./reportWebVitals";

import CategorysPage from "./Pages/Categorys";

import "./styles/main.scss"

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
      <CategorysPage></CategorysPage>
  </React.StrictMode>
);

reportWebVitals();
