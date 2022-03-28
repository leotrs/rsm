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

             fetch('http://localhost:8001/make', {
	         method: 'PUT',
	         headers:{'Content-Type':'application/json'},
	         body: JSON.stringify({
                     src: this.value
                 })
             }).then(response => {
                 return response.json()
             }).then(data => {
                 this.$emit('make', data.output);
             });
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
