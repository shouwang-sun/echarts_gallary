var myChart = echarts.init(document.getElementById('chartDiv'));
window.onresize = myChart.resize;

var channel = 'FCXF-X-03-S03';
var yellowThreshold = 100;
var redThreshold = 150;

option = {
    backgroundColor: '#f5f5f5',
    title: {
        text: channel+' 通道实时监测数据',
        left: 'center',
        top: '3%',
        textStyle: {
            fontSize: 18,
            fontWeight: 'bold',
            fontWeight: 'bold',
            color: 'rgba(18, 89, 147, 1)',
        }
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'line',
            axis: 'x',
            snap: true
        },
        formatter: function(params) {
            return params[0].value[0].toLocaleTimeString() + '<br\>'
            + params[0].value[1]
        }
    },
    visualMap: {
        type: 'piecewise',
        seriesIndex: [0, 1],
        pieces: [
            {gte: redThreshold},
            {gte: yellowThreshold, lt: redThreshold},
            {lt: yellowThreshold}
        ],
        color: ['red', 'orange', 'green'],
        show: false
    },
    toolbox: {
        feature: {
            dataZoom: {show: true},
            restore: {show: true},
            dataView: {show: true},
        }
    },
    dataZoom: {type: 'inside'},
    xAxis: {
        type: 'time',
        splitNumber: 10,
        axisLine: {
            show: true,
            onZero: false,
            lineStyle: {color: 'rgba(18, 89, 147, 1)', width: 2}
        },
        axisTick: {
            show: true,
            lineStyle: {color: 'rgba(18, 89, 147, 1)', width: 1.5}
        },
        axisLabel: {
            margin: 8,
            textStyle: {color: 'rgba(18, 89, 147, 0.8)', fontWeight: 'bold'}
        },
        splitLine: {show: true},
        // 把min与max注释掉，数据更新会变成向左移动的模式
         min: function (value) { return Math.ceil(value.max/30000) * 30000 - 300000 },
         max: function (value) { return Math.ceil(value.max/30000) * 30000 },
    },
    yAxis: {
        type: 'value',
        // scale: 是否脱离0值比例
        scale: true,
        axisLine: {
            show: true,
            onZero: false,
            lineStyle: {color: 'rgba(18, 89, 147, 1)', width: 2}
        },
        axisTick: {
            show: true,
            lineStyle: {color: 'rgba(18, 89, 147, 1)', width: 1.5}
        },
        axisLabel: {
            margin: 8,
            textStyle: {color: 'rgba(18, 89, 147, 0.8)', fontWeight: 'bold'}
        },
        splitLine: {show: true},
        // min: function (value) { return Math.floor(value.min/10) * 10 },
        // max: function (value) { return Math.ceil(value.max/10) * 10 },
    },
    series: [
        {
            name: 'realtimeData',
            type: 'line',
            data: [],
            symbolSize: 6,
            showSymbol: false,
            // hoverAnimation: false,
            animation: false,
            markLine: {
                lineStyle: {
                    normal: {width: 1.5, opacity: 0.8}
                },
                label: {
                    normal: {
                        color: 'auto',
                        fontSize: 13,
                        fontWeight: 'bold',
                        // textBorderColor: 'auto',
                        // textBorderWidth: 2,
                        formatter: function (params) { return params.name }
                    },
                    emphasis: {
                        formatter: function (params) { return params.name + '：' + params.value }
                    }
                },
                data: [
                    {
                        name: '橙色预警阈值',
                        yAxis: yellowThreshold,
                        lineStyle: {
                            normal: { color: 'orange' }
                        }
                    },
                    {
                        name: '红色预警阈值',
                        yAxis: redThreshold,
                        lineStyle: {
                            normal: { color: 'red' }
                        }
                    }
                ]
            },
            markPoint: {
                symbolSize: 25,
                itemStyle: {
                    opacity: 0.8
                },
                label: {
                    normal: {
                        fontSize: 13,
                        fontWeight: 'bold',
                        formatter: function (params) {return params.name + ':' + params.value.toPrecision(5)}
                    }
                },
                data: [
                    {
                        name: '最大值',
                        type: 'max',
                        itemStyle:{
                            normal: { color: 'rgb(194, 53, 49)' }
                        },
                        label: {
                            normal: { position: 'top' }
                        }
                    },
                    {
                        name: '最小值',
                        symbolRotate: '180',
                        type: 'min',
                        itemStyle: {
                            normal: { color: 'rgb(18, 89, 147)' }
                        },
                        label: {
                            normal: { position: 'bottom' }
                        }
                    }
                ]
            }
        },
        {
            name: 'latestData',
            type: 'scatter',
            symbol: 'emptyCircle',
            symbolSize: 6,
            label: {
                normal: {
                    show: true,
                    position: 'right',
                    align: 'left',
                    color: 'auto',
                    fontSize: 13,
                    fontWeight: 'bold',
                    formatter: function (params) {
                        return params.value[0].toLocaleTimeString() + '\n' +
                                params.value[1].toPrecision(5)
                    }
                }
            }
        }
    ]
};
myChart.setOption(option);

var now = $.now();
var timeDelta = 1000;
var value = 80;
var data = [];
var maxDataLength = 300;

function randomData() {
    now = new Date( + now + timeDelta);
    value = value + Math.random() * 20 - 10;
    return {
        // name: now.toString(),
        value: [now, value]
    }
}
setInterval(
    function () {
        data.push(randomData());
        if (data.length > maxDataLength) {data.shift();}
        myChart.setOption({
            series:[
                {data: data},
                {data: [data[data.length-1]]}
            ]
        });
    },
1000);