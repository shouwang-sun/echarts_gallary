// 初始化图表
var myChart = echarts.init(document.getElementById('chartDiv'));
window.onresize = myChart.resize;

// 数据集
var dimensions = ['name', 'value', 'type', 'realtimeData', 'unit', 'status', 'url'];
var dataset = [
    {
        center: [289, 283],
        source: [
            ['FCXF-X-03-S01', 1, '应变传感器',   null, 'με',  'green', 'http://www.baidu.com/'],
            ['FCXF-X-03-T01', 1, '温度传感器',   null, '℃',  'green', 'http://www.baidu.com/']
        ]
    },
    {
        center: [289, 303],
        source: [
            ['FCXF-X-03-S07', 1, '振弦传感器',   null, 'με',  'green', 'http://www.baidu.com/']
        ]
    },
    {
        center: [289, 323],
        source: [
            ['FCXF-X-03-S02', 1, '应变传感器',   null, 'με',  'green', 'http://www.baidu.com/'],
            ['FCXF-X-03-T02', 1, '温度传感器',   null, '℃',  'green', 'http://www.baidu.com/']
        ]
    },
    {
        center: [289, 343],
        source: [
            ['FCXF-X-03-S08', 1, '振弦传感器',   null, 'με',  'green', 'http://www.baidu.com/']
        ]
    },
    {
        center: [289, 363],
        source: [
            ['FCXF-X-03-S03', 1, '应变传感器',   null, 'με',  'green', 'http://www.baidu.com/'],
            ['FCXF-X-03-T03', 1, '温度传感器',   null, '℃',  'green', 'http://www.baidu.com/']
        ]
    },
    {
        center: [878, 280],
        source: [
            ['FCXF-X-03-S04', 1, '应变传感器',   null, 'με',  'green', 'http://www.baidu.com/'],
            ['FCXF-X-03-T04', 1, '温度传感器',   null, '℃',  'green', 'http://www.baidu.com/']
        ]
    },
    {
        center: [878, 300],
        source: [
            ['FCXF-X-03-S09', 1, '振弦传感器',   null, 'με',  'green', 'http://www.baidu.com/']
        ]
    },
    {
        center: [878, 320],
        source: [
            ['FCXF-X-03-S05', 1, '应变传感器',   null, 'με',  'green', 'http://www.baidu.com/'],
            ['FCXF-X-03-T05', 1, '温度传感器',   null, '℃',  'green', 'http://www.baidu.com/']
        ]
    },
    {
        center: [878, 340],
        source: [
            ['FCXF-X-03-S10', 1, '振弦传感器',   null, 'με',  'green', 'http://www.baidu.com/']
        ]
    },
    {
        center: [878, 360],
        source: [
            ['FCXF-X-03-S06', 1, '应变传感器',   null, 'με',  'green', 'http://www.baidu.com/'],
            ['FCXF-X-03-T06', 1, '温度传感器',   null, '℃',  'green', 'http://www.baidu.com/']
        ]
    },
    {
        center: [319, 387],
        source: [
            ['NLH-X-02-A01', 1, '加速度传感器', null, 'gal', 'green', 'http://www.baidu.com/']
        ]
    },
    {
        center: [844, 387],
        source: [
            ['NLH-X-02-A02', 1, '加速度传感器', null, 'gal', 'green', 'http://www.baidu.com/']
        ]
    }
];

// 富文本标签
var rich = {
    labelName: {
        fontSize: 12,
        fontWeight: 'bold',
        align: 'center',
        padding: [0, 0, 6, 0]
    },
    labelLine: {
        width: '100%',
        height: 0,
        borderColor: 'auto',
        borderWidth: 0.5
    },
    gap: {
        height: 2
    },
    redLabelData: {
        backgroundColor: 'red',
        color: 'white',
        fontSize: 12,
        fontWeight: 'bold',
        align: 'center',
        padding: [3, 3, 3, 3],
        borderRadius: 3
    },
    yellowLabelData: {
        backgroundColor: 'orange',
        color: 'white',
        fontSize: 12,
        fontWeight: 'bold',
        align: 'center',
        padding: [3, 3, 3, 3],
        borderRadius: 3
    },
    greenLabelData: {
        backgroundColor: 'green',
        color: 'white',
        fontSize: 12,
        fontWeight: 'bold',
        align: 'center',
        padding: [3, 3, 3, 3],
        borderRadius: 3
    }
};
function labelFormatter(params) {
    var name = params.data[0];
    var realtimeData = params.data[3];
    var unit = params.data[4];
    var status = params.data[5];
    if (realtimeData) {
        return '{labelName|' + name + '}\n' +
            '{gap|}\n{labelLine|}\n{gap|}\n' +
            '{' + status + 'LabelData|' + realtimeData.toFixed(3) + ' ' + unit + '}';
    }
    else {
        return '{labelName|' + name + '}\n' +
            '{gap|}\n{labelLine|}\n{gap|}\n' +
            '{' + status + 'LabelData|' + '-.---' + ' ' + unit + '}';
    }
}

