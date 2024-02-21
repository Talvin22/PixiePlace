import React, {useState} from "react";
import { FaShoppingCart } from "react-icons/fa"

export default function Header(){
    let [cartOpen, setCartOpen] = useState(false)
    return(
        <header>
            <div>
                <span className='logo'>PixiePlace</span>
                <ul className="nav">
                    <li><a className="bottonCategories">Women</a></li>
                    <li><a className="bottonCategories">Men</a></li>
                </ul>
                <FaShoppingCart onClick={()=> setCartOpen(cartOpen = !cartOpen)} className={`ShopCartBotton $(cartOpen && 'activ')`}/>

                {cartOpen && (
                    <div className='shop-cart'>

                    </div>
                )}
            </div>
            <div className='presentation'></div>
        </header>
    )

}