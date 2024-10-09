import React from 'react';
import './inputinfo.css';
import { useState } from 'react';

function InputInfoComponent() {

    const [errorMessage, setErrorMessage] = useState("");

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

    const resetValues = () => {
        setArtist("");
        setGenre("");
        setAlbum("");
    }

    const handleSubmit = (e) => {
        e.preventDefault();

        if (artist == "" || genre == "" || album == "") {
            setErrorMessage("All fields are required for a good music recommendation!");
        } else {
            setErrorMessage("");
        }
    }



    return (
        <div className = "body">
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
                        3. Finally, put in your favorite album for an accurate music recommendation!
                    </p>
                </div>
                <div className = "input">
                    <div className = "inputforms">
                            <label className = "label">Favorite artist</label>
                            <input placeholder = "Your favorite artist goes here!" className = "artistinput" type = "text" value = {artist} onChange = {handleArtist}/>
                            <label className = "label">Favorite Genre</label>
                            <input placeholder = "Your favorite genre goes here!" className = "genreinput" type = "text" value = {genre} onChange = {handleGenre}/>
                            <label className = "label">Favorite Album</label>
                            <input placeholder = "Your favorite artist goes here!" className = "albuminput" type = "text" value = {album} onChange = {handleAlbum}/>
                            <div className = "buttons">
                                <button onClick = {resetValues} className = "resetbutton">Reset responses</button>
                                <button onClick = {handleSubmit} className = "submitbutton">Submit</button>
                                {errorMessage && <p style = {{color: "red"}}>{errorMessage}</p>}
                            </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default InputInfoComponent;