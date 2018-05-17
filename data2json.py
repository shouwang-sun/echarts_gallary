# -*- coding: utf-8 -*-
__author__ = 'SUNShouwang'

import json

baofu_highway = [
    {
        'name'               : '圣水村大桥',
        'location'           : [114.093296,38.882953],
        'conditionAssessment': 80,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '道有沟大桥',
        'location'           : [114.084194,38.884639],
        'conditionAssessment': 75,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '龙堂沟大桥',
        'location'           : [114.079911, 38.884806],
        'conditionAssessment': 91,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '黄土岭1号大桥',
        'location'           : [114.075912,38.885676],
        'conditionAssessment': 80,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '黄土岭2号大桥',
        'location'           : [114.067277,38.883691],
        'conditionAssessment': 72,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '阜长线分离式立交',
        'location'           : [114.052989,38.881409],
        'conditionAssessment': 90,
        'realtimeWarning'    : [2, 2],
        'url'                : ''
    },
    {
        'name'               : '不老树大桥',
        'location'           : [114.043609,38.885155],
        'conditionAssessment': 85,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '北流河大桥',
        'location'           : [114.035213,38.890308],
        'conditionAssessment': 80,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '走道河大桥',
        'location'           : [114.028652,38.893247],
        'conditionAssessment': 90,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '菜地沟大桥',
        'location'           : [114.022469,38.894419],
        'conditionAssessment': 90,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '头道沟大桥',
        'location'           : [114.018135,38.895399],
        'conditionAssessment': 75,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '石湖沟大桥',
        'location'           : [114.016065,38.895997],
        'conditionAssessment': 90,
        'realtimeWarning'    : [],
        'url'                : ''
    }
]

xinglin_highway = [
    {
        'name'               : '分离式立交一',
        'location'           : [114.672845, 37.006556],
        'conditionAssessment': 91,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '护城河中桥',
        'location'           : [114.687977, 37.002045],
        'conditionAssessment': 85,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '分离立交二',
        'location'           : [114.696336, 37.000594],
        'conditionAssessment': 85,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '溜子河大桥',
        'location'           : [114.70553, 36.999333],
        'conditionAssessment': 72,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '分离立交三',
        'location'           : [114.707695, 36.999037],
        'conditionAssessment': 85,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '南澧河大桥',
        'location'           : [114.724448, 36.993363],
        'conditionAssessment': 85,
        'realtimeWarning'    : [1],
        'url'                : ''
    },
    {
        'name'               : '南和互通匝道桥',
        'location'           : [114.730309, 36.990887],
        'conditionAssessment': 87,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '天桥一',
        'location'           : [114.740186, 36.98852],
        'conditionAssessment': 87,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '板式通道二',
        'location'           : [114.744637, 36.988009],
        'conditionAssessment': 65,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '分离立交四',
        'location'           : [114.754842, 36.986928],
        'conditionAssessment': 85,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '天桥二',
        'location'           : [114.765119, 36.984654],
        'conditionAssessment': 83,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '小桥',
        'location'           : [114.775912, 36.980737],
        'conditionAssessment': 83,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '邢沧干渠中桥',
        'location'           : [114.788439, 36.976347],
        'conditionAssessment': 72,
        'realtimeWarning'    : [],
        'url'                : ''
    },
    {
        'name'               : '西三召中桥',
        'location'           : [114.803885, 36.974099],
        'conditionAssessment': 80,
        'realtimeWarning'    : [],
        'url'                : ''
    }
]

