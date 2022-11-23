<template>
  <div class="signup bg-dark" style="text-align:left; padding-left:50px;">
    <br>
    <div v-if="arr.length ===0" style="text-align:center;">
      <img src="@/assets/noResult.png" alt="" style="margin-top:50px; margin-bottom:20px; filter: invert(100%);">
      <h1 style="font-family: 'BMHANNAPro';">검색 결과가 없습니다. </h1>
    </div>
    <div v-if="arr.length !=0">
      <h1 style="font-family: 'BMHANNAPro';">'{{this.$route.params.searchtext}}'과 관련된 영화</h1>
      <div style="width:100%;" v-if="arr">
            <MovieCard
              v-for="movie in arr"
              :key="movie.id" 
              :movie="movie"
            />
          </div>
    </div>

  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'

export default {
  name:'searchPage',
  components: { 
    MovieCard, 
    // NowMovieCard 
  },
  data:function(){
    return{
      arr:[]
    }
  },
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
    search(){
      this.arr=[]
      console.log(this.$route.params.searchtext)
      console.log(this.topmoviesList)
      for(let i=0; i<this.topmoviesList.length; i++){
          if (this.topmoviesList[i].title.includes(this.$route.params.searchtext)){
            this.arr.push(this.topmoviesList[i])
          }
      }
      console.log(this.arr)
    }
  },
  created(){
    this.search()
  }
}
</script>

<style>
.searchmovie_list {
    white-space: nowrap;

    /* overflow-x: scroll;
  overflow-y: hidden;
  white-space: nowrap;
  user-select: none;
  cursor: pointer;
  transition: all 0.2s;
  transform: scale(0.98);
  will-change: transform; */
    }
</style>