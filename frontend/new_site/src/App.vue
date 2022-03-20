<template>
  <header></header>
    <Main/>
    <NotKnow/>
  <footer></footer>
</template>

<script>
import Main from './components/Main.vue'
import NotKnow from './components/NotKnow.vue'
export default {
  name: 'App',
  components: {
    Main,
    NotKnow
  }
}
</script>

<style>

</style>
