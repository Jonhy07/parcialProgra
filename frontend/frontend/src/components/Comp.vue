<template>
    <div>
        <table class="table table-striped mt-4">
            <thead>
                <tr>
                    <th scope="col">Medicamento</th>
                    <th scope="col">Casa Medica</th>
                    <th scope="col">Proveedor</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="input in directory.edges" :key="input.id">
                    <td>{{ input.node.medicamentoNombre }}</td>
                    <td>{{ input.node.medicamentoCasa.casaMedica }}</td>
                    <td>{{ input.node.medicamentoProveedor.proveedorNombre }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
  import axios from 'axios'
  export default{
  	name: 'CompanyData',
    data(){
      return {
      	directory: []
      }
    },
    async mounted () {
    	try {
	var result = await axios({
		method: 'POST',
		url: 'http://127.0.0.1:8000/graphql/',
		data: {
			query:`{
                    todosMedicamentos {
                      edges {
                        node {
                                id
                                medicamentoNombre
                                medicamentoCasa
                                {
                                casaMedica
                                }
                                medicamentoProveedor {
                                    proveedorNombre
                                }
                            }
                        }
                    }
                }`
    			}
    		})
    		this.directory = result.data.data.todosMedicamentos
    	} catch (error) {
    		console.error(error)
    	}
    }
  }
</script>

<style scoped>
</style>
