// src/App.js
import React from 'react';
import Chat from './components/Chat';
import Booking from './components/Booking';
import './App.css';

function App() {
    return (
        <div className="App">
            <h1>Hotel Booking Chatbot</h1>
            <Chat />
            <Booking />
        </div>
    );
}

export default App;
