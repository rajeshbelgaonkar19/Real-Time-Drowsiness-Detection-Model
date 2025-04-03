import React from 'react';

function App() {
  const startDetection = async () => {
    try {
      const response = await fetch("http://localhost:5000/start", {
        method: "POST",
        headers: { "Content-Type": "application/json" }
      });
      const data = await response.json();
      alert(data.message);
    } catch (error) {
      console.error("Error starting detection:", error);
    }
  };

  return (
    <div>
      <h1>Drowsiness Detection System</h1>
      <button onClick={startDetection}>Start Drowsiness Detection</button>
    </div>
  );
}

export default App;
