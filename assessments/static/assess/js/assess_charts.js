$(document).ready(function(){

    var assessChart = echarts.init($('#assess_chart')[0]);

    var option = {
        tooltip: {},
        legend: {
            data: ['Current', 'Target'],
            bottom: 0,
        },
        radar: {
            shape: 'circle',
            name: {
                textStyle: {
                    color: '#fff',
                    backgroundColor: '#999',
                    borderRadius: 3,
                    padding: [3, 5]
               }
            },
            indicator: sectionList,
        },
        series: [{
            name: 'Assessment data',
            type: 'radar',
            // areaStyle: {normal: {}},
            data : [
                {
                    value : currentScores,
                    name : 'Current',
                    itemStyle: {
                        color: '#007bff',
                    },
                    lineStyle: {
                        color: '#007bff',
                    }
                },
                {
                    value : targetScores,
                    name : 'Target',
                    itemStyle: {
                        color: '#a200ff',
                    },
                    lineStyle: {
                        color: '#a200ff',
                    }
                }
            ]
        }]
    };

    assessChart.setOption(option);

    $(window).on('resize', function(){
        if(assessChart != null && assessChart != undefined){
            assessChart.resize();
        }
    });
});


