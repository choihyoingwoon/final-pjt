<template>
  <div id="app" >
    <div>
  <b-navbar fixed="top" toggleable="lg" type="dark" variant="dark" style="padding-left:20px; padding-right:20px; ">
    <b-navbar-brand @click="find()">NavBar</b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" style="justify-content: space-between;" is-nav>
      <b-navbar-nav>
          <b-nav-item href="/movies">Home</b-nav-item>
          <b-nav-item href="/movies" >Disabled</b-nav-item>
          <b-nav-item href="/movies" >Disabled</b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav>
          <b-nav-item v-show="!isLoggedIn" href='/accounts/signup' >Signup</b-nav-item>
          <b-nav-item v-show="!isLoggedIn" href='/accounts/login'>Login</b-nav-item>
          <b-nav-item v-show="isLoggedIn" @click="logout" href='#'>Logout</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>

    <router-view @login="changeLog" />
  </div>
</template>
<script>
// @ is an alias to /src
import axios from 'axios'
export default {
  name: 'HomeIndex',
  data: function() {
    return {
      isLoggedIn: false,
    };
  },

  methods:{
    logout() {
      this.isLoggedIn = false;
      localStorage.removeItem("jwt");
      this.$router.push({ name: "Login" });
    },

    topMovie:function(){
      axios({
        method:'get',
        url:'http://127.0.0.1:8000/movies/top_movies/',
      })
      .then(res=>{
        this.$store.state.topmoviesList = res.data
      })
      .catch(err=>{
        console.log(err)
      })
    },
    nowMovie:function(){
      axios({
        method:'get',
        url:'http://127.0.0.1:8000/movies/now_movies/',
      })
      .then(res=>{
        this.$store.state.nowmoviesList = res.data
        console.log(res)
      })
      .catch(err=>{
        console.log(err)
      })
    },
    find(){
      console.log(this.isLoggedIn)
      const token = localStorage.getItem("jwt");
      console.log(token)
    },
    changeLog(){
      this.isLoggedIn = true;
      console.log(this.isLoggedIn)
    }
  },
  created(){
    this.topMovie()
    this.nowMovie()
    const token = localStorage.getItem("jwt");
    if (token) {
      this.isLoggedIn = true;
      this.$router.push({ name: "movies" });
    }
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
.hidden{
  display: none;
}
.active{
  display: '';
}
</style>
