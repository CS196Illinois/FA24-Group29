import React from 'react';
import './inputinfo.css';
import { useState } from 'react';

function InputInfoComponent() {

    const [recommendations, setRecommendations] = useState([]); // to store the list of recommended songs

    const [errorMessage, setErrorMessage] = useState("");

    const [trackName, setTrackName] = useState("");
    const handleTrackName = (e) => {
        setTrackName(e.target.value);
    }

    const [artistName, setArtistName] = useState("");
    const handleArtistName = (e) => {
        setArtistName(e.target.value);
    }

    const [genre, setGenre] = useState("");
    const handleGenre = (e) => {
        setGenre(e.target.value);
    }

    const resetValues = () => {
        setTrackName("");
        setArtistName("");
        setGenre("");
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
    
        if (trackName === "" || artistName === "" || genre === "") {
            setErrorMessage("All fields are required for a good music recommendation!");
        } else {
            setErrorMessage("");
            
            // Prepare data to send to the backend
            const requestData = {
                songs: [
                    { track_name: trackName, genre: genre, artist_name: artistName }
                ]
            };
    
try {
            const response = await fetch('http://localhost:5000/recommend', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(requestData),  // Convert the object to a JSON string
            });

            const data = await response.json();
            if (data.recommendations) {
                setRecommendations(data.recommendations);
            } else {
                console.error("Error with recommendations:", data.error);
            }
        } catch (error) {
            console.error("Error fetching recommendations:", error);
            }
        }
    };



    return (
        <div className = "bodyinputinfo">
            <h1 className = "bigheader"> Ready for some accurate </h1>
            <h className = "recommendations"> music recommendations?</h>
            <div className = "inputinfo">
                <div className = "info">
                    <p className = "directionbody"> 
                        <p className = "directions">The directions are pretty simple!</p><br />
                        1. Now what you first want to do is input your favorite artist's name.<br />
                        <span className = "extraspace"></span>
                        2. Next, you want to input your favorite genre of music! <br />
                        <span className = "extraspace"></span>
                        3. Finally, input your favorite track name for an accurate music recommendation!
                    </p>
                </div>
                <div className = "input">
                    <div className = "inputforms">
                            <label className = "label">Favorite artist</label>
                            <input placeholder = "Your favorite artist goes here!" className = "artistinput" type = "text" value = {artistName} onChange = {handleArtistName}/>
                            <label className = "label">Favorite Genre</label>
                            <input placeholder = "Your favorite genre goes here!" className = "genreinput" type = "text" value = {genre} onChange = {handleGenre}/>
                            <label className = "label">Favorite Track</label>
                            <input placeholder = "Your favorite track name goes here!" className = "trackinput" type = "text" value = {trackName} onChange = {handleTrackName}/>
                            <div className = "buttons">
                                <button onClick = {resetValues} className = "resetbutton">Reset responses</button>
                                <button onClick = {handleSubmit} className = "submitbutton">Submit</button>
                                {errorMessage && <p style = {{color: "red"}}>{errorMessage}</p>}
                            </div>
                    </div>
                </div>
                {/* Display Recommendations */}
                {recommendations.length > 0 && (
                    <div className="recommendation-section">
                        <h2>Your Music Recommendations</h2>
                        <ul>
                            {recommendations.map((rec, index) => (
                                <li key={index}>
                                    {rec.track_name} by {rec.artist_name} - Genre: {rec.genre}
                                </li>
                            ))}
                        </ul>
                    </div>
                )}
                {/* End of Recommendations Section */}
            </div>
        </div>
    );
}

export default InputInfoComponent;