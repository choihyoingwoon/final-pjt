<template>
  <div id="app">
    <header class="bg-dark">
      <br>
      <h1 style="font-family: 'BMDOHYEON'; color:red">Netflix</h1>
      <div>
        <b-navbar toggleable="lg" type="dark" variant="dark" style="font-family: 'BMDOHYEON'; padding-left:20px; padding-right:20px; ">
      <b-navbar-brand>SSAFY</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" style="justify-content: space-between;" is-nav>
        <b-navbar-nav>
            <b-nav-item href="/">Home</b-nav-item>
            <b-nav-item href="/community" >community</b-nav-item>
            <b-nav-item href="/movies" >Disabled</b-nav-item>
          </b-navbar-nav>
          <b-navbar-nav>
            <b-nav-item v-show="!isLoggedIn" href='/accounts/signup' >Signup</b-nav-item>
            <b-nav-item v-show="!isLoggedIn" href='/accounts/login'>Login</b-nav-item>
            <b-navbar-brand v-show="isLoggedIn">{{me}}님 환영합니다</b-navbar-brand>
            <b-nav-item href="/accounts/mypage" v-show="isLoggedIn">MyPage</b-nav-item>
            <b-nav-item v-show="isLoggedIn" @click="logout" href='#'>Logout</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
      </div>
    </header>

    <router-view @login="changeLog" />
  </div>
</template>

<!-- <script src="https://unpkg.com/vue"></script>
<script src="https://unpkg.com/vue-dragscroll"></script> -->
<script>
// @ is an alias to /src
import axios from 'axios'
import VueJwtDecode from 'vue-jwt-decode'
export default {
  name: 'HomeIndex',
  data: function() {
    return {
      isLoggedIn: false,
      me:null,
    };
  },
  computed:{
    userName() {
          return this.$store.state.user
      },
  },
  methods:{
    getUserInfo() {
      const token = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(token)
      // console.log(info)
      // const user_id = info.user_id
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/mypage/',
        data: {
          info
        },
        headers: {
          Authorization: `Bearer ${token}`
        },
      })
        .then((res) => {
          // console.log(res)
          this.me=res.data.username
        })
        .catch((err) => {
          console.log(err)
        })
    },
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
      })
      .catch(err=>{
        console.log(err)
      })
    },
    changeLog(){
      this.isLoggedIn = true;
    }
  },
  created(){
    this.getUserInfo()
    this.topMovie()
    this.nowMovie()
    const token = localStorage.getItem("jwt");
    if (token) {
      this.isLoggedIn = true;
    }
  }
}
// const app = Vue.createApp(HomeIndex);
//         app.use(VueDragscroll);
//         app.mount('#app')
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
@font-face{
  font-family: 'BMDOHYEON';
  src:url('assets/BMDOHYEON_ttf.ttf')
}
@font-face{
  font-family: 'BMHANNAPro';
  src:url('assets/BMHANNAPro.ttf')
}
@font-face{
  font-family: 'BMJUA';
  src:url('assets/BMJUA_ttf.ttf')
}
@font-face{
  font-family: 'BMHANNAAir';
  src:url('assets/BMHANNAAir_ttf.ttf')
}
header {
  position: sticky;
  top: 0px; /* 도달했을때 고정시킬 위치 */
  padding: 5px;
  background-color: gold;
  z-index: 10;
}
.bodycss{
    height: 100%;
    color: white;
    position: relative;
  }
</style>
