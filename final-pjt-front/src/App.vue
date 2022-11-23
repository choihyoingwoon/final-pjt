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
            <b-nav-item href="/myMvti" >MVTI✨</b-nav-item>
          </b-navbar-nav>
          <form @submit.prevent="searchmovie()" class="search-bar" style="display:flex;">
            <input placeholder="찾고 싶은 영화 제목을 입력하세용" @keyup.enter="searchmovie(searchtext)" type="search" name="search" v-model.trim="searchtext" pattern=".*\S.*" required >
            <button class="search-btn" type="submit" @click="searchmovie(searchtext)">
              <span>Search</span>
            </button>
          </form>
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
    <router-view :key="$route.fullPath" @login="changeLog"/>
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
      searchtext:null,
    };
  },
  computed:{
    userName() {
          return this.$store.state.user
      },
  },
  methods:{
    searchmovie(searchtext){
      console.log(searchtext)
      this.$router.push({name:"searchPage",params:{searchtext}})
    },
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
        console.log(res.data)
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
    this.topMovie()
    this.nowMovie()
    this.getUserInfo()
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

  .search-bar input,
.search-btn, 
.search-btn:before, 
.search-btn:after {
	transition: all 0.25s ease-out;
}
.search-bar input,
.search-btn {
	width: 3em;
	height: 3em;
}
.search-bar input:invalid:not(:focus),
.search-btn {
	cursor: pointer;
}
.search-bar,
.search-bar input:focus,
.search-bar input:valid  {
	width: 100%;
}
.search-bar input:focus,
.search-bar input:not(:focus) + .search-btn:focus {
	outline: transparent;
}
.search-bar {
	margin: auto;
	/* padding: 1.5em; */
	justify-content: center;
	max-width: 30em;
}
.search-bar input {
	background: transparent;
	border-radius: 1.5em;
    box-shadow: 0 0 0 0.4em #fff inset;
	padding: 0.75em;
	transform: translate(0.5em,0.5em) scale(0.5);
	transform-origin: 100% 0;
	-webkit-appearance: none;
	-moz-appearance: none;
	appearance: none;
}
.search-bar input::-webkit-search-decoration {
	-webkit-appearance: none;
}
.search-bar input:focus,
.search-bar input:valid {
	background: #fff;
	border-radius: 0.375em 0 0 0.375em;
	box-shadow: 0 0 0 0.1em #d9d9d9 inset;
	transform: scale(1);
}
.search-btn {
	background: #fff;
	border-radius: 0 0.75em 0.75em 0 / 0 1.5em 1.5em 0;
	padding: 0.75em;
	position: relative;
	transform: translate(0.25em,0.25em) rotate(45deg) scale(0.25,0.125);
	transform-origin: 0 50%;
}
.search-btn:before, 
.search-btn:after {
	content: "";
	display: block;
	opacity: 0;
	position: absolute;
}
.search-btn:before {
	border-radius: 50%;
	box-shadow: 0 0 0 0.2em #f1f1f1 inset;
	top: 0.75em;
	left: 0.75em;
	width: 1.2em;
	height: 1.2em;
}
.search-btn:after {
	background: #f1f1f1;
	border-radius: 0 0.25em 0.25em 0;
	top: 51%;
	left: 51%;
	width: 0.75em;
	height: 0.25em;
	transform: translate(0.2em,0) rotate(45deg);
	transform-origin: 0 50%;
}
.search-btn span {
	display: inline-block;
	overflow: hidden;
	width: 1px;
	height: 1px;
}

/* Active state */
.search-bar input:focus + .search-btn,
.search-bar input:valid + .search-btn {
	background: rgb(220, 53, 69);
	border-radius: 0 0.375em 0.375em 0;
	transform: scale(1);
}
.search-bar input:focus + .search-btn:before, 
.search-bar input:focus + .search-btn:after,
.search-bar input:valid + .search-btn:before, 
.search-bar input:valid + .search-btn:after {
	opacity: 1;
}
.search-bar input:focus + .search-btn:hover,
.search-bar input:valid + .search-btn:hover,
.search-bar input:valid:not(:focus) + .search-btn:focus {
	background: rgb(187,45,59);
}
.search-bar input:focus + .search-btn:active,
.search-bar input:valid + .search-btn:active {
	transform: translateY(1px);
}

@media screen and (prefers-color-scheme: dark) {
	body, input {
		color: #f1f1f1;
	}
	body {
		background: #171717;
	}
	.search-bar input {
		box-shadow: 0 0 0 0.4em #f1f1f1 inset;
	}
	.search-bar input:focus,
	.search-bar input:valid {
		background: #fff;
		box-shadow: 0 0 0 0.1em #3d3d3d inset;
	}
	.search-btn {
		background: #f1f1f1;
	}
}
</style>
