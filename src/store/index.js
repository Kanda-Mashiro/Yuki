import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import YAML from 'yamljs'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    profile: []
  },
  mutations: {
    updateProfilee(state, payload) {
      state.profile = payload.profile
    }
  },
  actions: {
    async fetchProfile({ commit }) {
      let str = ''
      if (process.env.NODE_ENV === "development") {
        str = await axios.get('http://localhost:8000/Yuki/static/profile.yml')
      } else {
        str = await axios.get('static/profile.yml')
      }

      const profile = YAML.parse(str.data)
      profile.shuffle()

      commit({
        type: 'updateProfilee',
        profile
      })
    }
  }
})
