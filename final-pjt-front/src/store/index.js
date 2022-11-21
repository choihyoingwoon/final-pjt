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
    communityDetail:[],
  },
  getters: {
  },
  mutations: {
    ADD_MOVIE(state, movie) {
      for(let i = 0; i < state.likeList.length; i++) {
          if(state.likeList[i].id === movie.id) {
            return
          }
        }
      state.likeList.push(movie)
    },
    ALL_DELETE(state) {
      state.likeList = []
    }
  },
  actions: {
    addMovie(context, movie){
      context.commit('ADD_MOVIE', movie)
    },
    alldelete(context) {
      context.commit('ALL_DELETE')
    }
  },
  modules: {
  }
})
