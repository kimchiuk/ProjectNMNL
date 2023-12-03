<template>
  <div>
    <div>
      <nav>
        <div class="nav-top">
          <div class="hearder">
            <RouterLink :to="{ name: 'home' }"
              ><img class="img" src="@/assets/LOGO.png" alt="LOGO_img"
            /></RouterLink>
          </div>
          <div v-if="!store.isLogin">
            <RouterLink class="link-style1" :to="{ name: 'signup' }">
              SIGNUP</RouterLink
            >
            <RouterLink class="link-style1" :to="{ name: 'login' }">
              LOGIN</RouterLink
            >
          </div>
          <div v-else>
            <RouterLink class="link-style1" :to="{ name: 'profile' }">
              PROFILE</RouterLink
            >
            <a class="link-style1" @click="store.logout">LOGOUT</a>
          </div>
        </div>

        <div class="nav-category">
          <RouterLink class="link-style2" :to="{ name: 'products' }">
            PRODUCTS
          </RouterLink>
          <RouterLink class="link-style2" :to="{ name: 'exchange' }">
            EXCHANGE
          </RouterLink>
          <RouterLink class="link-style2" :to="{ name: 'searchbank' }">
            SEARCHBANK
          </RouterLink>
          <RouterLink class="link-style2" :to="{ name: 'reviews' }">
            REVIEWS
          </RouterLink>
        </div>
      </nav>
    </div>
    <RouterView />
  </div>
</template>

<script setup>
import { useCounterStore } from "./stores/counter";

const store = useCounterStore();
</script>

<style scoped>
.img {
  height: 80px;
  width: 150px;
}
.nav-top {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: flex-end;
  padding: 5px 20px;
  height: 100px;
}

.nav-category {
  display: flex;
  justify-content: center;
  background-color: rgb(45, 67, 45);
}
.link-style1 {
  text-decoration: none;
  font-weight: bolder;
  margin: 10px;
  color: darkgrey;
}

.link-style2 {
  text-decoration: none;
  font-weight: bolder;
  margin: 10px;
  color: whitesmoke;
}
</style>
