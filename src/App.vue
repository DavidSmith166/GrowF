<template>
  <div id="app">
    <h1>GrowF</h1>
    <div id = "Graphs">
      <div id = "Marquee">
        <h2>Marquee</h2>
        <table class="table table-hover">
          <tbody>
            <tr>
            <td>
                <button type="button" class="btn btn-success btn-sm">Past Month</button>
                <button type="button" class="btn btn-dark btn-sm" >Past Quarter</button>
                <button type="button" class="btn btn-outline-danger btn-sm">Past Year</button>
            </td>
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
                <button type="button" class="btn btn-success btn-sm">Past Month</button>
                <button type="button" class="btn btn-dark btn-sm">Past Quarter</button>
                <button type="button" class="btn btn-outline-danger btn-sm">Past Year</button>
            </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <portfolio></portfolio>
  </div>
</template>

<script>  
import Portfolio from './components/Portfolio';

export default{
  name: 'App',
  data () {
    return {
    }
  },
  components: {
    portfolio : Portfolio,
  }
};
</script>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
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
    width: 650px;
}
#Current{
    flex: 1;
}
</style>