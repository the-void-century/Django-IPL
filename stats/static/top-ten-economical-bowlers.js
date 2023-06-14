const options = {
	chart: {
  	type: 'column',
    events: {
      load: function () {
        const chart = this
        fetch("/stats/top-ten-economical-bowlers")
        .then((response)=>response.json())
        .then((answer)=>{
            console.log(answer)
            chart.series[0].setData(answer.map((point)=>point.economy))
            chart.xAxis[0].setCategories(answer.map((point)=>point.bowler))
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