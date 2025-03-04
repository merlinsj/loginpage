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
    <div className="flex items-center justify-center min-h-screen bg-gray-200">
      <div className="bg-white p-8 rounded-lg shadow-lg w-96">
        <h2 className="text-2xl font-semibold mb-6 text-center">Login</h2>
        {error && <p className="text-red-500 text-center">{error}</p>}
        <form onSubmit={handleSubmit} className="space-y-4">
          <input type="text" name="username" placeholder="Username" required className="input-style" onChange={handleChange} />
          <input type="password" name="password" placeholder="Password" required className="input-style" onChange={handleChange} />
          <button type="submit" className="btn-primary">Login</button>
        </form>
        <p className="text-center mt-4">
          <a href="/forgot-password" className="text-blue-500">Forgot Password?</a>
        </p>
      </div>
    </div>
  );
};

export default Login;

