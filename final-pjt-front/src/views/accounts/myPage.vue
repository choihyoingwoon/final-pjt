<template>
    <div class="signup" style="background-color:black;">
      <br>
      <h1 style="color:white; font-family: 'BMHANNAPro';">My Page</h1>
      <br>
      <hr style="width: 100;">
      <br>
      <div>
          <h3 style="margin-left:0px; font-family: 'BMHANNAPro';">{{me}}님이 담아놓은 영화들🎬</h3>
          <div>
              <MovieCard
                  v-for="movie in likelist" :key="movie.id"
                  :movie="movie"
              />
          </div>
      </div>
      <br>
  
    </div>
  </template>
  
  <script>
  import MovieCard from '@/components/MovieCard.vue';
  import axios from 'axios'
  import VueJwtDecode from 'vue-jwt-decode'

  export default {
      name: "myPage",
      data() {
        return {
            me:null,
            likelist: [],
            userdata: [],
        }
      },
      components: {
          MovieCard,
      },  
      computed: {
          userName() {
              return this.$store.state.user
          }
      },
      methods: {
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
          getMyMovie() {
            const token = localStorage.getItem('jwt')
            const info = VueJwtDecode.decode(token)
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
                    this.userdata = res.data
                    const mymovies = this.userdata.like_movies
                    axios({
                        method: 'post',
                        url: `http://127.0.0.1:8000/movies/${info.user_id}/likelist/`,
                        data: {
                            'mymovies' : mymovies,
                        },
                        headers: {
                            Authorization: `Bearer ${token}`
                        },

                    })
                        .then((res)=> {
                            this.likelist = res.data
                        })
                        .catch((err) => {
                            console.log(err)
                        })
              
                })
                .catch((err) => {
                    console.log(err)
                })
                },
      },
      created() {
        this.getMyMovie()
        this.getUserInfo()
      }
  }
  </script>
  
  <style>
  
  </style>