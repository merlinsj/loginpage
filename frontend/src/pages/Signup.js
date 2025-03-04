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

  const navigate = useNavigate(); // Initialize navigate for programmatic redirection

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
        navigate('/login'); // Redirect to login page
      } else {
        alert(data.error || 'Signup failed');
      }
    } catch (error) {
      console.error('Signup error:', error);
    }
  };

  return (
    <div>
      <h2>Signup</h2>
      <form onSubmit={handleSignup}>
        <label>Username:</label>
        <input type="text" name="username" value={formData.username} onChange={handleChange} required />

        <label>Email:</label>
        <input type="email" name="email" value={formData.email} onChange={handleChange} required />

        <label>Password:</label>
        <input type="password" name="password" value={formData.password} onChange={handleChange} required />

        <label>Role:</label>
        <select name="role" value={formData.role} onChange={handleChange} required>
          <option value="">Select Role</option>
          <option value="student">Student</option>
          <option value="teacher">Teacher</option>
        </select>

        <label>Security Code:</label>
        <input type="text" name="security_code" value={formData.security_code} onChange={handleChange} required />

        <button type="submit">Signup</button>
      </form>
    </div>
  );
};

export default Signup;
