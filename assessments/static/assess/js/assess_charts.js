$(document).ready(function(){

    var assessChart = echarts.init($('#assess_chart')[0]);

    var option = {
        color: '#007bff',
        legend: {
            data: ['Current', 'Target'],
            bottom: 0,
            left: 0,
        },
        radar: {
            shape: 'circle',
            name: {
                textStyle: {
                    color: '#fff',
                    backgroundColor: '#007bff',
                    borderRadius: 3,
                    padding: [3, 5]
                }
            },
            indicator: sectionList,
            splitArea: {
                areaStyle: {
                    color: [
                        'rgba(0, 123, 255, 0.1)',
                        'rgba(0, 123, 255, 0.15)',
                        'rgba(0, 123, 255, 0.2)',
                        'rgba(0, 123, 255, 0.25)',
                        'rgba(0, 123, 255, 0.3)'
                    ]
                }
            },
            axisLine: {
                lineStyle: {
                    color: 'rgba(255, 255, 255, 0.6)'
                }
            },
            splitLine: {
                lineStyle: {
                    color: 'rgba(255, 255, 255, 0.6)'
                }
            },
            splitNumber: 5
        },
        series: [{
            name: 'Assessment data',
            type: 'radar',
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
        }],


        tooltip: {},
    };

    assessChart.setOption(option);

    $(window).on('resize', function(){
        if(assessChart != null && assessChart != undefined){
            assessChart.resize();
        }
    });
});


