<template>
    <div class="not-found-container">
      <h1>403 - Forbidden</h1>
      <p>Sorry, you don't have permission to access this page.</p>
      <router-link to="/" class="home-link">Go to Homepage</router-link>
    </div>
  </template>
  
  
  <script>
  export default {
    name: 'NotAdmin',
  };
  </script>
  
  <style scoped>
  .not-found-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    text-align: center;
    background-color: #f8f8f8;
    color: #333;
  }
  
  .not-found-container h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
  }
  
  .not-found-container p {
    font-size: 1.5rem;
    margin-bottom: 2rem;
  }
  
  .home-link {
    background-color: white;
    font-size: 1.2rem;
    color: #007bff;
    text-decoration: none;
    border: 1px solid #007bff;
    padding: 0.5rem 1rem;
    border-radius: 5px;
    transition: background-color 0.3s, color 0.3s;
  }
  
  .home-link:hover {
    background-color: #007bff;
    color: #fff;
  }
  </style>
  