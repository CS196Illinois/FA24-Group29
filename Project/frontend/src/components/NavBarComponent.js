import React from 'react';
import logoImg from './img/MusicLogo.jpg'


function NavBarComponent() {
    return (
    <>
        <header className="fpy-4 bg-black sm:py-6 h-25">
            <div className="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8 flex flex-row justify-between">
                <div className="flex items-center">
                    <img className="w-auto h-20" src={logoImg} alt="Img not found"/>
                </div>

                <nav>
                    <div className="pt-8 pb-4 space-x-10">
                        <a href="#" title="" className="text-base font-normal text-gray-400 transition-all duration-200 hover:text-white"> Home </a>

                        <a href="#" title="" className="text-base font-normal text-gray-400 transition-all duration-200 hover:text-white"> Input Music </a>

                        <a href="#" title="" className="text-base font-normal text-gray-400 transition-all duration-200 hover:text-white"> About </a>
                    </div>
                </nav>
            </div>
        </header>
    </>)
}

export default NavBarComponent;