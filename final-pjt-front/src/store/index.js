import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    topmoviesList:[],
    nowmoviesList:[],
    movieVideo:[],
    user:null,
    // likeList : [],
    communityDetail:null,
  },
  getters: {
  },
  mutations: {
    // ADD_MOVIE(state, movie) {
    //   for(let i = 0; i < state.likeList.length; i++) {
    //       if(state.likeList[i].id === movie.id) {
    //         return
    //       }
    //     }
    //   state.likeList.push(movie)
    // },
    ALL_DELETE(state) {
      state.likeList = []
    }
  },
  actions: {
    // addMovie(context, movie){
    //   context.commit('ADD_MOVIE', movie)
    // },
    alldelete(context) {
      context.commit('ALL_DELETE')
    }
  },
}
)
