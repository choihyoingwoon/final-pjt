<template>
    <div class="signup" style="background-color:black;">
      <div class="mainsignup" style="font-family:sans-serif;">
        <h1 style="font-family: 'BMDOHYEON';">Login</h1>
        <hr>
        <div class="box">
          <label for="username" style="font-family: 'BMDOHYEON';">사용자 이름</label>
          <br>
          <input type="text" id="username" v-model="credentials.username" />
        </div>
        <div class="box">
          <label for="password" style="font-family: 'BMDOHYEON';">비밀번호</label>
          <br>
          <input
            type="password"
            id="password"
            v-model="credentials.password"
            @keyup.enter="login"
          />
        </div>
        <hr>
        <button class="btn btn-danger" @click="login" style="font-family: 'BMDOHYEON';">로그인</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "LogIn",
    data: function() {
      return {
        credentials: {
          username: null,
          password: null,
        },
      };
    },
    methods: {
      login: function() {
        axios({
          method: "post",
          url: "http://127.0.0.1:8000/api/token/",
          data: this.credentials,
        })
          .then((res) => {
            this.$store.state.user=this.credentials.username
            localStorage.setItem("jwt", res.data.access);
            this.$emit("login");
            this.$router.push({ name: "movies" });
            this.$router.go()
          })
          .catch((err) => {
            if (err.message==="Request failed with status code 400"){
              alert("사용자 이름이나 비밀번호를 입력하세요!!!")
            }else{
              alert("사용자 이름이나 비밀번호를 정확하게 입력하세요!!!")
            }
          });
      },
    },
  };
  </script>
  