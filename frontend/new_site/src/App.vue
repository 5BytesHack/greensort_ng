<template>
  <div class="mmm container-lg p-0 d-flex flex-column col-12">

    <header class="app_header d-flex text-uppercase align-items-center justify-content-center bg-green-278B17">
        <div class="d-flex align-items-baseline">
          <span>с</span>
          <img alt="recycle icon" class="res_img" src="./svg/recycle_icon.svg">
          <span>ртируй!</span>
        </div>
    </header>

    <div class="app_body d-flex flex-column align-items-center">
      <div class="d-flex flex-column col-7 align-items-stretch text-center">
        <span class="text-uppercase c-green-278B17 mt-5">найти точку приема</span>
        <span class="text-uppercase c-green-278B17 mt-1">бытовых отходов</span>
        <button class="btn bg-white c-green-278B17 px-0 text-nowrap py-3 py-md-3 mt-5 border-green-278B17 text-uppercase btn-outline-success">я знаю вид отходов</button>
        <button class="btn bg-white c-green-278B17 px-0 py-1 py-md-1 mt-4 border-green-278B17 text-uppercase btn-outline-success">я хочу узнать<br> вид отходов</button>
      </div>

      <div class="d-flex flex-column col-7 align-items-stretch text-center">
        <span class="text-uppercase c-green-278B17 mt-5">найти вид отходов</span>
        <button class="btn bg-white c-green-278B17 px-0 text-nowrap py-3 py-md-3 mt-5 border-green-278B17 text-uppercase btn-outline-success">по маркировке</button>
        <button class="btn bg-white c-green-278B17 px-0 py-3 mt-4 border-green-278B17 text-uppercase btn-outline-success">по номеру штрихкода</button>
        <button class="btn bg-white c-green-278B17 px-0 py-3 mt-4 border-green-278B17 text-uppercase btn-outline-success">по фото штрихкода</button>
      </div>
    </div>

    <footer class="bg-green-278B17 text-center">
      <p>5 Bytes</p>
    </footer>

  </div>
</template>

<script>
export default {
  name: 'App',
  data(){
    return{

    }
  },
  components: {

  },
  methods: {

  }
}
</script>

<style>
@import'bootstrap/dist/css/bootstrap.min.css';
@font-face {
  font-family: Roboto;
  src:url('./fonts/Roboto-Regular.ttf');
  font-weight: normal;
  font-style: normal;
}

.mmm{
  font-family: Roboto;
  height: inherit;
}
.app_body{
  height: 100%;
  background: url('./img/bg_map.png') 0 0 /cover no-repeat;
}

.app_body span{
  font-size: 1.1875rem;
}

.app_body button{
  font-size: 0.9375rem;
}

.res_img{
  width: 1.56rem;
}

.app_header{
  height: 15.3vh;
  font-size: 2.5rem;
  color: white;
}

.app_body button:hover{
  background-color: #278B17 !important;
  color: white !important;
}

.mmm footer p{
  color: white;
}

.bg-green-278B17{
  background-color: #278B17;
}

.c-green-278B17{
  color: #278B17;
}

.border-green-278B17{
  border-color: #278B17;
}
</style>
