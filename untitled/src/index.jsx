//import "/src/DivWrapper/global.css"
import React from "react";
import ReactDOMClient from "react-dom/client";
import {DivWrapper} from "./DivWrapper";

const app = document.getElementById("app");
const root = ReactDOMClient.createRoot(app);
root.render(<DivWrapper />)