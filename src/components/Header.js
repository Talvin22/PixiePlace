import React, { useState } from 'react'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {  faCartShopping, faHeart, faUser, faXmark } from '@fortawesome/free-solid-svg-icons';


export default function Header() {
    // Працюємо з іконками і кнопками
    const [cartOpen, setCartOpen] = useState(false);
    const [likedOpen, setLikedOpen] = useState(false);
    const [loginOpen, setLoginOpen] = useState(false);
    const [registerOpen, setRegisterOpen] = useState(false);
    // Функція для відкриття/закриття вікон
    const toggleWindow = (windowType) => {
      if (windowType === "cart") {
        setCartOpen(!cartOpen);
        setRegisterOpen(false);
        setLikedOpen(false);
        setLoginOpen(false);
      } else if (windowType === "liked") {
        setLikedOpen(!likedOpen);
        setRegisterOpen(false);
        setCartOpen(false);
        setLoginOpen(false);
      } else if (windowType === "login") {
        setLoginOpen(!loginOpen);
        setRegisterOpen(false);
        setCartOpen(false);
        setLikedOpen(false);
      }else if (windowType === "register") {
        setRegisterOpen(!loginOpen);
        setLoginOpen(false);
        setCartOpen(false);
        setLikedOpen(false);
      }
    };
  
    return (
      <header>
        <div className="head">
          <span className="logo">PixiePlase</span>
          <div className="button-container">
            <button className="btn">Жіночий</button>
            <button className="btn">Чоловічий</button>
            <input className="search" placeholder="Введіть товар для пошуку" />
            <button className="btn">Пошук</button>
  
            <FontAwesomeIcon
              onClick={() => toggleWindow("cart")}
              icon={faCartShopping}
              className="icon-shopping"
              id="icon"
            />
            <button onClick={() => toggleWindow("cart")} className="btn">Кошик</button>
  
            <FontAwesomeIcon
              onClick={() => toggleWindow("liked")}
              icon={faHeart}
              className="icon-heart"
              id="icon"
            />
            <button onClick={() => toggleWindow("liked")} className="btn">Бажане</button>
  
            <FontAwesomeIcon
              onClick={() => toggleWindow("login")}
              icon={faUser}
              className="icon-user"
              id="icon"
            />
            <button onClick={() => toggleWindow("login")} className="btn">Увійти</button>
  
            {/* Вікно кошика */}
            {cartOpen && (
              <div className="shop-cart">
                <label className="Basket">Кошик</label>
                <FontAwesomeIcon
                  onClick={() => setCartOpen(false)}
                  icon={faXmark}
                  className="close"
                />
                <div className="buy-commodity"></div>
                <label className="Sum" id="Bask">Бонуси</label>
                <label className="Sum1" id="Bask">Сума товарів</label>
                <label className="Sum2" id="Bask">До сплати</label>
                <button className="Buy" id="Bask">Купити</button>
              </div>
            )}
  
            {/* Вікно бажаного */}
            {likedOpen && (
              <div className="liked">
                <label className="list-liked">Список бажаного</label>
                <FontAwesomeIcon
                  onClick={() => setLikedOpen(false)}
                  icon={faXmark}
                  className="close"
                />
              </div>
            )}
  
            {/* Вікно входу */}
            {loginOpen && (
              <div className="login">
                <label className="entrance">Вхід</label>
                <label htmlFor="email" className="email-label">Введіть пошту</label>
                <input className="email-input" placeholder="Введіть пошту" />
                <label className="password-label">Введіть пароль</label>
                <input className="password-input" placeholder="Введіть пароль" />
                <button className="forgot-password">Забули пароль</button>
                <button className="enter">Увійти</button>
                <button onClick={() => toggleWindow("refister")} className="register">Зареєструватися</button>
              </div>
            )}
          </div>
        </div>
        <div className="presentation"></div>
      </header>
    );
  }