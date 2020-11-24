<template>
    <div>
       <div class="form-group mt-4">
                <label class="form-check-label mr-2 ml-3" for="inlineCheckbox3">Nombre del medicamento:</label>
                </br>
                <input type="text" class="form-control ml-3 m-2" id="name" placeholder="Medicamento" v-model="nombre_medicamento">
        </div>
        <label class="form-check-label mr-2 ml-3" for="inlineCheckbox3">Proveedor:</label>
        <select v-model="nombreProveedor">
          <option  v-for="(proveedor,index) in proveedoresD" :key="index">{{ proveedor.node.proveedorNombre }}</option>
        </select>
        </br>
        </br>
        <label class="form-check-label mr-2 ml-3" for="inlineCheckbox3">Casa Medica:</label>
        <select v-model="nombreCasa">
          <option  v-for="(casa,index) in casasD" :key="index">{{ casa.node.casaMedica }}</option>
        </select>
        </br>
        </br>
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
            nombre_medicamento:'',
            proveedoresD:[],
            casasD:[],
            nombreProveedor:null,
            nombreCasa:null,
        }
    },
      watch: {
          nombreProveedor() {
              console.log(this.nombreProveedor)
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
                              createMedicamento(input:{
                                medicamentoNombre:"${this.nombre_medicamento}",
                                medicamentoCasa:"${this.nombreCasa}",
                                medicamentoProveedor:"${this.nombreProveedor}"
                              }
                              )
                              {
                              medicamento
                                {
                                  medicamentoNombre

                                  medicamentoProveedor {
                                    proveedorNombre
                                  }

                                  medicamentoCasa{
                                    casaMedica
                                  }

                              \t}
                              }
                            }
                            `
                            }
                        })
                    } catch (error) {
                        console.error(error)
                    }
        },
        async casas(){
            try {
                var result = await axios({
                method: 'POST',
                url: 'http://127.0.0.1:8000/graphql/',
                data: {
                    query:`
                       {
                        todosCasas{
                              edges {
                                node {
                                        id
                                        casaMedica
                                    }
                                }
                            }
                        }
                        `
                        }
                    })
                    console.log('casasD')
                    this.casasD = result.data.data.todosCasas.edges
                    console.log(this.casasD)
                } catch (error) {
                    console.error(error)
                }
        },
        async proveedores(){
            try {
            var result = await axios({
                method: 'POST',
                url: 'http://127.0.0.1:8000/graphql/',
                data: {
                    query:`
                        {
                            todosProveedores{
                              edges {
                                node {
                                        id
                                        proveedorNombre
                                    }
                                }
                            }
                        }
                        `
                        }
                    })
                    this.proveedoresD = result.data.data.todosProveedores.edges
                    console.log('proveedoresD')
                    console.log(this.proveedoresD)
                } catch (error) {
                    console.error(error)
                }
        }

    },
    mounted () {
        this.casas()
        this.proveedores()
    }
  }
</script>

<style scoped>
</style>
