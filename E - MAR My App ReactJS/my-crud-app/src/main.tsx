// src/main.tsx
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import DataProvider from './context/DataContext';

ReactDOM.render(
  <React.StrictMode>
    <DataProvider>
      <App />
    </DataProvider>
  </React.StrictMode>,
  document.getElementById('root')
);
