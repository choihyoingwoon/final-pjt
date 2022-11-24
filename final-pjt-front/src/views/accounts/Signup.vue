<template>
    <div class="signup" style="background-color:black;">
      <div class="mainsignup" style="font-family:sans-serif;">
        <h1 style="font-family: 'BMDOHYEON';">Signup</h1>
        <hr>
        <div class="box">
          <label for="username" style="font-family: 'BMDOHYEON';">사용자 이름</label>
          <br>
          <input type="text" id="username" v-model="credentials.username" />
        </div>
        <div class="box">
          <label for="password" style="font-family: 'BMDOHYEON';">비밀번호</label>
          <br>
          <input type="password" id="password" v-model="credentials.password" />
        </div>
        <div class="box">
          <label for="passwordConfirmation" style="font-family: 'BMDOHYEON';">비밀번호 확인</label>
          <br>
          <input
            v-model="credentials.passwordConfirm"
            @keyup.enter="signup"
            type="password"
            id="passwordConfirmation"
          />
        </div>
        <div>
          <label for="eamil" style="font-family: 'BMDOHYEON';">이메일</label>
          <br>
          <input type="email" id="eamil" v-model="credentials.email" />
        </div>
        <hr>
        <button class="btn btn-danger"  @click="signup">
          <h4 >회원가입</h4>
        </button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "SignUp",
    data: function() {
      return {
        credentials: {
          username: null,
          password: null,
          passwordConfir: null,
          email: null,
        },
      };
    },
    methods: {
      signup: function() {
        axios({
          method: "post",
          url: "http://127.0.0.1:8000/accounts/signup/",
          data: this.credentials,
        })
          .then(() => {
            alert("회원가입 성공!");
            this.$router.push({ name: "Login" });
          })
          .catch((err) => {
            console.log(err);
          });
      },
    },
  };
  </script>
  <style>
  .signup{
    height: 100vh;
    color: white;
    position: relative;
  }
  .mainsignup{
    line-height: 30px;
    position:absolute;
    top: 40%;
    left: 50%;
    transform: translate( -50%, -50% );
    text-align: left;
    width: 35%;
  }
  input{
    width: 100%;

  }
  .btn{
    width: 100%;
    height: 50px;
    margin-top: 10px;
  }
  .box{
    margin-bottom: 15px;
  }
</style>
  