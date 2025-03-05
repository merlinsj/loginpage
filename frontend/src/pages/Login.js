import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const Login = () => {
  const [formData, setFormData] = useState({ username: "", password: "" });
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://localhost:8000/accounts/login/", formData);
      localStorage.setItem("token", res.data.token);
      navigate(res.data.role === "admin" ? "/admin-dashboard" : "/dashboard");
    } catch (err) {
      setError("Invalid username or password.");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-purple-500 to-blue-600">
      <div className="w-[450px] backdrop-blur-md bg-white/30 p-8 rounded-2xl shadow-lg max-w-md w-full">
        <h2 className="text-4xl font-bold text-center text-white mb-8">Login</h2>

        {error && <p className="text-center text-red-500 mb-4">{error}</p>}

        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="flex items-center bg-white/80 p-3 rounded-lg border">
       
            <input 
              type="text" 
              name="username" 
              placeholder="Username" 
              value={formData.username} 
              onChange={handleChange} 
              required 
              className="w-full bg-transparent outline-none text-gray-700"
            />
          </div>

          <div className="flex items-center bg-white/80 p-3 rounded-lg border">
           
            <input 
              type="password" 
              name="password" 
              placeholder="Password" 
              value={formData.password} 
              onChange={handleChange} 
              required 
              className="w-full bg-transparent outline-none text-gray-700"
            />
          </div>

          <div className="flex items-center justify-between w-full mt-2">
  <a href="/forgot-password" className="text-blue-300 hover:underline">
    Forgot Password?
  </a>
</div>




          <button 
            type="submit" 
            className="w-full py-3 bg-blue-700 text-white font-bold rounded-lg hover:bg-blue-800 transition"
          >
            Login
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;
