import React, { useState, useEffect } from 'react';

import api from '../API/CatDog';
import Header from '../Components/Layout/Header'
import ScrollState from '../Components/Layout/ScrollState';
import Footer from '../Components/Layout/Footer'

///////////////////////////////////////////
import {
    UploadIcon,
} from '@heroicons/react/outline'

//import CNNPng from "../Assets/images/cnn.png"




function Main() {

    const [wheel, setWheel] = useState(0);
    const [wheelPercent, setWheelPercent] = useState(0);


    useEffect(() => {

    }, [])

    ///////////////////////////
    const onWheelState = (e) => {
        let _wheel = wheel + e.deltaY * 1.5

        if (wheel < 0) {
            _wheel = 0
        }

        if (wheel > document.body.scrollHeight) {
            _wheel = document.body.scrollHeight
        }

        let _wheelPercent = Number(_wheel / document.body.scrollHeight * 100)

        setWheel(_wheel);
        setWheelPercent(_wheelPercent);
    }

    return (
        <div className="min-w-screan min-h-full" onWheel={onWheelState} >
            <Header />
            <ScrollState
                wheelPercent={wheelPercent}
            />

            <Footer />
        </div>
    )
}

export default Main;