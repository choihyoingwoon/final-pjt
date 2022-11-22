import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

import communityStore from '@/store/modules/communityStore.js'

export default new Vuex.Store({

  modules: {
    communityStore : communityStore,
  },
  plugins:[
    createPersistedState({
          paths: ["communityStore"]
        }),
  ],
})
