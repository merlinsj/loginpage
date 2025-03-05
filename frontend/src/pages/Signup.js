// src/pages/Signup.js

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Signup = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    role: '',
    security_code: ''
  });

  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSignup = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://127.0.0.1:8000/accounts/signup/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      if (response.ok) {
        alert('Signup successful! Redirecting to login...');
        navigate('/login');
      } else {
        alert(data.error || 'Signup failed');
      }
    } catch (error) {
      console.error('Signup error:', error);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-purple-400 to-blue-500">
      <div className="backdrop-blur-lg bg-white/20 p-8 rounded-2xl shadow-lg max-w-md w-full">
        <div className="flex justify-center mb-6">
          <div className="w-20 h-20 bg-white/30 rounded-full flex items-center justify-center">
           
          </div>
        </div>

        <h2 className="text-3xl font-bold text-center text-white mb-6">Sign Up</h2>

        <form onSubmit={handleSignup} className="space-y-4">
          <input
            type="text"
            name="username"
            placeholder="Username"
            value={formData.username}
            onChange={handleChange}
            required
            className="input-style"
          />

          <input
            type="email"
            name="email"
            placeholder="Email"
            value={formData.email}
            onChange={handleChange}
            required
            className="input-style"
          />

          <input
            type="password"
            name="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleChange}
            required
            className="input-style"
          />

          <select
            name="role"
            value={formData.role}
            onChange={handleChange}
            required
            className="input-style"
          >
            <option value="">Select Role</option>
            <option value="student">Student</option>
            <option value="teacher">Teacher</option>
          </select>

          <input
            type="text"
            name="security_code"
            placeholder="Security Code"
            value={formData.security_code}
            onChange={handleChange}
            required
            className="input-style"
          />

          <button
            type="submit"
            className="w-full py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition"
          >
            Sign Up
          </button>
        </form>

        <p className="text-center text-white mt-4">
          Already have an account? <a href="/login" className="text-blue-300 underline">Login here</a>
        </p>
      </div>
    </div>
  );
};

export default Signup;
