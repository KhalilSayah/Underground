import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import Wallet from './Wallet.jsx'
import './index.css'
import 'bootstrap/dist/css/bootstrap.min.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
ReactDOM.createRoot(document.getElementById('connection')).render(
  <React.StrictMode>
    <Wallet />
  </React.StrictMode>,
)