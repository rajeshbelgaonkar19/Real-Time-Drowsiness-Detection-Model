// src/pages/Home.js
import React from "react";
import Navbar from "../components/Navbar";
import HeroSection from "../components/HeroSection";
import DetectionParameters from "../components/DetectionParameters";
import Alerts from "../components/Alerts";
import Footer from "../components/Footer";

const Home = () => {
    return (
        <>
            <Navbar />
            <HeroSection />
            <DetectionParameters />
            <Alerts />
            <Footer />
        </>
    );
};

export default Home;
