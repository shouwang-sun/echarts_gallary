// 初始化图表
let myChart = echarts.init(document.getElementById('chartDiv'));
window.onresize = myChart.resize;

// 数据集
let view = {
	name: 'FCXF-X-03',
	image_url: 'image/FCXF-X-03.png',
	subset: [
		{
			center: [289, 363],
			subset: ['FCXF-X-03-S03', 'FCXF-X-03-T03']
		},
		{
			center: [289, 343],
			subset: ['FCXF-X-03-S08', 'FCXF-X-03-T08']
		},
		{
			center: [289, 323],
			subset: ['FCXF-X-03-S02', 'FCXF-X-03-T02']
		},
		{
			center: [289, 303],
			subset: ['FCXF-X-03-S07', 'FCXF-X-03-T07']
		},
		{
			center: [289, 283],
			subset: ['FCXF-X-03-S01', 'FCXF-X-03-T01']
		},
		{
			center: [878, 360],
			subset: ['FCXF-X-03-S06', 'FCXF-X-03-T06']
		},
		{
			center: [878, 340],
			subset: [ 'FCXF-X-03-S10', 'FCXF-X-03-T10' ]
		},
		{
			center: [878, 320],
			subset: [ 'FCXF-X-03-S05', 'FCXF-X-03-T05' ]
		},
		{
			center: [878, 300],
			subset: ['FCXF-X-03-S09', 'FCXF-X-03-T09']
		},
		{
			center: [878, 280],
			subset: ['FCXF-X-03-S04', 'FCXF-X-03-T04']
		},
		{
			center: [319, 387],
			subset: ['FCXF-X-03-A01']
		},
		{
			center: [844, 387],
			subset: ['FCXF-X-03-A02']
		}
	]
};
let basicInfo = {
	'FCXF-X-03-S01': {name: 'FCXF-X-03-S01', type: '应变传感器', unit: 'με', url: ''},
	'FCXF-X-03-T01': {name: 'FCXF-X-03-T01', type: '温度传感器', unit: '℃', url: ''},
	'FCXF-X-03-S02': {name: 'FCXF-X-03-S02', type: '应变传感器', unit: 'με', url: ''},
	'FCXF-X-03-T02': {name: 'FCXF-X-03-T02', type: '温度传感器', unit: '℃', url: ''},
	'FCXF-X-03-S03': {name: 'FCXF-X-03-S03', type: '应变传感器', unit: 'με', url: ''},
	'FCXF-X-03-T03': {name: 'FCXF-X-03-T03', type: '温度传感器', unit: '℃', url: ''},
	'FCXF-X-03-S04': {name: 'FCXF-X-03-S04', type: '应变传感器', unit: 'με', url: ''},
	'FCXF-X-03-T04': {name: 'FCXF-X-03-T04', type: '温度传感器', unit: '℃', url: ''},
	'FCXF-X-03-S05': {name: 'FCXF-X-03-S05', type: '应变传感器', unit: 'με', url: ''},
	'FCXF-X-03-T05': {name: 'FCXF-X-03-T05', type: '温度传感器', unit: '℃', url: ''},
	'FCXF-X-03-S06': {name: 'FCXF-X-03-S06', type: '应变传感器', unit: 'με', url: ''},
	'FCXF-X-03-T06': {name: 'FCXF-X-03-T06', type: '温度传感器', unit: '℃', url: ''},
	'FCXF-X-03-A01': {name: 'FCXF-X-03-A01', type: '加速度传感器', unit: 'gal', url: ''},
	'FCXF-X-03-A02': {name: 'FCXF-X-03-A02', type: '加速度传感器', unit: 'gal', url: ''},
	'FCXF-X-03-S07': {name: 'FCXF-X-03-S07', type: '振弦应变传感器', unit: 'με', url: ''},
	'FCXF-X-03-T07': {name: 'FCXF-X-03-T07', type: '振弦温度传感器', unit: '℃', url: ''},
	'FCXF-X-03-S08': {name: 'FCXF-X-03-S08', type: '振弦应变传感器', unit: 'με', url: ''},
	'FCXF-X-03-T08': {name: 'FCXF-X-03-T08', type: '振弦温度传感器', unit: '℃', url: ''},
	'FCXF-X-03-S09': {name: 'FCXF-X-03-S09', type: '振弦应变传感器', unit: 'με', url: ''},
	'FCXF-X-03-T09': {name: 'FCXF-X-03-T09', type: '振弦温度传感器', unit: '℃', url: ''},
	'FCXF-X-03-S10': {name: 'FCXF-X-03-S10', type: '振弦应变传感器', unit: 'με', url: ''},
	'FCXF-X-03-T10': {name: 'FCXF-X-03-T10', type: '振弦温度传感器', unit: '℃', url: ''}
};
let warningThreshold = {
	'FCXF-X-03-S01': [-8, -5, 5, 8],
	'FCXF-X-03-T01': [-8, -5, 5, 8],
	'FCXF-X-03-S02': [-8, -5, 5, 8],
	'FCXF-X-03-T02': [-8, -5, 5, 8],
	'FCXF-X-03-S03': [-8, -5, 5, 8],
	'FCXF-X-03-T03': [-8, -5, 5, 8],
	'FCXF-X-03-S04': [-8, -5, 5, 8],
	'FCXF-X-03-T04': [-8, -5, 5, 8],
	'FCXF-X-03-S05': [-8, -5, 5, 8],
	'FCXF-X-03-T05': [-8, -5, 5, 8],
	'FCXF-X-03-S06': [-8, -5, 5, 8],
	'FCXF-X-03-T06': [-8, -5, 5, 8],
	'FCXF-X-03-A01': [-8, -5, 5, 8],
	'FCXF-X-03-A02': [-8, -5, 5, 8],
	'FCXF-X-03-S07': [-8, -5, 5, 8],
	'FCXF-X-03-T07': [-8, -5, 5, 8],
	'FCXF-X-03-S08': [-8, -5, 5, 8],
	'FCXF-X-03-T08': [-8, -5, 5, 8],
	'FCXF-X-03-S09': [-8, -5, 5, 8],
	'FCXF-X-03-T09': [-8, -5, 5, 8],
	'FCXF-X-03-S10': [-8, -5, 5, 8],
	'FCXF-X-03-T10': [-8, -5, 5, 8]
};
let realtimeData = {
	'FCXF-X-03-S01': 0,
	'FCXF-X-03-T01': 0,
	'FCXF-X-03-S02': 0,
	'FCXF-X-03-T02': 0,
	'FCXF-X-03-S03': 0,
	'FCXF-X-03-T03': 0,
	'FCXF-X-03-S04': 0,
	'FCXF-X-03-T04': 0,
	'FCXF-X-03-S05': 0,
	'FCXF-X-03-T05': 0,
	'FCXF-X-03-S06': 0,
	'FCXF-X-03-T06': 0,
	'FCXF-X-03-A01': 0,
	'FCXF-X-03-A02': 0,
	'FCXF-X-03-S07': 0,
	'FCXF-X-03-T07': 0,
	'FCXF-X-03-S08': 0,
	'FCXF-X-03-T08': 0,
	'FCXF-X-03-S09': 0,
	'FCXF-X-03-T09': 0,
	'FCXF-X-03-S10': 0,
	'FCXF-X-03-T10': 0
};

