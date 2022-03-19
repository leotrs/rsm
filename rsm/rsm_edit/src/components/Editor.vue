<script>
 export default {
     data() {
         return {
             value: "type RSM here"
         }
     },
     methods: {
         make(event) {
             console.log('emitting make event');
             this.$emit('make', this.value);
         }
     }
 }
</script>

<template>
  <div class="editor">
    <textarea id="input" v-model="value"/>
    <button @click="make">Make!</button>
  </div>
</template>

<style scoped>
 .editor {
     height: 100%;
     width: 50%;
 }
 
 #input {
     height: 100%;
     width: 100%;
 }
</style>
