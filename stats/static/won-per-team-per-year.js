let series_data=[]
let category=[]
var options;
function getData(){
    return new Promise((resolve,reject)=>{
        fetch("/stats/won-per-year-per-team")
        .then((response)=>response.json())
        .then((answer)=>{
            let i=0
            let mapped=answer.reduce((season,currentSeason)=>{
                console.log("Utsav")
                if(season[currentSeason.season]==undefined){
                    season[currentSeason.season] = i
                    i+=1
                }
                return season
            },{})
            console.log(mapped)
            let finalAnswer=answer.reduce((season,currentSeason)=>{
                if(season[currentSeason.winner]==undefined){
                    season[currentSeason.winner] = new Array(Object.keys(mapped).length).fill(0);
                    season[currentSeason.winner][mapped[currentSeason.season]]=currentSeason.win_count;
                }
                else{
                    season[currentSeason.winner][mapped[currentSeason.season]]=currentSeason.win_count;
                }
                return season;
            },{})
            //console.log(finalAnswer)
            console.log(finalAnswer);
            category=Object.keys(mapped)
            console.log(Object.keys(mapped))
            for(keys in finalAnswer){
                series_data.push({name:keys,data:finalAnswer[keys]})
            }
            console.log(category);
            options = {
                chart: {
                  type: 'column',
                  title:'Series'
              },
              xAxis: [{
                categories: category
              }],
              series: series_data
            }
            resolve()
        })
        .catch((error)=>{console.error(error.message);
        reject(error);
    })
    })
}

getData().then(()=>{
    Highcharts.chart('container', options);
})

