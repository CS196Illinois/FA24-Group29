import React from 'react';
import './aboutus.css';

function AboutUsComponent() {
    return (
        <d>
            <div className = "bodyaboutus">
                <div className = "text">
                    <h1 className = "question">Why create this application?</h1>
                        <div className = "longText">
                            <div className = "text1">
                                <p1 className = "shortp1">We thought it was time for you to experience good music based on what you usually listen to! It's as simple as that!</p1>
                                <p2 className = "shortp2">Based on proven machine learning models, we take in your information, and 
                                                        return to you accurate music recommendations based on music that you manually put in. Our vigorous and thorough models are ready 
                                                        to give you enjoyment as you listen to music that is new, invigorating, yet similar!</p2>
                            </div>
                            <img className = "spotifyimg" src = "https://i.pinimg.com/originals/71/88/bd/7188bd71e4ec64aa9f464b94388961c8.jpg" alt = "red spotify img"/>
                        </div>
                </div>
            </div>
        </d>
    );
}

export default AboutUsComponent;