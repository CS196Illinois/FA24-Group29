import React from 'react';
import logoImg from './img/MusicLogo.jpg'


function NavBarComponent() {
    return (
    <>
        <header className="fpy-4 pt-4 bg-black h-25">
            <div className="px-36 ml-1 mr-1 mx-auto max-w-full h-full flex flex-row justify-between">
                <div className="flex items-center">
                    <img className="w-auto h-20" src={logoImg} alt="Img not found"/>
                </div>

                <nav>
                    <div className="pt-7 pb-7 space-x-10 h-full">
                        <a href="#" title="" className="text-base font-normal text-gray-400 transition-all duration-200 hover:text-white"> Home </a>

                        <a href="#" title="" className="text-base font-normal text-gray-400 transition-all duration-200 hover:text-white"> Music Recommendations </a>

                        <a href="#" title="" className="text-base font-normal text-gray-400 transition-all duration-200 hover:text-white"> About </a>
                    </div>
                </nav>
            </div>
        </header>
    </>)
}

export default NavBarComponent;