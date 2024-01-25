<template>
  <section>
    <router-link v-if="!selectedAlbum" to="/">
      <div class="inline-flex ml-10 mt-10" @click="goHome">
        <img alt="" height="24" src="../assets/icons/tabler_square-rounded-arrow-left.png" width="24"/>
        <h2 class="text-black text-lg font-bold ml-6">Go Home</h2>
      </div>
    </router-link>

    <router-link v-if="selectedAlbum" to="/">
      <div class="inline-flex ml-10 mt-10" @click="goAlbums">
        <img alt="" height="24" src="../assets/icons/tabler_square-rounded-arrow-left.png" width="24"/>
        <h2 class="text-black text-lg font-bold ml-6">Go Albums</h2>
      </div>
    </router-link>

    <div v-if="!selectedAlbum" class="grid grid-cols-3 gap-4">
      <div v-for="album in albums" :key="album.id">
        <div class="border border-b-gray-800 grid grid-cols-2 p-3 m-3" @click="selectAlbum(album)">
          <div v-for="photo in album.photos.slice(0, 4)" :key="photo.id">
            <img :src=photo.thumbnailUrl alt="" class="border border-b-gray-200" height="200" width="200"/>
          </div>
        </div>
        <h2 class="text-black text-lg">{{ album.title }}</h2>
      </div>
    </div>

    <div v-if="selectedAlbum">
      <div v-for="photo in selectedAlbum.photos.slice(0, 4)" :key="photo.id" class="inline-flex mt-5 ml-5">
        <img :src=photo.url alt="" class="border border-b-gray-200 mr-3"/>
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
      albums: [],
      selectedUserId: localStorage.getItem('selectedUserId') || '',
      selectedAlbum: null,
    };
  },
  mounted() {
    this.fetchUserAlbums();
  },
  methods: {
    fetchUserAlbums() {
      const selectedUserId = localStorage.getItem('selectedUserId') || ''
      const apiUrl = `${API_BASE_URL}/users/${selectedUserId}/albums`;

      axios.get(apiUrl)
          .then(response => {
            for (let album of response.data) {
              const apiUrl = `${API_BASE_URL}/users/${selectedUserId}/albums/${album.id}`;
              axios.get(apiUrl)
                  .then(response => {
                    album = {album, "photos": response.data}
                    this.albums.push(album)
                  })
                  .catch(error => {
                    console.error('Error fetching photo list:', error);
                  });
            }
          })
          .catch(error => {
            console.error('Error fetching album list:', error);
          });


    },
    selectUser(user) {
      this.$emit('selectUser', user)
      localStorage.setItem('selectedUserId', user["id"]);
    },
    selectAlbum(album) {
      this.selectedAlbum = album
    },
    goHome() {
      localStorage.removeItem('selectedUserId');
      localStorage.setItem('selectedTab', "users");
      location.reload();
    },
    goAlbums() {
      location.reload();
      this.selectedAlbum = null
    }
  },
};
</script>

<style scoped>
@import '../styles/index.css';
</style>