// 生成绘图数据集
let data = $.extend({}, basicInfo);
for (let sensor in data) {
	data[sensor].activated = 1;
}
updatingData = getWarningStatus(realtimeData, warningThreshold);
$.extend(true, data, updatingData);

let center = [];
let dataset = [];
view.subset.forEach(function (element) {
	center.push(element.center);
	let source = [];
	element.subset.forEach(function (sensor) {
		source.push(data[sensor]);
	})
	dataset.push({source});
})

// 图表设置
let option = {
	backgroundColor: 'rgba(255, 255, 255, 0.5)',
	title: {
		text: '阜长线分离式立交主梁截面三数据视图',
		textStyle: {
			color: 'rgba(18, 89, 147, 0.75)',
			fontSize: 18,
			fontWeight: 'bold'
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
	animation: false,
	series: []
};

// 绘图系列设置
for (let i=0; i<center.length; i++) {
	let pieChart = {
		type: 'pie',
		radius: [0, 9],
		stillShowZeroSum: false,
		LegendHoverLink: true,
		itemStyle: {
			opacity: 0.5
		},
		label: {show: false},
		emphasis: {
			itemStyle: {
				opacity: 1.0
			},
			label: {
				show: true,
				backgroundColor: 'rgba(255, 255, 255, 0.8)',
				formatter(params) {
					let name = params.data.name;
					let value = params.data.value;
					let unit = params.data.unit;
					let status = params.data.status;
					if (value) {
						value = value.toFixed(3);
					} else {
						value = '-.---';
					}
					return `{labelName|${name}}\n{gap|}\n{labelLine|}\n{gap|}\n{${status}LabelData|${value} ${unit}}`;
				},
				rich: {
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
				}
			},
		},
		encode: {
			name: 'name',
			value: 'activated',
			itemID: 'name',
			itemName: 'type'
		}
	};
	// update serie's center and datasetIndex
	pieChart.center = center[i];
	pieChart.datasetIndex = i;
	option.series.push(pieChart);
}
myChart.setOption(option);

// 用户交互设置
let selectedSensors = new Set();
for ( sensor in basicInfo ) {
	selectedSensors.add(sensor);
}
let currentSensor = new String();

let callbacks = {
	click(params) {
		if ( params.componentType == 'series' && params.componentSubType == 'pie' ) {
			currentSensor = params.data.name;
			if ( selectedSensors.has(currentSensor) ) {
				selectedSensors.delete(currentSensor);
				currentSensor = '';
			}
			else {
				selectedSensors.add(currentSensor)
			}
		}
	},
	dblclick(params) {
		if (params.componentType == 'series' && params.componentSubType == 'pie') {
			window.open(params.data.url, '_blank');
		}
	}
};
for(let event in callbacks) {
	myChart.on(event, callbacks[event]);
}

document.onkeydown = function (event) {
	if ( event.code == 'Delete' && currentSensor != '' ) {
		data[currentSensor].activated = null; // 若data的某一项的activated值为null，那么它不会在绘图中显示出来。
	}
	event.preventDefault();
};

// 数据更新
setInterval(function () {
	for (let sensor in realtimeData) {
		realtimeData[sensor] = Math.random() * 10;
	}
	updatingData = getWarningStatus(realtimeData, warningThreshold);
	$.extend(true, data, updatingData);
	myChart.setOption(option);
	for ( let i=0; i<dataset.length; i++ ) {
		for ( let j=0; j<dataset[i].source.length; j++ ) {
			if ( selectedSensors.has(dataset[i].source[j].name) ) {
				myChart.dispatchAction({
					type: 'downplay',
					seriesIndex: i,
					dataIndex: j
				});
				myChart.dispatchAction({
					type: 'highlight',
					seriesIndex: i,
					dataIndex: j
				});
			}
		}
	}
}, 1000);

function getWarningStatus(realtimeData, warningThreshold) {
	let updatingData = {};
	for ( sensor in realtimeData ) {
		let value = realtimeData[sensor];
		let threshold = warningThreshold[sensor];
		let status = null;
		if ( value <= threshold[0] ) {
			status = 'red';
		}
		else if ( value > threshold[0] && value <= threshold[1] ) {
			status = 'yellow';
		}
		else if ( value > threshold[1] && value < threshold[2] ) {
			status = 'green';
		}
		else if ( value >= threshold[2] && value < threshold[3] ) {
			status = 'yellow';
		}
		else if ( value >= threshold[3] ) {
			status = 'red';
		}
		else {
			console.log('invalid warning thresholds');
		}
		updatingData[sensor] = {value, status}
	}
	return updatingData;
}

/* vim:set ts=4 sw=4 sts=4: */
