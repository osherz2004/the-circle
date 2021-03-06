import { createRouter, createWebHashHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/waiting-screen',
    name: 'WaitingScreen',
    component: () => import('../views/WaitingScreen.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/winner',
    name: 'Winner',
    component: () => import('../views/Winner.vue'),
  },
  {
    path: '/players',
    name: 'Players',
    component: () => import('../views/Players.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/chat',
    name: 'Chat',
    component: () => import('../views/Chat.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/votes',
    name: 'Votes',
    component: () => import('../views/Votes.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue'),
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue'),
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register.vue'),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const user = localStorage.getItem('user');
  // Check if user is not authenticated
  if (to.meta.requiresAuth && !user) return next({ name: 'Login' });
  // Check if user authenticated and tries to access login and register routes
  else if ((to.name == 'Login' || to.name == 'Register') && user)
    next({ name: from.name });
  // Not authenticated routes
  else next();
});

export default router;
