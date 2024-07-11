// src/components/Booking.js
import React, { useState } from 'react';
import axios from 'axios';
import './Booking.css';

const Booking = () => {
    const [details, setDetails] = useState({ name: '', roomType: '', dates: '' });
    const [message, setMessage] = useState('');

    const bookRoom = async () => {
        const response = await axios.post('http://localhost:5000/book', details);
        setMessage(response.data.message);
    };

    return (
        <div className="booking-container">
            <h2>Book a Room</h2>
            <input
                type="text"
                placeholder="Name"
                value={details.name}
                onChange={(e) => setDetails({ ...details, name: e.target.value })}
            />
            <input
                type="text"
                placeholder="Room Type"
                value={details.roomType}
                onChange={(e) => setDetails({ ...details, roomType: e.target.value })}
            />
            <input
                type="text"
                placeholder="Dates"
                value={details.dates}
                onChange={(e) => setDetails({ ...details, dates: e.target.value })}
            />
            <button onClick={bookRoom}>Book</button>
            {message && <p className="message">{message}</p>}
        </div>
    );
};

export default Booking;
