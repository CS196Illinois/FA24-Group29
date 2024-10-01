import React from 'react';

function NavBarComponent() {
    return (
    <>
        <nav className="flex flex-row bg-white border-yellow-300 border-2 rounded-b-xl h-14 justify-between">
            <img className="border-collapse"></img>
            <div className='basis-1/3 -space-x-36'>
                <ul className="grid grid-cols-3 bg-slate-500 text-center h-full">
                    <a className="border-2" href="#">Home</a>
                    <a className="border-2" href="#">Input Music</a>
                    <a className="border-2" href="#">About</a>
                </ul>
            </div>

        </nav>
    </>)
}

export default NavBarComponent;