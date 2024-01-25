<template>
  <div id="app" class="flex">
    <SidebarComponent @selectUser="selectUser" />
    <main class="flex-1 p-8">
      <UserListComponent
          v-if="selectedUser"
          :user="selectedUser"
          @selectTab="selectTab"
      />
      <UserPostsComponent v-if="selectedTab === 'posts'" :userId="selectedUser.id" />
    </main>
  </div>
</template>

<script>
import SidebarComponent from './components/SidebarComponent.vue'
import UserListComponent from './components/UserListComponent.vue'
import UserPostsComponent from './components/UserPostsComponent.vue'

export default {
  data() {
    return {
      // showSidebar: true,
      selectedUser: null,
      selectedTab: '',
    }
  },
  methods: {
    selectUser(user) {
      this.selectedUser = user
      console.log(this.selectedUser.name)
      // this.showSidebar = false
    },
    selectTab(tab) {
      this.selectedTab = tab
      console.log(111111111111111111, this.selectedTab)
    },
  },
  components: {
    SidebarComponent,
    UserListComponent,
    UserPostsComponent,
  },
}
</script>

<style>
@import './styles/index.css';
</style>
