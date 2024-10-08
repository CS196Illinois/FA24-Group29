import React from 'react';
import './inputinfo.css';
import { useState } from 'react';

function InputInfoComponent() {

    const [artist, setArtist] = useState("");
    const handleArtist = (e) => {
        setArtist(e.target.value);
    } 
    const [genre, setGenre] = useState("");
    const handleGenre = (e) => {
        setGenre(e.target.value);
    } 
    const [album, setAlbum] = useState("");
    const handleAlbum = (e) => {
        setAlbum(e.target.value);
    } 



    return (
        <div className = "body">
            <h1 className = "bigheader"> Ready for some accurate </h1>
            <h className = "recommendations"> music recommendations?</h>
            <div className = "inputinfo">
                <div className = "info">
                    <p> 
                        <p className = "directions">The directions are pretty simple!</p><br />
                        1. Now what you first want to do is input your favorite artist's name.<br />
                        <span className = "extraspace"></span>
                        2. Next, you want to input your favorite genre of music! <br />
                        <span className = "extraspace"></span>
                        3. Finally, put in your favorite album for an accurate music recommendation!
                    </p>
                </div>
                <div className = "input">
                    <div className = "inputforms">
                        <label>Favorite artist</label>
                        <input autofocus placeholder = "Your favorite artist" className = "artistinput" type = "text" value = {artist} onChange = {handleArtist}/>
                        <label>Favorite genre</label>
                        <input placeholder = "Your favorite genre" className = "genreinput" type = "text" value = {genre} onChange = {handleGenre}/>
                        <label>Favorite album</label>
                        <input placeholder = "Your favorite artist" className = "albuminput" type = "text" value = {album} onChange = {handleAlbum}/>
                        <button className = "resetbutton">Reset responses</button>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default InputInfoComponent;