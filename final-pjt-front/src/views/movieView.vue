<template>
  <div style="display: flex; text-align: left;">
    <br>
    <hr style="color:white;">
    <b-container class="bg-dark" fluid style="padding:15px;">
      <br>
      <div style="width:100%;">
        <button class="btn btn-danger" v-for="genre in genrenames" :key="genre.index" style="width:7%; margin:5px;" @click="genremovie(genre)">{{genre}}</button>
      </div>
      <div style="margin-top:20px;">
        <h2 style="color:white; font-family: 'BMHANNAPro'; margin-left:20px;">{{genrename}} 영화</h2>
        <div class="movie_list"  style="width:100%;">
          <NowMovieCard
            v-for="movie in arr"
            :key="movie.id" 
            :movie="movie"
          />
        </div>
      </div>
      <hr style="color:white;">
      <b-col align-self="center" style="margin-top:20px;">
          <h2 style="color:white; font-family: 'BMHANNAPro'; margin-left:20px;">최신영화</h2>
          <div>
            <div class="movie_list" >
              <NowMovieCard
                  v-for="movie in nowmoviesList" :key="movie.pk"
                  :movie="movie"
              />
            </div>
          </div>
      </b-col>
      <hr style="color:white;">
      <div style="width:100%; margin-top:20px;">
        <h2 style="color:white; font-family: 'BMHANNAPro'; margin-left:20px;">영화 목록</h2>
        <div class="movie_list" style="width:100%;"> 
          <NowMovieCard
              v-for="movie in topmoviesList" :key="movie.pk"
              :movie="movie"
          />
        </div>
      </div>
      <p>{{movie}}</p>
    </b-container>
  </div>
</template>

<script>
// import MovieCard from '@/components/MovieCard'
import NowMovieCard from '@/components/NowMovieCard'
export default {
  name: 'MovieView',

  data() {
      return {
          genrename:null,
          movie:null,
          arr:[],
          realgenre:null,
      }
  },
  components: { 
    // MovieCard, 
    NowMovieCard },
  computed: {
      topmoviesList() {
          return this.$store.state.topmoviesList
      },
      nowmoviesList() {
          return this.$store.state.nowmoviesList
      },
      genrenames() {
        
        const genrelist =  {28 : "액션", 16:"애니메이션",
        35:"코미디", 80:"범죄", 18:"드라마",
        10751:"가족", 14:"판타지", 27:"공포",
        10402:"음악",  10749:"로맨스", 878:"SF",
        53:"스릴러", 10752:"전쟁"}
        return genrelist
  
        }
  },
  methods:{
    genremovie(genre){
      this.arr=[]
      this.genrename=genre
      console.log(genre)
      const genre_nums = [28, 16, 35, 80, 99, 18, 10751, 14, 36, 27, 10402, 10749, 878,
      53, 10752]
      for (const genre_num in genre_nums) {
        if (this.genrenames[genre_nums[genre_num]] === genre) {
          this.realgenre=genre_nums[genre_num]
        }
      }
      for(let i=0; i<this.topmoviesList.length; i++){
        for (const num in this.topmoviesList[i].genres){
          if (this.realgenre===this.topmoviesList[i].genres[num]){
            this.arr.push(this.topmoviesList[i])
          }
        }
      }
      console.log(this.arr)
    },
  },
  created(){
    this.genremovie("액션")
  }
}
</script>

<style>
.movie_list {
    display: flex;
    overflow-x: scroll;
    scroll-behavior: smooth;
    height: 450px;;
    overflow-y:hidden;
    white-space: nowrap;
    }
.movie_list::-webkit-scrollbar{
  opacity: 0;
    
}
.movie_list::-webkit-scrollbar-thumb{
    background-color: white;
}
.list{
  /* justify-content: center;
  display: flex;
  justify-content: center;
  align-items: center; */
  display: inline-block;
  padding-left: 20px;
}
</style>
