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

    <p>Pour récupérer, chercher "fetch(" dans d4l (ou dans la doc node js)</p>
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