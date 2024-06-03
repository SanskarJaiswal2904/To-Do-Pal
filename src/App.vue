<template>
  <div id="app">
    <!-- Navbar will be rendered if user is logged in -->
    <!-- <Navbar/> -->

    <!-- Router view for rendering components based on route -->
    <router-view/>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import Navbar from './components/Navbar.vue'; // Import your Navbar component
import { pinia } from './main'; // Import Pinia instance

export default defineComponent({
  name: 'App',
  components: {
    Navbar,
  },
  setup() {
    // Access the isLoggedIn property from the pinia instance
    const isLoggedIn = pinia.state.value.isLoggedIn;

    return {
      isLoggedIn,
    };
  },
});
</script>

<style scoped>
*{
  background: linear-gradient(to right, #ffa088, #fce942);
}

</style>
