<template>
  <div id="main-layout">
    <main-menu></main-menu>
    <div id="main">
      <view-accounts></view-accounts>
    </div>
  </div>
</template>

<script>
import MainMenu from "./components/MainMenu.vue";
import ViewAccounts from "./components/ViewAccounts.vue";

export default {
  name: "App",
  components: {
    MainMenu,
    ViewAccounts,
  },
};
</script>

<style>
body {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
}

#main-layout {
  display: flex;
  align-items: stretch;
}

#main {
  flex-grow: 1;
  padding: 5px;
}
</style>
