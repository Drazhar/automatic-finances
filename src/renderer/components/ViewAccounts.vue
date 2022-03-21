<template>
  <li v-for="(account, index) in accounts" :key="index">
    {{ account.rowid }} {{ account.name }}
  </li>
</template>

<script>
export default {
  name: "ViewAccounts",
  data() {
    return {
      accounts: [],
    };
  },
  created() {
    window.ipc.getAccounts().then((x) => {
      this.accounts = x;
    });
  },
};
</script>

<style></style>
