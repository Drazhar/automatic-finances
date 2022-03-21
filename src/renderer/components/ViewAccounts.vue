<template>
  <div id="account_cards_container">
    <account-card
      v-for="account in accounts"
      :key="account.id"
      :accountData="account"
    ></account-card>
  </div>
</template>

<script>
import AccountCard from "./AccountCard.vue";

export default {
  name: "ViewAccounts",
  components: {
    AccountCard,
  },
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

<style scoped>
#account_cards_container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
</style>
