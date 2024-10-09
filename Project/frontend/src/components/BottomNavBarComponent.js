import React from 'react';
import "./bottomnavbar.css";
import logoImg from './img/MusicLogo.jpg'
import snapchatlogo from "./img/snapchat.png"
import facebooklogo from "./img/facebook.png"
import instagramlogo from "./img/instagram.png"
import twitterlogo from "./img/twitter.png"

const BottomNavBarComponent = () => {
    return (
        <div className = "bottomnavbar">
            <div className = "textbottomnavbar">
                <div className = "column1">
                    <h1 className = "subheading">Company</h1>
                    <p1>About Us</p1>
                    <p2>Terms and Conditions</p2>
                    <p3>Privacy Policy</p3>
                </div>
                <div className = "column2">
                    <h1 className = "subheading">User Service</h1>
                    <p1>Report a problem</p1>
                    <p2>Contact Us</p2>
                    <p3>Subscription</p3>
                    <p4>Donate</p4>
                </div>
                <div className = "column3">
                    <h1 className = "subheading">Connect with Us</h1>
                    <p1>Instagram</p1>
                    <p2>Facebook</p2>
                    <p3>Snapchat</p3>
                    <p4>Twitter</p4>
                </div>
                <div className = "image">
                    <img className = "musiclogo" src={logoImg}></img>
                    <div className = "socialmedialogos">
                        <img className = "smalllogo" src = {snapchatlogo}></img>
                        <img className = "smalllogo" src = {facebooklogo}></img>
                        <img className = "smalllogo" src = {instagramlogo}></img>
                        <img className = "smalllogo" src = {twitterlogo}></img>
                    </div>
                </div>

            </div>
        </div>
    )
}

export default BottomNavBarComponent;