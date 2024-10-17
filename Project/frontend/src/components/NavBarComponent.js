import React from 'react';
import logoImg from './img/MusicLogo.jpg'
import { Link } from 'react-router-dom';


function NavBarComponent() {
    return (
    <>
    <div className = "fixed w-full z-50">
        <header className="fpy-4 pt-4 bg-black h-25 top-0 w-full">
            <div className="px-36 ml-1 mr-1 mx-auto max-w-full h-full flex flex-row justify-between">
                <div className="flex items-center">
                    <img className="w-auto h-20" src={logoImg} alt="Img not found"/>
                </div>

                <nav>
                    <div className="pt-7 pb-7 space-x-10 h-full">
                        <Link to='/' title="" className="text-base font-normal text-gray-400 transition-all duration-200 hover:text-white"> Home </Link>

                        <Link to='/inputinfo' title="" className="text-base font-normal text-gray-400 transition-all duration-200 hover:text-white"> Music Recommendations </Link>

                        <Link to='/aboutus' title="" className="text-base font-normal text-gray-400 transition-all duration-200 hover:text-white"> About </Link>
                    </div>
                </nav>
            </div>
        </header>
    </div>
    </>)
}

export default NavBarComponent;