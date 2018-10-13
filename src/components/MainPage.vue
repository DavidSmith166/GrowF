<template>
<div>
  <h1>GrowF</h1>
    <div id = "Graphs">
      <div id = "Marquee">
        <h2>Marquee</h2>
        <table class="table table-hover">
          <tbody>
            <tr>
              <td> 
                <button type="button" class="btn btn-success btn-sm" v-b-modal.loc-weather-modal>Past Month</button>
                <button type="button" class="btn btn-dark btn-sm" v-b-modal.loc-update-modal>Past Quarter</button>
                <button type="button" class="btn btn-outline-danger btn-sm">Past Year</button>
            </tr>
          </tbody>
        </table>
      </div>
      <div id = "Current">
        <h2> Current </h2> 
        <table class="table table-hover">
          <tbody>
            <tr>
              <td> 
                <button type="button" class="btn btn-success btn-sm" v-b-modal.loc-weather-modal>Past Month</button>
                <button type="button" class="btn btn-dark btn-sm" v-b-modal.loc-update-modal>Past Quarter</button>
                <button type="button" class="btn btn-outline-danger btn-sm">Past Year</button>
            </tr>
          </tbody>
        </table>   
      </div>
    </div>
</div>
</template>

<script>
export default{
  data () {
    return {
    }
  }
}
</script>

<style>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
#Graphs{
  display:flex;
}
#Marquee{
  width: 300px;
}
#Current{
  flex: 1;
}
</style>