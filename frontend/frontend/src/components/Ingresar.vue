<template>
    <div>
       <div class="form-group mt-4">
                <label class="form-check-label mr-2 ml-3" for="inlineCheckbox3">Nombre de la nueva casa medica:</label>
                </br>
                <input type="text" class="form-control ml-3 m-2" id="name" placeholder="casa medica" v-model="nombre_casa">
        </div>
        <div class="form-group">
            <button class="btn btn-primary ml-3" @click="ingresar" > Ingresar </button>
        </div>
    </div>
</template>

<script>
  import axios from 'axios'
  export default{
  	name: 'Cuarto',
    data(){
        return{
            nombre_casa:'',
        }
    },
    methods:{
  	    async ingresar()
        {
            try {
                var result = await axios({
                    method: 'POST',
                    url: 'http://127.0.0.1:8000/graphql/',
                    data: {
                        query:`
                            mutation{
                              createCasa(input:{
                                      casaMedica:"${this.nombre_casa}"
                                  })
                                  {
                                      casaMedica{
                                        id
                                        casaMedica
                                      }
                                  }
                            }
                            `
                            }
                        })
                    } catch (error) {
                        console.error(error)
                    }
        }
    },
    mounted () {

    }
  }
</script>

<style scoped>
</style>
