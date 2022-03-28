<script>
 import Editor from './components/Editor.vue'
 import Viewer from './components/Viewer.vue'

 export default {
     data() {
         return {
             body: ""
         }
     },
     methods: {
         display(value) {
             this.body = value;
         }
     },
     components: {
         Viewer, Editor
     }
 }
</script>

<template>
  <div class="body">
    <Editor :value="body" @make="display"/>
    <Viewer :body="body" />
  </div>
</template>

<style>
 @import './assets/base.css';

 #app {
     max-width: 1280px;
     margin: 0 auto;
     padding: 2rem;
     font-weight: normal;
     height: 100%;
     width: 100%;
     position: absolute;
 }

 .body {
     display: flex;
     gap: 3%;
     width: 100%;
     height: 100%;
 }
</style>
