<template>
    <h3>Contenu renseigné</h3>
    <ul>
        <li>author</li>
        <li>publisher</li>
        <li>book</li>
        <li>bookinstance</li>
    </ul>
    <form v-on:submit.prevent="search">
        <input type="text" v-model="userstr" />
        <button type="submit">Afficher</button>
    </form>
    <p>Liste recherchée : {{ userstr }}</p>
</template>
<script>
export default {
  data() {
    return {
      userstr: "",
      result: "",
    };
  },
  methods: {
    search: function () {
        this.result = "" + this.userstr;
    },
  },
};
</script>
<style></style>