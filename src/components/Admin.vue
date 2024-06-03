<template>
  <Navbar/>
    <div class="page-container">
      <div class="admin-panel">
        <div v-if="loading" class="loading">Loading...</div>
        <div v-else>
          <h1>Users</h1>
          <ul>
            <li v-for="user in users" :key="user.id" class="user-card">
            <strong>{{ user.name }}</strong> --  ({{ user.email }}) 
              <button class="delete-btn" @click="deleteUser(user.id)">Delete User</button>
              <button class="primary-btn" @click="toggleUserTasks(user.id)">
                {{ expandedUser === user.id ? 'Hide Tasks' : 'View Tasks' }}
              </button>
              <div v-if="expandedUser === user.id" class="tasks">
                <h3>Tasks for {{ user.name }}</h3>
                <ul>
                  <li v-for="task in user.tasks" :key="task.id" class="task-item">
                    <span :class="{ completed: task.completed }">{{ task.title }}</span>
                    <button class="delete-btn" @click="deleteTask(user.id, task.id)">Delete Task</button>
                    <button class="primary-btn" @click="toggleTaskCompletion(user.id, task.id)">
                      Mark as {{ task.completed ? 'Pending' : 'Completed' }}
                    </button>
                  </li>
                </ul>
                <form @submit.prevent="addTask(user.id)">
                  <input type="text" v-model="newTaskTitle" placeholder="New Task Title" required />
                  <button class="primary-btn" type="submit">Add Task</button>
                </form>
              </div>
            </li>
          </ul>
        </div>
      </div>
      <div class="footer-container">
        <Footer />
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import Footer from './Footer.vue';
  import Navbar from './Navbar.vue'; // Import your Navbar component

  
  export default {
    name: 'AdminPanel',
    components: {
      Footer,
      Navbar
    },
    setup() {
      const users = ref([]);
      const loading = ref(true);
      const expandedUser = ref(null);
      const newTaskTitle = ref('');
  
      const fetchUsers = () => {
        // Mock data
        users.value = [
          {
            id: 1,
            name: 'John Doe',
            email: 'john@example.com',
            tasks: [
              { id: 1, title: 'Task 1', completed: false },
              { id: 2, title: 'Task 2', completed: true },
            ],
          },
          {
            id: 2,
            name: 'Jane Smith',
            email: 'jane@example.com',
            tasks: [
              { id: 3, title: 'Task 3', completed: false },
              { id: 4, title: 'Task 4', completed: false },
            ],
          },
        ];
        loading.value = false;
      };
  
      const deleteUser = (userId) => {
        users.value = users.value.filter(user => user.id !== userId);
      };
  
      const toggleUserTasks = (userId) => {
        expandedUser.value = expandedUser.value === userId ? null : userId;
      };
  
      const deleteTask = (userId, taskId) => {
        const user = users.value.find(user => user.id === userId);
        if (user) {
          user.tasks = user.tasks.filter(task => task.id !== taskId);
        }
      };
  
      const toggleTaskCompletion = (userId, taskId) => {
        const user = users.value.find(user => user.id === userId);
        if (user) {
          const task = user.tasks.find(task => task.id === taskId);
          if (task) {
            task.completed = !task.completed;
          }
        }
      };
  
      const addTask = (userId) => {
        const user = users.value.find(user => user.id === userId);
        if (user && newTaskTitle.value.trim()) {
          user.tasks.push({
            id: new Date().getTime(), // Mock ID
            title: newTaskTitle.value.trim(),
            completed: false,
          });
          newTaskTitle.value = '';
        }
      };
  
      onMounted(() => {
        fetchUsers();
      });
  
      return {
        users,
        loading,
        expandedUser,
        newTaskTitle,
        deleteUser,
        toggleUserTasks,
        deleteTask,
        toggleTaskCompletion,
        addTask,
      };
    },
  };
  </script>
  
  <style scoped>
  .page-container {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }
  
  .footer-container {
    margin-top: auto;
    width: 100%;
  }
  
  /* General button styles */
  button {
    padding: 0.5rem 1rem;
    border-radius: 0.25rem;
    cursor: pointer;
    font-size: 1.1rem;
    margin-left: 0.5rem;
    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s;
  }
  
  /* Primary Button Styles */
  button.primary-btn {
    background-color: white;
    color: #007bff;
    border: 1px solid #007bff;
  }
  
  button.primary-btn:hover {
    background-color: #0056b3;
    border-color: #0056b3;
    color: white;
    box-shadow: 0 0 10px rgba(0, 91, 187, 0.3);
  }
  
  /* Delete Button Styles */
  button.delete-btn {
    background-color: white;
    color: red;
    border: 1px solid #dc3545;
  }
  
  button.delete-btn:hover {
    background-color: #dc3545;
    border-color: #c82333;
    color: white;
    box-shadow: 0 0 10px rgba(200, 35, 51, 0.3);
  }
  
  /* Disabled Button Styles */
  button:disabled {
    background-color: #6c757d;
    color: #fff;
    border: 1px solid #6c757d;
    cursor: not-allowed;
    opacity: 0.65;
  }
  
  /* Admin Panel Styles */
  .admin-panel {
    padding: 2rem;
  }
  
  .loading {
    font-size: 1.5rem;
    text-align: center;
  }
  
  .user-card {
    border: 1px solid #ccc;
    padding: 1rem;
    margin-bottom: 1rem;
    border-radius: 0.5rem;
    background-color:white;
    width: 1100px;
    list-style-type: none;
  }
  
  .tasks {
    margin-top: 1rem;
    padding: 1rem;
    border-top: 1px solid #ddd;
  }
  
  .task-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.5rem;
    list-style-type: none;
  }
  
  .task-item .completed {
    text-decoration: line-through;
  }
  
  /* Form Styles */
  form {
    display: flex;
    margin-top: 1rem;
  }
  
  form input {
    flex: 1;
    padding: 0.5rem;
    margin-right: 0.5rem;
  }
  
  form button {
    padding: 0.5rem 1rem;
  }
  </style>
  