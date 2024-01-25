<template>
  <div id="sidebar">
    <!--  user detail-->
    <div v-if="user" class="profile-box px-5 pb-5">
      <div class="inline-flex">
        <img class="mr-3" height="40" src="../assets/icons/image%201.png" width="40">
        <div class="">
          <h2 class="text-md text-black font-semibold">{{ user.name }}</h2>
          <p class="text-sm text-gray-600 underline underline-offset-1">{{ user.email }}</p>
        </div>
      </div>
    </div>

    <div v-if="user" class="profile-box-border mb-5"></div>

    <ul>
      <li v-if="!user" @click="selectTab('users')">
        <router-link to="/users">
          <div class="inline-flex text-black"><img alt="" class="mr-2" height="24"
                                                   src="../assets/icons/tabler_users.png" width="24"/>Users
          </div>
        </router-link>
      </li>
      <li v-if="user" @click="selectTab('todos')">
        <router-link to="/todos">
          <div class="inline-flex text-black"><img alt="" class="mr-2" height="24"
                                                   src="../assets/icons/tabler_checkup-list.png" width="24"/>Todos
          </div>
        </router-link>
      </li>
      <li v-if="user" @click="selectTab('posts')">
        <router-link to="/posts">
          <div class="inline-flex text-black"><img alt="" class="mr-2" height="24"
                                                   src="../assets/icons/tabler_notebook.png" width="24"/>Posts
          </div>
        </router-link>
      </li>
      <li v-if="user" @click="selectTab('albums')">
        <router-link to="/albums">
          <div class="inline-flex text-black"><img alt="" class="mr-2" height="24"
                                                   src="../assets/icons/tabler_photo-heart.png" width="24"/>Albums
          </div>
        </router-link>
      </li>
    </ul>

    <div class="sidebar-footer px-5 pb-5">
      <div class="inline-flex content-center ml-10">
        <img alt="" class="mr-3" height="40" src="../assets/icons/image%201.png" width="40">
        <h2 class="text-md text-gray-800 font-bold mt-2">N2MOBIL</h2>
      </div>
    </div>

  </div>


  <div id="content w-100">
    <router-view></router-view>
  </div>
</template>

<script>
import axios from 'axios';
import {API_BASE_URL} from "../../config";

axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.xsrfCookieName = 'csrftoken';
export default {
  data() {
    return {
      user: null,
      users: [],
      selectedUserId: localStorage.getItem('selectedUserId') || '',
    }
  },
  mounted() {
    this.fetchUserDetails();
  },
  methods: {
    selectTab(tab) {
      localStorage.setItem('selectedTab', tab);
    },

    fetchUserDetails() {
      const selectedUserId = localStorage.getItem('selectedUserId') || ''
      if (selectedUserId !== '') {
        const apiUrl = `${API_BASE_URL}/users/${selectedUserId}/`;

        axios.get(apiUrl)
            .then(response => {
              this.user = response.data;
            })
            .catch(error => {
              console.error('Error fetching user details:', error);
            });
      }

      return selectedUserId
    }
  },
}
</script>

<style scoped>
@import '../styles/index.css';
</style>

