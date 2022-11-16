<template>
  <div id="app">
    <nav>
      <router-link @click.native="nowMovie" :to="{name:'movies'}">Home</router-link> |
    </nav>
    <router-view/>
  </div>
</template>
<script>
// @ is an alias to /src
import axios from 'axios'
export default {
  name: 'HomeIndex',
  methods:{
    nowMovie:function(){
      axios({
        method:'get',
        url:'http://127.0.0.1:8000/movies/',
      })
      .then(res=>{
        this.$store.state.moviesList = res.data
        console.log(res.data)
      })
      .catch(err=>{
        console.log(err)
      })
    },
  },
  created(){
    this.nowMovie()
    this.$router.push('movies')
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
