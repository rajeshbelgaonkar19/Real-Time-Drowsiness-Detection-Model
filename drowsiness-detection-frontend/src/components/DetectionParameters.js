// src/components/DetectionParameters.js
import React from "react";
import "./DetectionParameters.css";

const DetectionParameters = () => {
    return (
        <div className="parameters">
            <h2>Detection Parameters</h2>
            <div className="parameter-grid">
                <div className="card">
                    <h3>Eye Detection</h3>
                    <p>Monitors eye closure duration to detect drowsiness.</p>
                </div>
                <div className="card">
                    <h3>Mouth Detection</h3>
                    <p>Detects yawning frequency as an indicator of fatigue.</p>
                </div>
                <div className="card">
                    <h3>Head Movement</h3>
                    <p>Tracks unusual head tilts or jerks to identify drowsiness.</p>
                </div>
            </div>
        </div>
    );
};

export default DetectionParameters;
