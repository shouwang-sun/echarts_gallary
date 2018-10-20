// 初始化图表
let myChart = echarts.init(document.getElementById('chartDiv'));
window.onresize = myChart.resize;

// 数据集
$.ajaxSettings.async = false;
let viewData = {};
$.getJSON('data/bridgeSunburst.json', function (ret) {viewData = ret} );
$.ajaxSettings.async = true;
console.log(viewData);

let seriesOption = {
    type: 'sunburst',
    radius: [0, 21],
    levels: [
        {// level0
            r0: 0,
            r: 6,
            itemStyle: {
                color: 'rgba(255, 255, 255, 0.6)',
                borderWidth: 0.5,
                borderColor: 'rgba(0, 0, 0, 1)'
            }
        },
        {// level1
            r0: 6,
            r: 15,
            itemStyle: {
                borderWidth: 0.5,
                borderColor: 'rgba(0, 0, 0, 1)'
            },
            label: {
                show: false
            }
        },
        {// level2
            r0: 15,
            r: 21,
            itemStyle: {
                borderWidth: 0.5,
                borderColor: 'rgba(0, 0, 0, 1)'
            },
            label: {
                show: true,
                position: 'outside',
                distance: 20,
                align: 'left',
                textBorderWidth: 3
            }
        }
    ]
};

let series = [];
for (let i=0; i<viewData.length; i++) {
    series.push($.extend({}, seriesOption, {
        id: viewData[i].name,
        center: viewData[i].center,
        data: viewData[i].children
    }));
}
console.log(series);

// 图表设置
let option = {
    backgroundColor: 'rgba(255, 255, 255, 0.6)',
    title: {
        text: '阜长线分离式立交数据视图',
        textStyle: {
            color: 'rgba(18, 89, 147, 0.75)',
            fontSize: 18,
            fontWeight: 'bold'
        }
    },
    animation: true,
    series: series
};
myChart.setOption(option);

/* vim:set ts=4 sw=4 sts=4: */
