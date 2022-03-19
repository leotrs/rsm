<script>
 export default {
     props: ['body']
 }
</script>

<template>
  <div class="viewer">
    <div class="manuscritp" v-html="body"></div>
  </div>
</template>

<style scoped>
 .viewer {
     height: 100%;
     width: 50%;
 }
</style>
