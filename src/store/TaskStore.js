import { defineStore } from 'pinia';

export const useTaskStore = defineStore('user-info', {
  state: () => ({
    isLoggedIn: false,
  }),
  getters:{
    checkLogin(){
      return this.isLoggedIn;
    }
  },
  actions: {
    logIn() {
      this.isLoggedIn = true;
    },
    logOut() {
      this.isLoggedIn = false;
    },
  },
});

// global state .js