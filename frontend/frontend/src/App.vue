<template>
  <div id="app">
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
          <div class="collapse navbar-collapse" id="navbarText">
              <ul class="navbar-nav mr-auto">
                  <li class="nav-item active">
                      <a class="nav-link" @click="ingresar1" href="#"> Medicamentos <span class="sr-only">(current)</span></a>
                  </li>
                  <li class="nav-item">
                      <a class="nav-link" @click="ingresar2" href="#"> Casas Medicas </a>
                  </li>
                  <li class="nav-item">
                      <a class="nav-link" @click="ingresar3" href="#"> Proveedores </a>
                  </li>
                  <li class="nav-item">
                      <a class="nav-link" @click="ingresar4" href="#"> Ingresar Casa </a>
                  </li>
                  <li class="nav-item">
                      <a class="nav-link" @click="ingresar5" href="#"> Ingresar Medicamento </a>
                  </li>
              </ul>
          </div>
      </nav>
    <CompanyData v-if="primera"/>
    <Casa v-if="segunda"/>
    <Proveedores v-if="tercera"/>
    <Ingresar v-if="cuarto"/>
    <IngresarM v-if="quinto"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import CompanyData from './components/Comp'
import Casa from './components/Casa'
import Proveedores from './components/Proveedores'
import Ingresar from './components/Ingresar'
import IngresarM from './components/Ingresarm'

export default {
    name: 'App',
    data(){
        return{
            primera:true,
            segunda:false,
            tercera:false,
            cuarto:false,
            quinto:false,
        }
    },
    components: {
        HelloWorld,
        CompanyData,
        Casa,
        Proveedores,
        Ingresar,
        IngresarM
    },
	methods:{
        ingresar1(){
            this.primera=true
            this.segunda=false
            this.tercera=false
            this.cuarto=false
            this.quinto=false
        },
        ingresar2(){
            this.segunda=true
            this.primera=false
            this.tercera=false
            this.cuarto=false
            this.quinto=false
        },
        ingresar3(){
            this.tercera=true
            this.segunda=false
            this.primera=false
            this.cuarto=false
            this.quinto=false
        },
        ingresar4(){
            this.tercera=false
            this.segunda=false
            this.primera=false
            this.cuarto=true
            this.quinto=false
        },
        ingresar5(){
            this.tercera=false
            this.segunda=false
            this.primera=false
            this.cuarto=false
            this.quinto=true
        },
    }

}
</script>

<style>

@import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
#app {
}
</style>
