import React from "react";
import { useState } from "react";
import transition from "../transition";
import "../App.css";

const Contact = () => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        message: ''
    });
    const [fake_field, setFakeField] = useState('')

    // Handle input changes
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    // Handle form submission
    const handleSubmit = (e) => {
        e.preventDefault();
        // Add your logic to send the form message here
        console.log('Form submitted:', formData);
    };
    return (
        <div className="centered-form-container">
            <form onSubmit={handleSubmit} className="centered-form">
                <label>
                    Name:
                    <input
                        type="text"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                    />
                </label>
                <label>
                    Email:
                    <input
                        type="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                    />
                </label>
                <label>
                    Message:
                    <textarea
                        name="message"
                        value={formData.message}
                        onChange={handleChange}
                        rows="5" // Increase the number of rows for a larger input area
                    />
                </label>
                <button type="submit">Send Message</button>
                <input type="hidden" name="fake_field" value={fake_field} onChange={e => setFakeField(e.target.value)} />
            </form>
        </div>
    );
};
{/*<div>
            <form className="form">
                <div className="form-wrapper">
                    <div className="form-item">
                        <label htmlFor="name">Name</label>
                        <input type="text" id="name" name="name" value={name} onChange={e => setName(e.target.value)}/>
                    </div>

                    <div className="form-item">
                        <label htmlFor="email">Email</label>
                        <input type="email" id="email" name="email" value={email} onChange={e => setEmail(e.target.value)}/>
                    </div>

                    <div className="form-item">
                        <label htmlFor="message">Message</label>
                        <textarea id="message" name="message" value={message} onChange={e => setMessage(e.target.value)}/>
                    </div>

                    <button className="form-item" type="submit" onClick={handleSubmit}>Submit</button>

                    <input type="hidden" name="fake_field" value={fake_field} onChange={e => setFakeField(e.target.value)}/>
                </div>
            </form>
        </div>
    )
}*/}

export default transition(Contact);