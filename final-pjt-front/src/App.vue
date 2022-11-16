<template>
  <div id="app">
    <div>
  <b-navbar fixed="top" toggleable="lg" type="dark" variant="dark" style="padding-left:20px; padding-right:20px; ">
    <b-navbar-brand>NavBar</b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" style="justify-content: space-between;" is-nav>
      <b-navbar-nav>
          <b-nav-item href="/movies">Home</b-nav-item>
          <b-nav-item href="#" >Disabled</b-nav-item>
          <b-nav-item href="#" >Disabled</b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav>
          <b-nav-item href="#" >Signup</b-nav-item>
          <b-nav-item href="#" >Login</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>

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
