<template>
  <div id="menu">
    <button>Dashboard</button>
    <button>Transactions</button>
    <button>Accounts</button>
    <button>Categories</button>
    <button>Import</button>
  </div>
</template>

<script>
export default {
  name: "MainMenu",
};
</script>

<style scoped>
#menu {
  display: flex;
  flex-direction: column;
}
</style>
