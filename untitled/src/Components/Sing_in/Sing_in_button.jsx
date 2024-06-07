import React from "react";
import "./style.css";

export const Sing_in_button = ({ className }) =>{
    return(
        <div className={'sing_in_button ${clssName}'}>
            <div className="text-wrapper">Увійти</div>
            <div className="overlap">
                <div className="rectangle"/>
                <div className="div">Забув пароль</div>
            </div>
            <div className="overlap-group">
                <div className="overlap-group">
                    <div className="rectangle"/>
                    <div className="div">Зареєструвати акаунт</div>
                </div>
            </div>
        </div>
    );
};