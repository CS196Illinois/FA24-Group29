import React from "react";
import {Link} from 'react-router-dom';
import newlogoImg from './img/soundlogo.png'

function HomePageBodyComponent() {
    return (<>
    <section class="py-12 bg-[#0C1821] sm:pb-16 lg:pb-20 xl:pb-24">
        <div class="px-4 mx-auto sm:px-6 lg:px-8 max-w-7xl pt-20">
            <div class="relative">
                <div class="lg:w-2/3">
                    <p class="max-w-lg text-sm font-normal tracking-wider text-gray-300 uppercase">Getting Better Music Recommendations</p>
                    <h1 class="max-w-lg mt-6 text-4xl font-normal text-white sm:mt-10 sm:text-5xl lg:text-6xl xl:text-8xl"><span class="text-transparent text-[#CCC9DC]">Perfect Your</span> Playlists</h1>
                    <p class="max-w-lg mt-4 text-xl font-normal text-gray-400 sm:mt-8">Our machine learning models analyzes many various features of songs including tempo, genre, and lyrics. Input any song or playlist into our model and we'll give you recommendations. Add more info about how model works.</p>
                    <div class="mr-72 relative inline-flex items-center justify-center mt-8 sm:mt-12 group">
                        <div class="absolute transition-all duration-200 rounded-full -inset-px bg-blue-500 group-hover:shadow-lg group-hover:shadow-[#324A5F]"></div>
                        <Link to='/inputinfo' title="" class="relative inline-flex items-center justify-center px-8 py-3 text-base font-normal text-white bg-black border border-transparent rounded-full" role="button"> Get Started With Music </Link>
                    </div>

                    <div>
                        <div class="mr-72 pr-4 inline-flex items-center pt-6 mt-8 border-t border-gray-800 sm:pt-10 sm:mt-14">
                            <span class="ml-2 text-base font-normal text-gray-400"> Over 10,000+ songs recommended to users or some other value</span>
                        </div>
                    </div>
                </div>

                <div class="mt-8 ml-20 md:absolute lg:top-0 md:right-0">
                    <img class="w-full max-w-xs mx-auto lg:max-w-lg xl:max-w-xl" src= {newlogoImg} alt="Red and Black Spotify Logo" />
                </div>
            </div>
        </div>
    </section>
    </>)
}

export default HomePageBodyComponent;