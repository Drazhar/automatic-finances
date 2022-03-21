<template>
  <div id="card">
    <div class="column-flex">
      <div>Name</div>
      <h1>{{ accountData.name }}</h1>
    </div>
    <div class="row-flex">
      <div class="value" style="background-color: darkblue">Balance</div>
      <div class="value" style="background-color: darkgreen">Trend</div>
    </div>
    <div>03</div>
  </div>
</template>

<script>
export default {
  name: "AccountCard",
  props: {
    accountData: Object,
  },
  created() {
    console.log(this.accountData);
  },
};
</script>

<style scoped>
#card {
  background-color: white;
  padding: 5px;
  margin: 5px;
  border-radius: 5px;
}

.column-flex {
  display: flex;
  flex-direction: column;
}

.row-flex {
  display: flex;
  flex-direction: row;
}

.value {
  color: white;
  margin: 3px;
  padding: 3px;
  border-radius: 3px;
}
</style>
