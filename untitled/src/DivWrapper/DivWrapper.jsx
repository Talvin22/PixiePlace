import React from "react";
import {Button} from "../Components/Button/Button.jsx";
import "./style.css"

export const DivWrapper =()=>{
    return(
        <div className="div-wrapper">
            <div className="div-2">
                <div className="primary-button-wrapper">
                    <Button className="primary-button-instance" />
                </div>
                <div className="overlap-5">
                    <div className="text-wrapper-6">PixiePlace</div>
                    <img className="rectangle-5"
                    alt="Rectangle"
                    src=""></img>
                </div>
            </div>
        </div>
    )
}
