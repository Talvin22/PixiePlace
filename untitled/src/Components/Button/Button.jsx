import React from "react";
import "./style.css"

export const Button = ({className}) =>{
    return(
    <div className={`button ${className}`}>
        <div className="overlap">
        <div className="rectangle" />
        <div className="text-wrapper">Жіночий</div>
    </div>

        <div className="overlap-group">
        <div className="div"/>
        <div className="text-wrapper2">Чоловічий</div>
    </div>

    <div className="overlap-group2">
        <div className="rectangle2"/>
        <div className="text-wrapper3">Кошик</div>
    </div>

    <img className="vector" alt="Vector"/>
    <div className="overlap2">
        <div className="rectangle3"/>
        <div className="text-wrapper4">Увійти</div>
    </div>

    <img className="img" alt="Vector"/>
    <div className="overlap3">
        <div className="retangle2"/>
        <div className="text-wrapper3">Бажане</div>
    </div>

    <img className="vector2" alt="Vector"/>
    <div className="overlap4">
        <div className="rectangle4"/>
        <div className="text-wrapper5">Пошук</div>
    </div>

    <img className="vector3" alt="Vector"/>

    </div>

    );
};