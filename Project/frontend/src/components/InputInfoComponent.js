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
            <h1> Ready for some accurate music recommendations?</h1>
            <div className = "inputinfo">
                <div className = "info">
                    <h1> This is where the information will go, including instructions!</h1>
                </div>
                <div className = "input">
                    <h1>This is where the form will go.</h1>
                    <div className = "inputforms">
                        <input className = "artistinput" type = "text" value = {artist} onChange = {setArtist}/>
                        <input className = "genreinput" type = "text" value = {genre} onChange = {setGenre}/>
                        <input className = "albuminput" type = "text" value = {album} onChange = {setAlbum}/>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default InputInfoComponent;