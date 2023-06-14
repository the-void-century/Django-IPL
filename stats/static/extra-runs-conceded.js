const options = {
	chart: {
  	type: 'column',
    events: {
      load: function () {
        const chart = this
        fetch("/stats/extra-runs-conceded")
        .then((response)=>response.json())
        .then((answer)=>{
            chart.series[0].setData(answer.map((point)=>point.Runs))
            chart.xAxis[0].setCategories(answer.map((point)=>point.bowling_team))
            console.log(chart.series)
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