<template>
  <section>
    <router-link to="/">
      <div class="inline-flex ml-10 mt-10" @click="goHome">
        <img src="../assets/icons/tabler_square-rounded-arrow-left.png" height="24" width="24" alt=""/>
        <h2 class="text-black text-lg font-bold ml-6">Go Home</h2>
      </div>
    </router-link>

    <div class="ml-10 mt-10 ">
      <div v-for="todo in todos" :key="todo.id" class="pt-3">
        <div class="inline-flex mb-2">
          <input @click="checkTodo(todo.id, false)" v-if="todo.completed" class="mr-3" type="checkbox" checked>
          <input @click="checkTodo(todo.id, true)" v-if="!todo.completed" class="mr-3" type="checkbox">
          <p>{{ todo.title }}</p>
        </div>
      </div>
    </div>
  </section>

</template>

<script>
import axios from 'axios';
import {API_BASE_URL} from "../../config";

axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.xsrfCookieName = 'csrftoken';
export default {
  data() {
    return {
      todo: null,
      todos: [],
      selectedUserId: localStorage.getItem('selectedUserId') || '',
    };
  },
  mounted() {
    this.fetchUserTodos();
  },
  methods: {
    fetchUserTodos() {
      const selectedUserId = localStorage.getItem('selectedUserId') || ''
      const apiUrl = `${API_BASE_URL}/users/${selectedUserId}/todos`;

      axios.get(apiUrl)
          .then(response => {
            this.todos = response.data;
          })
          .catch(error => {
            console.error('Error fetching todo list:', error);
          });
    },
    selectUser(user) {
      this.$emit('selectUser', user)
      localStorage.setItem('selectedUserId', user["id"]);
    },
    goHome() {
      localStorage.removeItem('selectedUserId');
      localStorage.setItem('selectedTab', "users");
      location.reload();
    },
    checkTodo(todoId, value) {
      const data = {"completed": value}
      const selectedUserId = localStorage.getItem('selectedUserId') || ''
      const apiUrl = `${API_BASE_URL}/users/${selectedUserId}/todos/${todoId}`;

      axios.patch(apiUrl, data)
          .then(response => {
            this.todo = response.data;
          })
          .catch(error => {
            console.error('Error fetching todo list:', error);
          });
      this.fetchUserList()
    }
  },
};
</script>

<style scoped>
@import '../styles/index.css';
</style>
