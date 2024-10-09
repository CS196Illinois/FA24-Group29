import React from 'react';
import "./bottomnavbar.css";
import logoImg from './img/MusicLogo.jpg'

const BottomNavBarComponent = () => {
    return (
        <div className = "bottomnavbar">
            <div className = "text">
                <div className = "column1">
                    <h1>Company</h1>
                    <p1>About Us</p1>
                    <p2>Terms and Conditions</p2>
                    <p3>Privacy Policy</p3>
                </div>
                <div className = "column2">
                    <h1>User Service</h1>
                    <p1>Report a problem</p1>
                    <p2>Contact Us</p2>
                    <p3>Subscription</p3>
                    <p4>Donate</p4>
                </div>
                <div className = "column3">
                    <h1>Connect with Us</h1>
                    <p1 className = "flex">
                        Instagram
                        <img></img>
                    </p1>
                    <p2 className = "flex">
                        Facebook
                        <img></img>
                    </p2>
                    <p3 className = "flex">
                        Snapchat
                        <img></img>
                        </p3>
                    <p4 className = "flex">
                        Twitter
                        <img></img>
                        </p4>
                </div>
            </div>
        </div>
    )
}

export default BottomNavBarComponent;