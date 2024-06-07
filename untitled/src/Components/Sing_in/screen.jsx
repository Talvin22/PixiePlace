import React from "react";
import {Sing_in_button} from "./Sing_in_button";
import "./text.css"

export const Screen = () =>{
    return(
        <div className="screen">
            <div className="div2">
                <div className="text-wrapper2">Вхід</div>
                <div className="text-wrapper3">Введіть пошту</div>
                <div className="rectangle2"/>
                <div className="text-wrapper4">Введіть пароль</div>
                <div className="rectangle3"/>
                <Sing_in_button className="sing_in_button1"/>
            </div>
        </div>
    );
};