<script>
 export default {
     props: ['body']
 }
</script>

<template>
  <div class="viewer">
    <div class="manuscript">
      <iframe id="frame" src="http://localhost:8001/view">
      </iframe>
    </div>
  </div>
</template>

<style scoped>
 .viewer {
     height: 100%;
     width: 50%;
 }

 .manuscript {
     height: 100%;
     width: 100%;
 }

 #frame {
     height: 100%;
     width: 100%;
 }
</style>
