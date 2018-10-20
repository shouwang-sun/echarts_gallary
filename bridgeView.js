// 初始化图表
let myChart = echarts.init(document.getElementById('chartDiv'));
window.onresize = myChart.resize;

// 加载数据集
$.ajaxSettings.async = false;
let data = null;
$.getJSON('data/sensorBasicInfo.json', function (ret) {data = new sensorData(ret)});
let view = {};
$.getJSON('data/bridgeView.json', function (ret) {view = ret} );
$.ajaxSettings.async = true;

let center = [];
let dataset = [];
view.forEach(function (group) {
	let source = [];
	group.sensors.forEach(function (sensor) {
		source.push(data.plotData[sensor]);
	});
	dataset.push({source});
    center.push(group.center);
});

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
	dataset: dataset,
	legend: {
		show: true,
		selectedMode: 'single',
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
		avoidLabelOverlap: true,
		startAngle: 90,
		itemStyle: {
			opacity: 0.5,
			borderColor: 'rgb(255, 255, 255)',
			borderWidth: 1
		},
		label: {
			show: false
		},
		labelLine: {
		    length: 30,
		 	length2: 10
		 },
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
			}
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
for (let sensor in data.plotData) {
	selectedSensors.add(sensor);
}
let currentSensor = new String();

// 单击双击事件设置
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

// 在视图中删除当前选中传感器
document.onkeydown = function (event) {
	if ( event.code == 'Delete' && currentSensor != '' ) {
		data[currentSensor].activated = null; // 若data的某一项的activated值为null，那么它不会在绘图中显示出来。
	}
	event.preventDefault();
};

// 数据更新
setInterval(function () {
    realtimeData = {};
	for (let sensor in data.plotData) {
		realtimeData[sensor] = Math.random() * 10;
	}

	data.update(realtimeData);

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

function sensorData(basicInfo) {
	this.plotData = {};
	this.threshold = {};
	for (sensor in basicInfo) {
		let name = basicInfo[sensor].name;
		let type = basicInfo[sensor].type;
		let unit = basicInfo[sensor].unit;
		let threshold = basicInfo[sensor].threshold;
		let activated = 1;
		let value = null;
		let status = null;
		
		this.plotData[sensor] = {name, type, unit, activated, value, status};
		this.threshold[sensor] = threshold;
	}
	
	this.update = function (realtimeData) {
		for (sensor in this.plotData) {
			let value = realtimeData[sensor];
			let threshold = this.threshold[sensor];
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
            this.plotData[sensor].value = value;
            this.plotData[sensor].status = status;
		}
    }
}

/* vim:set ts=4 sw=4 sts=4: */
