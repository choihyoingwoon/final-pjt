import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    topmoviesList:[],
    nowmoviesList:[],
    movieVideo:[],
    user:null,
    likeList : [],
  },
  getters: {
  },
  mutations: {
    ADD_MOVIE(state, movie) {
      state.likeList.push(movie)
    }
  },
  actions: {
    addMovie(context, movie){
      context.commit('ADD_MOVIE', movie)
    }
  },
  modules: {
  }
})
