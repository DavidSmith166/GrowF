<template>
<div>
<body>
  <div id="app">
    <svg width="500" height="270">
      <g style="transform: translate(0, 10px)">
        <path :d="line" />
      </g>
    </svg>
  </div>
</body>
</div>
</template>

<script>
import * as d3 from "d3";

export default {
    props: ['result'],
    data() {
        return {
            line: '',
        };
    },
    mounted() {
        this.calculatePath();
    },
    methods: {
        getScales() {
        console.log('getScales')
        const x = d3.scaleTime().range([0, 500]);
        const y = d3.scaleLinear().range([210, 0]);
        d3.axisLeft().scale(x);
        d3.axisBottom().scale(y);
        x.domain(d3.extent( { result }, (d, i) => i));
        y.domain([0, d3.max( { result }, d => d)]);
        return { x, y };
        },
        calculatePath() {
        console.log('calculatePath')
        const scale = this.getScales();
        const path = d3.line()
            .x((d, i) => scale.x(i))
            .y(d => scale.y(d));
        this.line = path({ result });
        },
    },
}
</script>


<style>
svg{
  margin: 25px;
}
path{
  fill: none;
  stroke: #76BF8A;
  stroke-width: 5px;
}
</style>