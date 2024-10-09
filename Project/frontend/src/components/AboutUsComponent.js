import React from 'react';
import './aboutus.css';
import {Link} from 'react-router-dom';

function AboutUsComponent() {
    return (
        <d>
            <div className = "bodyaboutus">
                <h1 className = "header">Why did we decide to create this application?</h1>
                <div className = "aboutus">
                    <img className = "spotifylogo" src = "https://i.pinimg.com/originals/71/88/bd/7188bd71e4ec64aa9f464b94388961c8.jpg" alt = "Spotify logo" />
                    <div className = "text">
                        <h1 className = "smalltext">THE FUTURE OF SONG RECOMMENDATIONS. PROVEN MODELS. PROVEN RESULTS</h1>
                        <p1>Imagine taking your favorite artists, genres, and albums, and being able to, from just that information, produce song recommendations that sounded new, but had a similar feel. Something intricate, but personalized.</p1>
                        <span className = "extraspace"></span>
                        <p2>We did the hard part for you! With thorough machine learning models, we are able to give you what you have been waiting for. With just a few vital pieces of information, we can give you accurate, real music recommendations.</p2>
                        <span className = "extraspace"></span>
                        <p3>User enjoyability is our goal, so giving you quality recommendations is our priority, and our methods back it up. So do our results, try it out here! </p3>
                        <span className = "extraspace"></span>
                        <Link to="/inputinfo" className = "transportbutton">Find new music!</Link>
                    </div>
                </div>
            </div>
        </d>
    );
}

export default AboutUsComponent;