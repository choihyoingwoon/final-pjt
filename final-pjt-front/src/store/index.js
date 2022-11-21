import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[
    createPersistedState(),
  ],
  state: {
    topmoviesList:[],
    nowmoviesList:[],
    movieVideo:[],
    user:null,
    likeList : [],
    communityDetail:[]
  },
  getters: {
  },
  mutations: {
    ADD_MOVIE(state, movie) {
      if (state.likeList.includes(movie)) {
        state.likeList.splice(0,1)
      } else {
        state.likeList.push(movie)
      }
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
