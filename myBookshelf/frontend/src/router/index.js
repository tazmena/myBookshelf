import { createRouter, createWebHistory } from "vue-router";

const routes = [
    {
      path: '/',
      name: 'Home',
      component: () => import('../pages/Home.vue')
    },
    {
      path: '/recommendations',
      name: 'Recommendations',
      component: () => import('../pages/Recommendations.vue')
    },
    {
        path: '/search',
        name: 'Search',
        component: () => import('../pages/Search.vue')
    },
    {
      path: '/quiz',
      name: 'Quiz',
      component: () => import('../pages/Quiz.vue'),
    },
  ]

const router = createRouter({
    // history: createWebHistory(process.env.BASE_URL),
    history: createWebHistory(),
    routes
})

export default router