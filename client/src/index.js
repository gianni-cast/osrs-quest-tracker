import React from "react";
import App from "./components/App";
import "./index.css";
import { createRoot } from "react-dom/client";
import {
    createBrowserRouter,
    RouterProvider,
    Route,
    Link,
    BrowserRouter,
  } from "react-router-dom";
import Home from "./components/Home";

const container = document.getElementById("root");
const root = createRoot(container);

root.render(
    <BrowserRouter>
        <App />
    </BrowserRouter>
    );
