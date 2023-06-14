const options = {
	chart: {
  	type: 'column',
    events: {
      load: function () {
        const chart = this
        fetch("/stats/matches-per-year")
        .then((response)=>response.json())
        .then((answer)=>{
            console.log(answer)
            chart.series[0].setData(answer.map((point)=>point.count))
            chart.xAxis[0].setCategories(answer.map((point)=>point.season))
        })
      }
    }
  },
  xAxis: [{
    categories: []
  }],
  series: [{
  	data: []
  }]
}
const chart = Highcharts.chart('container', options);