// 饼图通用设置
var pieOptions = {
    type: 'pie',
    center: [],
    radius: [2, 10],
    stillShowZeroSum: false,
    LegendHoverLink: true,
    itemStyle: {
        borderColor: 'white',
        borderWidth: 1,
        opacity: 0.8
    },
    label: {
        formatter: labelFormatter,
        rich: rich
    },
    emphasis: {
        itemStyle: {
            borderColor: 'rgba(0, 0, 0, 0.8)',
            opacity: 1.0
        }
    },
    dimensions: dimensions,
    datasetIndex: null,
    encode: {
        name: 'name',
        value: 'value',
        itemID: 'name',
        itemName: 'type'
    }
};
// 绘图系列设置
var series = [];
dataset.forEach(function (element) {
    series.push($.extend({}, pieOptions,
        {
            center: element.center,
            datasetIndex: dataset.indexOf(element)
        }
    ));
});
// 图表设置
var option = {
    backgroundColor: 'rgba(255, 255, 255, 0.5)',
    title: {
        text: '阜长线分离式立交主梁截面三数据视图',
        textStyle: {
            color: 'rgba(18, 89, 147, 0.75)',
            fontSize: 18,
            fontWeight: 1000
        }
    },
    dataset: dataset,
    legend: {
        show: true,
        selectedMode: 'multiple',
        orient: 'vertical',
        left: 10,
        bottom: 10
    },
    animation: false
};
$.extend(option, {series: series});
myChart.setOption(option);

// 用户交互设置
var selectedSensor = {};
myChart.on('click', function (params) {
    console.log(params);
    if (params.componentType == 'series' && params.componentSubType == 'pie') {
        if (!$.isEmptyObject(selectedSensor)) {
            myChart.dispatchAction($.extend({type: 'downplay'}, selectedSensor));
        }
    }
    selectedSensor = {
        seriesIndex: params.seriesIndex,
        dataIndex: params.dataIndex
    };
    myChart.dispatchAction($.extend({type: 'highlight'}, selectedSensor));
});

document.onkeydown = function (event) {
    if (event.code == 'Delete' && !$.isEmptyObject(selectedSensor)) {
        dataset[selectedSensor.seriesIndex].source[selectedSensor.dataIndex][1] = null;
        myChart.setOption(option);
        event.preventDefault();
    }
};

myChart.on('dblclick', function (params) {
    if (params.componentType == 'series' && params.componentSubType == 'pie') {
        window.open(dataset[params.seriesIndex].source[params.dataIndex][6], '_blank');
    }
});

var zr = myChart.getZr();
zr.on('contextmenu', function (params) {
    console.log(params);
    params.event.preventDefault();
});

// 数据更新
setInterval(function () {
    for (var i = 0; i < dataset.length; i++) {
        for (var j = 0; j < dataset[i].source.length; j++) {
            var realtimeData = Math.random() * 10;
            var status = '';
            if (realtimeData >= 8) {
                status = 'red';
            }
            else if (realtimeData >= 5) {
                status = 'yellow';
            }
            else {
                status = 'green';
            }
            dataset[i].source[j][3] = realtimeData;
            dataset[i].source[j][5] = status;
        }
    }
    myChart.setOption(option);
    if (!$.isEmptyObject(selectedSensor)){
        myChart.dispatchAction($.extend({type: 'downplay'}, selectedSensor));
        myChart.dispatchAction($.extend({type: 'highlight'}, selectedSensor));
    }
}, 1000);