daye_road = [
    {
        'name'               : '叶榭大桥',
        'location'           : [121.334907, 30.957056],
        'conditionAssessment': 89,
        'realtimeWarning'    : [],
        'url'                : 'https://www.baidu.com/'
    },
    {
        'name'               : '先锋港桥',
        'location'           : [121.351810, 30.958117],
        'conditionAssessment': 65,
        'realtimeWarning'    : [1, 2],
        'url'                : 'http://www.163.com/'
    },
    {
        'name'               : '千步泾桥',
        'location'           : [121.369238, 30.958488],
        'conditionAssessment': 92,
        'realtimeWarning'    : [],
        'url'                : 'http://www.qq.com/'
    },
    {
        'name'               : '大寨河桥',
        'location'           : [121.379848, 30.957660],
        'conditionAssessment': 96,
        'realtimeWarning'    : [],
        'url'                : 'https://www.baidu.com/'
    },
    {
        'name'               : '巨潮港桥',
        'location'           : [121.389036, 30.958976],
        'conditionAssessment': 81,
        'realtimeWarning'    : [],
        'url'                : 'https://www.baidu.com/'
    },
    {
        'name'               : '红旗港桥',
        'location'           : [121.401515, 30.961608],
        'conditionAssessment': 88,
        'realtimeWarning'    : [],
        'url'                : 'https://www.baidu.com/'
    },
    {
        'name'               : '沙港桥',
        'location'           : [121.412284, 30.963776],
        'conditionAssessment': 82,
        'realtimeWarning'    : [],
        'url'                : 'https://www.baidu.com/'
    },
    {
        'name'               : '光辉河桥',
        'location'           : [121.419571, 30.965533],
        'conditionAssessment': 84,
        'realtimeWarning'    : [],
        'url'                : 'https://www.baidu.com/'
    },
    {
        'name'               : '竹港桥',
        'location'           : [121.427382, 30.967829],
        'conditionAssessment': 87,
        'realtimeWarning'    : [],
        'url'                : 'https://www.baidu.com/'
    },
    {
        'name'               : '横泾桥',
        'location'           : [121.449525, 30.973897],
        'conditionAssessment': 83,
        'realtimeWarning'    : [],
        'url'                : 'https://www.baidu.com/'
    },
    {
        'name'               : '白庙港桥',
        'location'           : [121.474699, 30.980028],
        'conditionAssessment': 69,
        'realtimeWarning'    : [1, 2],
        'url'                : 'https://www.baidu.com/'
    },
    {
        'name'               : '金汇港桥',
        'location'           : [121.503949, 30.982894],
        'conditionAssessment': 86,
        'realtimeWarning'    : [],
        'url'                : 'https://www.baidu.com/'
    },
    {
        'name'               : '新强港桥',
        'location'           : [121.532579, 30.981778],
        'conditionAssessment': 79,
        'realtimeWarning'    : [],
        'url'                : 'https://www.baidu.com/'
    },
    {
        'name'               : '西新港桥',
        'location'           : [121.554062, 30.983930],
        'conditionAssessment': 75,
        'realtimeWarning'    : [2],
        'url'                : 'https://www.baidu.com/'
    },
    {
        'name'               : '泰青港桥',
        'location'           : [121.565489, 30.984981],
        'conditionAssessment': 77,
        'realtimeWarning'    : [],
        'url'                : 'https://www.baidu.com/'
    },
    {
        'name'               : '泰东港桥',
        'location'           : [121.574593, 30.985683],
        'conditionAssessment': 79,
        'realtimeWarning'    : [],
        'url'                : 'https://www.baidu.com/'
    },
    {
        'name'               : '一号港桥',
        'location'           : [121.584775, 30.986654],
        'conditionAssessment': 83,
        'realtimeWarning'    : [1, 1],
        'url'                : 'https://www.baidu.com/'
    }
]

assessment = {
    'name'    : '综合性能',
    'weight'  : 1.0,
    'children': [
        {
            'name'    : '结构安全性',
            'weight'  : 0.5,
            'children': [
                {
                    'name'  : '混凝土强度',
                    'weight': 0.2,
                    'value' : 80
                },
                {
                    'name'    : '箱梁中性轴高度',
                    'weight'  : 0.3,
                    'children': [
                        {
                            'name'  : '跨中截面中性轴高度',
                            'weight': 0.4,
                            'value' : 85
                        },
                        {
                            'name'  : '1/4截面中性轴高度',
                            'weight': 0.3,
                            'value' : 85
                        },
                        {
                            'name'  : '3/4截面中性轴高度',
                            'weight': 0.3,
                            'value' : 82
                        }
                    ]
                },
                {
                    'name'  : '上部结构移动荷载影响线',
                    'weight': 0.3,
                    'value' : 88
                },
                {
                    'name'    : '上部结构振动模态',
                    'weight'  : 0.2,
                    'children': [
                        {
                            'name'  : '一阶模态',
                            'weight': 0.5,
                            'value' : 80
                        },
                        {
                            'name'  : '二阶模态',
                            'weight': 0.5,
                            'value' : 84
                        },
                    ]
                }
            ]
        },
        {
            'name'    : '结构耐久性',
            'weight'  : 0.25,
            'children': [
                {
                    'name'  : '混凝土碳化深度',
                    'weight': 0.3,
                    'value' : 85
                },
                {
                    'name'  : '混凝土保护层厚度',
                    'weight': 0.3,
                    'value' : 80
                },
                {
                    'name'  : '钢筋锈蚀',
                    'weight': 0.4,
                    'value' : 75
                }
            ]
        },
        {
            'name'    : '结构使用性',
            'weight'  : 0.25,
            'children': [
                {
                    'name'  : '路面平整度',
                    'weight': 0.6,
                    'value' : 92
                },
                {
                    'name'  : '伸缩缝跳车',
                    'weight': 0.4,
                    'value' : 78
                }
            ]
        }
    ]
}

with open(r'data\bridge2.json', 'w') as json_output_file:
    json.dump(baofu_highway, json_output_file)
