<template>
  <div class="navbar">
      <ul class="nav-menu">
          <div class="item1">
              <h3>TO-DO Pal</h3>
              <li>
                  <router-link class="nav-item nav-link" to="/">
                      <i class="fas fa-home"></i> Home
                  </router-link>
              </li>
              <li>
                  <router-link class="nav-item nav-link" to="/about">
                      <i class="fas fa-info-circle"></i> About
                  </router-link>
              </li>
              <li>
                  <router-link class="nav-item nav-link" to="/admn">
                      <i class="fas fa-user-shield"></i> Admin
                  </router-link>
              </li>
          </div>
          <div class="item2">
            <form class="nav-search-form">
              <input type="text" placeholder="Search...">
              <button type="submit">Search</button>
          </form>

              <li class="nav-item nav-link logoutClass" v-on:click="logout">
                  <i class="fas fa-sign-out-alt"></i> Logout
              </li>
          </div>
      </ul>
  </div>
</template>

<script setup>
import { pinia } from '../main'; // Import Pinia instance


const logout = () =>{
  console.log("Logging out");
  localStorage.clear();
  window.location.reload();
  pinia.state.value.isLoggedIn = false;
};
</script>


<style scoped>
*{
  margin: 0;
  padding: 0;
  align-items: center;
}
body{
  margin: 0;
  padding: 0;
}

h3{
  color: white;
  margin-right: 30px;
  font-family:Georgia, 'Times New Roman', Times, serif;
  font-size: larger;
}

.navbar {
  background-color: #423ddb;
  padding: 2.5rem;
  top: 0; /* Stick it to the top */
}
.nav-menu {
  list-style: none;
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.nav-item {
  margin-right: 1rem;
  color: white;
  text-decoration: none;
}

.item1 {
  display: flex;
}

.item2 {
  display: flex;
  margin-left: auto;
}

.nav-link {
  color: #fff;
  padding: 0.5rem 1rem;
  transition: background-color 0.3s ease;
}

.nav-link:hover {
  background-color: rgb(135, 137, 255);
}

/* Style for search form */
.nav-search-form {
  display: flex;
}
.nav-search-form input[type="text"] {
  padding: 0.65rem;
  border: 1px solid #ccc;
  border-radius: 0.55rem;
  margin-right: 0.5rem;
  width: 265px;
}

.nav-search-form button {
  padding: 0.5rem 1rem;
  background-color: rgb(7, 215, 7);
  color: #fff;
  border: none;
  border-radius: 0.45rem;
  cursor: pointer;
}

.nav-search-form button:hover {
  background-color: rgb(4, 152, 4);
}

.logoutClass{
  cursor: pointer;
  margin-left: 20px
}

</style>
