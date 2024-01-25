<template>
  <section>
    <router-link to="/">
      <div class="inline-flex ml-10 mt-10" @click="goHome">
        <img src="../assets/icons/tabler_square-rounded-arrow-left.png" height="24" width="24" alt=""/>
        <h2 class="text-black text-lg font-bold ml-6">Go Home</h2>
      </div>
    </router-link>

    <div class="scroll divide-y divide-solid ml-10 mt-10 ">
      <div v-for="post in posts" :key="post.id" class="relative pt-5 py-5">
        <div class="mb-20 w-4/6">
          <h5 class="font-semibold mb-2">{{ post.title }}</h5>
          <p>{{ post.body }}</p>
        </div>
        <div @click="openModal(post)" class="absolute bottom-0 right-0 inline-flex mr-10 mt-10 mb-10">
          <h2 class="text-black text-md font-semibold mr-6">See More</h2>
          <img src="../assets/icons/tabler_square-rounded-arrow-right.png" height="24" width="24" alt=""/></div>
      </div>
    </div>

    <!-- Modal -->
    <div v-if="selectedPost" v-show="isModalOpen" class="fixed inset-0 shadow-gray-500 flex items-center justify-center">
      <div class="bg-white p-6 rounded shadow-md">
        <div class="inline-flex mb-5">
          <h2 class="font-bold">{{ selectedPost.title }}</h2>
          <button @click="closeModal" class="text-end top-2 right-2 text-gray-500 hover:text-gray-700">
            <img src="../assets/icons/tabler_square-rounded-x.png" height="24" width="24" alt=""/>
          </button>
        </div>

        <div class="grid grid-cols-2 gap-4">
          <div>
            <p>{{ selectedPost.body }}</p>
          </div>
          <div>
            <h3 class="font-semibold mb-3">Comments</h3>
            <div v-for="comment in comments" :key="comment.id" class="profile-box pb-5">
              <div class="inline-flex">
                <img src="../assets/icons/image%201.png" height="40" width="40" class="mr-3">
                <div class="">
                  <h2 class="text-md text-black font-semibold">{{ comment.name }}</h2>
                  <p class="text-sm text-gray-600">{{ comment.body }}</p>
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
      posts: [],
      comments: [],
      selectedUserId: localStorage.getItem('selectedUserId') || '',
      isModalOpen: false,
      selectedPost: null,
    };
  },
  mounted() {
    this.fetchUserPosts();
  },
  methods: {
    fetchUserPosts() {
      const selectedUserId = localStorage.getItem('selectedUserId') || ''
      const apiUrl = `${API_BASE_URL}/users/${selectedUserId}/posts`;

      axios.get(apiUrl)
          .then(response => {
            this.posts = response.data;
          })
          .catch(error => {
            console.error('Error fetching post list:', error);
          });
    },
    selectUser(user) {
      this.$emit('selectUser', user)
      localStorage.setItem('selectedUserId', user["id"]);
    },
    goHome() {
      localStorage.removeItem('selectedUserId');
      localStorage.setItem('selectedTab', "posts");
      location.reload();
    },
    openModal(post) {
      this.selectedPost = post
      this.isModalOpen = true;

      const apiUrl = `${API_BASE_URL}/users/${this.selectedUserId}/posts/${this.selectedPost.id}`;

      axios.get(apiUrl)
          .then(response => {
            this.comments = response.data;
          })
          .catch(error => {
            console.error('Error comment post list:', error);
          });
    },
    closeModal() {
      this.isModalOpen = false;
    },
  },
};
</script>

<style scoped>
@import '../styles/index.css';
</style>
