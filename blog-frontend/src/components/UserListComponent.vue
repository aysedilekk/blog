<template>
  <section>
    <div v-if="!selectedUserId" class="ml-10">
      <h1 class="text-xl mt-10" v-if="users.length">All Users</h1>
      <div class="flex flex-wrap justify-center mt-10">
        <div class="grid grid-cols-3 gap-4">
          <div v-for="user in users" :key="user.id" class="p-4 max-w-sm" @click="selectUser(user)">
            <div class="flex rounded-lg h-full bg-white border-2 border-gray p-8 flex-col hover:shadow-indigo-500/40">
              <div class="flex items-center mb-4">
                <div
                    class="w-8 h-8 mr-3 inline-flex items-center justify-center rounded-full dark:bg-indigo-500 bg-indigo-500 text-white flex-shrink-0">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-linecap="round"
                       stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">
                    <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
                  </svg>
                </div>
                <div>
                  <h2 class="text-lg font-medium">{{ user.name }}</h2>
                  <p class="text-md">{{ user.email }}</p>
                  <p>{{ user.phone }}</p>
                </div>
              </div>
              <div class="flex flex-col justify-between flex-grow">
                <div class="mb-3">
                  <h3 class="inline-flex title text-md font-medium">
                    <img class="mr-2" height="24" src="../assets/icons/tabler_map-pin-heart.png" width="24" alt=""/>
                    Location
                  </h3>
                  <p class="text-sm text-gray-900">
                    {{ user.address.city }}
                  </p>
                </div>
                <div class="mb-3">
                  <h3 class="inline-flex title text-md font-medium">
                    <img class="mr-2"  height="24" src="../assets/icons/tabler_building-skyscraper.png" width="24" alt=""/>
                    Company
                  </h3>
                  <p class="text-sm text-gray-900">
                    {{ user.company.name }}
                  </p>
                </div>
                <div class="mb-3">
                  <h3 class="inline-flex title text-md font-medium">
                    <img class="mr-2"  height="24" src="../assets/icons/tabler_world-share.png" width="24" alt=""/>
                    Website
                  </h3>
                  <p class="text-sm text-gray-900">
                    {{ user.website }}
                  </p>
                </div>
              </div>
            </div>
          </div>
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
      users: [],
      selectedUserId: localStorage.getItem('selectedUserId') || '',
    };
  },
  mounted() {
    this.fetchUserList();
  },
  methods: {
    fetchUserList() {
      const apiUrl = `${API_BASE_URL}/users/`;

      axios.get(apiUrl)
          .then(response => {
            this.users = response.data;
          })
          .catch(error => {
            console.error('Error fetching user list:', error);
          });
    },
    selectUser(user) {
      this.$emit('selectUser', user)
      localStorage.setItem('selectedUserId', user["id"]);
      location.reload();
    },
  },
};
</script>

<style scoped>
@import '../styles/index.css';
</style>
