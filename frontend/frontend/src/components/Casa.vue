<template>
    <div>
        <table class="table table-striped mt-4">
            <thead>
                <tr>
                    <th scope="col">Nombre de casa medica</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="input in directory.edges" :key="input.id">
                    <td>{{ input.node.casaMedica }}</td>
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
    		this.directory = result.data.data.todosCasas
    	} catch (error) {
    		console.error(error)
    	}
    }
  }
</script>

<style scoped>
</style>
