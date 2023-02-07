import { createContext, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import jwtDecode from "jwt-decode";
import useAuth from "../hooks/useAuth";

const [user, token] = useAuth({})
const SleeperAuth = createContext();

export default SleeperAuth

async function getUser() {
    const token = 
}