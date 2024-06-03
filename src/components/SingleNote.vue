<template>
    <div class="table-container">
        <div class="flexitems">
            <h2>Notes</h2>
            <button class="action-btn bigClass">
                <i class="fas fa-trash-alt"></i>  Delete All
              </button>  
        </div>
      <table class="custom-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Description</th>
            <th>Date Created</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in items" :key="item.id">
            <td>{{ item.id }}</td>
            <td>{{ item.title }}</td>
            <td>{{ item.description }}</td>
            <td>{{ item.datecreated }}</td>
            <td>
                <button class="action-btn delete-btn"><i class="fas fa-trash-alt"></i> Delete</button>
                <button class="action-btn update-btn"><i class="fas fa-pencil-alt"></i> Update</button>
                
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      items: {
        type: Array,
        required: true
      }
    }
  };
  </script>
  
  <style scoped>
  .bigClass{
    background-color: rgb(255, 210, 210);
    color: red;
    border: 1px solid red;
    width: 300px;
    height: 45px;
    margin-right: 8px; 
    border-radius: 8px;
  }
  .bigClass:hover{
    background-color: red;
    color: white;
    border: 1px solid red;
  }
  .flexitems{
    display: flex;
    justify-content:space-between;
    align-items: center;
  }
  .table-container {
    width: 90vw;
    margin: 0 auto;
  }
  
  .custom-table {
    width: 100%;
    border-collapse: collapse;
    border-spacing: 0;
  }
  
  .custom-table th, .custom-table td {
    border: 1px solid #ddd;
    padding: 12px;
    text-align: left;
    word-wrap: break-word; /* Add this line to allow long words to wrap */
  }
  
  
  .custom-table th {
    background-color: #ef7d03;
    color: #333;
    font-weight: bold;
  }
  
  .custom-table tr {
    background-color: #ffbd76;
  }
  
  .custom-table tr:hover {
    background-color: #c6c4c4;
  }

  
  .action-btn {
    border: none;
    padding: 8px 16px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    margin: 10px;
  }
  
  .delete-btn {
    background-color: #ff5757;
    color: #fff;
    margin-right: 8px; /* Add margin-right for spacing */
    border-radius: 8px; /* Rounded corners */

  }
  
  .delete-btn:hover {
    background-color: #f03737;
  }
  
  .update-btn {
    background-color: #4caf50;
    color: #fff;
    border-radius: 8px; /* Rounded corners */
  }
  
  .update-btn:hover {
    background-color: #43a047;
  }
  </style>
  