// router.js

import { createRouter, createWebHistory }  from 'vue-router';
import UserListComponent from '../components/UserListComponent.vue';
import UserPostsComponent from '../components/UserPostsComponent.vue';
import UserTodosComponent from '../components/UserTodosComponent.vue';
import UserAlbumsComponent from '../components/UserAlbumsComponent.vue';


const routes = [
    { path: '/users', component: UserListComponent },
    { path: '/posts', component: UserPostsComponent },
    { path: '/todos', component: UserTodosComponent },
    { path: '/albums', component: UserAlbumsComponent },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
