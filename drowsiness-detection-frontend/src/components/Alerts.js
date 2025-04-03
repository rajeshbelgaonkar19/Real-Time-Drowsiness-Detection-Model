// src/components/Alerts.js
import React, { useEffect, useState } from "react";
import axios from "axios";
import "./Alerts.css";

const Alerts = () => {
    const [alertData, setAlertData] = useState("");

    useEffect(() => {
        axios.get("http://localhost:5000/detect")
            .then(response => setAlertData(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div className="alert-container">
            <h2>Real-Time Alerts</h2>
            <p>{alertData ? alertData : "No alerts currently"}</p>
        </div>
    );
};

export default Alerts;
