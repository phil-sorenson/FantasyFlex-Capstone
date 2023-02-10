// General Imports
import { Routes, Route, useParams } from "react-router-dom";
import "./App.css";
import { KEY } from "./localKey"
import { APP_ID } from "./localKey";

// Pages Imports
import HomePage from "./pages/HomePage/HomePage";
import LoginPage from "./pages/AppLoginPage/LoginPage";
import RegisterPage from "./pages/RegisterPage/RegisterPage";

// Component Imports
import Navbar from "./components/NavBar/NavBar";
import Footer from "./components/Footer/Footer";

// Util Imports
import PrivateRoute from "./utils/PrivateRoute";
import { useState } from "react";
import useAuth from "./hooks/useAuth";
import LoginForm from "./components/PlatformLogin/LoginForm";

const BASE_URL = `https://api.sleeper.app/v1/`;
const DB_URL = `http://127.0.0.1:8000/api/auth/`



function App() {
  
  const [currentUser, setCurrentUser] = useState(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [sleeperUser, setSleeperUser] = useStet(null);
  const [league, setLeague] = useState(null);
  const [user, token] = useAuth();
  const { user_id } = useParams();

  // Authentication

  async function loginUser(user) {
    try {
      await axios.post(`${DB_URL}/sleeper_user/login`, user, {
        headers: {
          Authorization: "Bearer " + token
        }    
      }); 
      const user = await response.json()
      console.log('userLoggedIn', user)
        
    } catch (error) {
      console.log(error.message)
    }
  }

  async function getUser() {
    
  }
  
  return (
    <div>
      <Navbar />
      <Routes>
        <Route
          path="/"
          element={
            <PrivateRoute>
              <HomePage />
            </PrivateRoute>
          }
        />
        <Route path="/platform_login" element={<LoginForm />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/login" element={<LoginPage />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
