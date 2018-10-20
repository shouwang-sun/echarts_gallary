# -*- coding: utf-8 -*-
__author__ = 'SUNShouwang'

## import
import codecs
import json

## 保阜分离式立交桥数据
import json, codecs

baofu_highway = [
    {
        'name': u'圣水村大桥',
        'location': [114.093296, 38.882953],
        'conditionAssessment': 80,
        'realtimeWarning': [],
        'url': ''
    },
    {
        'name': u'道有沟大桥',
        'location': [114.084194, 38.884639],
        'conditionAssessment': 75,
        'realtimeWarning': [],
        'url': ''
    },
    {
        'name': u'龙堂沟大桥',
        'location': [114.079911, 38.884806],
        'conditionAssessment': 91,
        'realtimeWarning': [],
        'url': ''
    },
    {
        'name': u'黄土岭1号大桥',
        'location': [114.075912, 38.885676],
        'conditionAssessment': 80,
        'realtimeWarning': [],
        'url': ''
    },
    {
        'name': u'黄土岭2号大桥',
        'location': [114.067277, 38.883691],
        'conditionAssessment': 72,
        'realtimeWarning': [],
        'url': ''
    },
    {
        'name': u'阜长线分离式立交',
        'location': [114.052989, 38.881409],
        'conditionAssessment': 90,
        'realtimeWarning': [2, 2],
        'url': ''
    },
    {
        'name': u'不老树大桥',
        'location': [114.043609, 38.885155],
        'conditionAssessment': 85,
        'realtimeWarning': [],
        'url': ''
    },
    {
        'name': u'北流河大桥',
        'location': [114.035213, 38.890308],
        'conditionAssessment': 80,
        'realtimeWarning': [],
        'url': ''
    },
    {
        'name': u'走道河大桥',
        'location': [114.028652, 38.893247],
        'conditionAssessment': 90,
        'realtimeWarning': [],
        'url': ''
    },
    {
        'name': u'菜地沟大桥',
        'location': [114.022469, 38.894419],
        'conditionAssessment': 90,
        'realtimeWarning': [],
        'url': ''
    },
    {
        'name': u'头道沟大桥',
        'location': [114.018135, 38.895399],
        'conditionAssessment': 75,
        'realtimeWarning': [],
        'url': ''
    },
    {
        'name': u'石湖沟大桥',
        'location': [114.016065, 38.895997],
        'conditionAssessment': 90,
        'realtimeWarning': [],
        'url': ''
    }
]

bridge1 = {
    'data': baofu_highway,
    'title': u'保阜高速阜长线分离式立交桥安全监测系统',
    'center': [114.052989, 38.881409],
    'zoom': 15
}
with codecs.open('data/bridge2.json', 'w', encoding='utf-8') as json_output_file:
    json.dump(bridge1, json_output_file,
              ensure_ascii=False,
              encoding='utf-8',
              indent=4,
              separators=[',', ': '],
              sort_keys=True
              )

## 南澧河大桥数据
import json, codecs

xinglin_highway = [
    {
        'name': u'分离式立交一',
        'location': [114.672845, 37.006556],
        'conditionAssessment': 91,
        'realtimeWarning': [],
    },
    {
        'name': u'护城河中桥',
        'location': [114.687977, 37.002045],
        'conditionAssessment': 85,
        'realtimeWarning': [],
    },
    {
        'name': u'分离立交二',
        'location': [114.696336, 37.000594],
        'conditionAssessment': 85,
        'realtimeWarning': [],
    },
    {
        'name': u'溜子河大桥',
        'location': [114.70553, 36.999333],
        'conditionAssessment': 72,
        'realtimeWarning': [],
    },
    {
        'name': u'分离立交三',
        'location': [114.707695, 36.999037],
        'conditionAssessment': 85,
        'realtimeWarning': [],
    },
    {
        'name': u'南澧河大桥',
        'location': [114.724448, 36.993363],
        'conditionAssessment': 85,
        'realtimeWarning': [1],
    },
    {
        'name': u'南和互通匝道桥',
        'location': [114.730309, 36.990887],
        'conditionAssessment': 87,
        'realtimeWarning': [],
    },
    {
        'name': u'天桥一',
        'location': [114.740186, 36.98852],
        'conditionAssessment': 87,
        'realtimeWarning': [],
    },
    {
        'name': u'板式通道二',
        'location': [114.744637, 36.988009],
        'conditionAssessment': 65,
        'realtimeWarning': [],
    },
    {
        'name': u'分离立交四',
        'location': [114.754842, 36.986928],
        'conditionAssessment': 85,
        'realtimeWarning': [],
    },
    {
        'name': u'天桥二',
        'location': [114.765119, 36.984654],
        'conditionAssessment': 83,
        'realtimeWarning': [],
    },
    {
        'name': u'小桥',
        'location': [114.775912, 36.980737],
        'conditionAssessment': 83,
        'realtimeWarning': [],
    },
    {
        'name': u'邢沧干渠中桥',
        'location': [114.788439, 36.976347],
        'conditionAssessment': 72,
        'realtimeWarning': [],
    },
    {
        'name': u'西三召中桥',
        'location': [114.803885, 36.974099],
        'conditionAssessment': 80,
        'realtimeWarning': [],
    }
]

bridge2 = {
    'data': xinglin_highway,
    'title': u'邢临高速南澧河大桥安全监测系统',
    'center': [114.765119,36.984654],
    'zoom': 14
}
with codecs.open('data/bridge2.json', 'w', encoding='utf-8') as json_output_file:
    json.dump(
        bridge2, json_output_file,
        ensure_ascii=False,
        encoding='utf-8',
        indent=4,
        separators=[',', ': '],
        sort_keys=True
    )

## 大叶公路数据
daye_road = [
    {
        'name': '叶榭大桥',
        'location': [121.334907, 30.957056],
        'conditionAssessment': 89,
        'realtimeWarning': [],
        'url': 'https://www.baidu.com/'
    },
    {
        'name': '先锋港桥',
        'location': [121.351810, 30.958117],
        'conditionAssessment': 65,
        'realtimeWarning': [1, 2],
        'url': 'http://www.163.com/'
    },
    {
        'name': '千步泾桥',
        'location': [121.369238, 30.958488],
        'conditionAssessment': 92,
        'realtimeWarning': [],
        'url': 'http://www.qq.com/'
    },
    {
        'name': '大寨河桥',
        'location': [121.379848, 30.957660],
        'conditionAssessment': 96,
        'realtimeWarning': [],
        'url': 'https://www.baidu.com/'
    },
    {
        'name': '巨潮港桥',
        'location': [121.389036, 30.958976],
        'conditionAssessment': 81,
        'realtimeWarning': [],
        'url': 'https://www.baidu.com/'
    },
    {
        'name': '红旗港桥',
        'location': [121.401515, 30.961608],
        'conditionAssessment': 88,
        'realtimeWarning': [],
        'url': 'https://www.baidu.com/'
    },
    {
        'name': '沙港桥',
        'location': [121.412284, 30.963776],
        'conditionAssessment': 82,
        'realtimeWarning': [],
        'url': 'https://www.baidu.com/'
    },
    {
        'name': '光辉河桥',
        'location': [121.419571, 30.965533],
        'conditionAssessment': 84,
        'realtimeWarning': [],
        'url': 'https://www.baidu.com/'
    },
    {
        'name': '竹港桥',
        'location': [121.427382, 30.967829],
        'conditionAssessment': 87,
        'realtimeWarning': [],
        'url': 'https://www.baidu.com/'
    },
    {
        'name': '横泾桥',
        'location': [121.449525, 30.973897],
        'conditionAssessment': 83,
        'realtimeWarning': [],
        'url': 'https://www.baidu.com/'
    },
    {
        'name': '白庙港桥',
        'location': [121.474699, 30.980028],
        'conditionAssessment': 69,
        'realtimeWarning': [1, 2],
        'url': 'https://www.baidu.com/'
    },
    {
        'name': '金汇港桥',
        'location': [121.503949, 30.982894],
        'conditionAssessment': 86,
        'realtimeWarning': [],
        'url': 'https://www.baidu.com/'
    },
    {
        'name': '新强港桥',
        'location': [121.532579, 30.981778],
        'conditionAssessment': 79,
        'realtimeWarning': [],
        'url': 'https://www.baidu.com/'
    },
    {
        'name': '西新港桥',
        'location': [121.554062, 30.983930],
        'conditionAssessment': 75,
        'realtimeWarning': [2],
        'url': 'https://www.baidu.com/'
    },
    {
        'name': '泰青港桥',
        'location': [121.565489, 30.984981],
        'conditionAssessment': 77,
        'realtimeWarning': [],
        'url': 'https://www.baidu.com/'
    },
    {
        'name': '泰东港桥',
        'location': [121.574593, 30.985683],
        'conditionAssessment': 79,
        'realtimeWarning': [],
        'url': 'https://www.baidu.com/'
    },
    {
        'name': '一号港桥',
        'location': [121.584775, 30.986654],
        'conditionAssessment': 83,
        'realtimeWarning': [1, 1],
        'url': 'https://www.baidu.com/'
    }
]

## 评估数据
assessment = {
    'name': u'综合性能',
    'weight': 1.0,
    'children': [
        {
            'name': u'结构安全性',
            'weight': 0.5,
            'children': [
                {
                    'name': u'混凝土强度',
                    'weight': 0.2,
                    'value': 85
                },
                {
                    'name': u'箱梁中性轴高度',
                    'weight': 0.3,
                    'children': [
                        {
                            'name': u'跨中截面中性轴高度',
                            'weight': 0.4,
                            'value': 88
                        },
                        {
                            'name': u'1/4截面中性轴高度',
                            'weight': 0.3,
                            'value': 86
                        },
                        {
                            'name': u'3/4截面中性轴高度',
                            'weight': 0.3,
                            'value': 87
                        }
                    ]
                },
                {
                    'name': u'横向联系',
                    'weight': 0.3,
                    'value': 80,
                    'children': [
                        {
                            'name': u'顶板湿接缝',
                            'weight': 0.5,
                            'value': 83
                        },
                        {
                            'name': u'横隔板',
                            'weight': 0.5,
                            'value': 80
                        }
                    ]
                },
                {
                    'name': u'上部结构振动模态',
                    'weight': 0.2,
                    'children': [
                        {
                            'name': u'一阶模态',
                            'weight': 0.5,
                            'value': 82
                        },
                        {
                            'name': u'二阶模态',
                            'weight': 0.5,
                            'value': 84
                        },
                    ]
                }
            ]
        },
        {
            'name': u'结构耐久性',
            'weight': 0.25,
            'children': [
                {
                    'name': u'混凝土碳化深度',
                    'weight': 0.3,
                    'value': 80
                },
                {
                    'name': u'混凝土保护层厚度',
                    'weight': 0.3,
                    'value': 82
                },
                {
                    'name': u'钢筋锈蚀',
                    'weight': 0.4,
                    'value': 80
                }
            ]
        },
        {
            'name': u'结构使用性',
            'weight': 0.25,
            'children': [
                {
                    'name': u'路面平整度',
                    'weight': 0.6,
                    'value': 80
                },
                {
                    'name': u'伸缩缝跳车',
                    'weight': 0.4,
                    'value': 81
                }
            ]
        }
    ]
}

import codecs, json
with codecs.open(r'data\assessment.json', 'w', encoding='utf-8') as json_output_file:
    json.dump(
        assessment, json_output_file,
        ensure_ascii=False,
        encoding='utf-8',
        indent=4,
        separators=[',', ': '],
        sort_keys=True
    )

## bridge data
sensor_set = [{
    'name': 'FCXF-X',
    'image': 'image/bridge.png',
    'location': [],
    'subset': [{
        'name': 'FCXF-X-01',
        'image': 'image/FCXF-X-01',
        'location': [200, 220],
        'subset': [{
            'name': 'P01',
            'location': [581, 387],
            'subset': [{
                'name': 'FCXF-X-01-D01'
            }, {
                'name': 'FCXF-X-01-T01'
            }]
        }, {
            'name': 'P02',
            'location': [903, 337],
            'subset': [{
                'name': 'FCXF-X-01-D02'
            }]
        }]
    }, {
        'name': 'FCXF-X-02',
        'image': 'image/FCXF-X-02',
        'location': [356, 182],
        'subset': [{
            'name': 'P01',
            'location': [289, 283],
            'subset': [{
                'name': 'FCXF-X-02-S01'
            }, {
                'name': 'FCXF-X-02-T01'
            }]
        }, {
            'name': 'P02',
            'location': [289, 323],
            'subset': [{
                'name': 'FCXF-X-02-S02'
            }, {
                'name': 'FCXF-X-02-T02'
            }, {
                'name': 'FCXF-X-02-D01'
            }]
        }, {
            'name': 'P03',
            'location': [289, 363],
            'subset': [{
                'name': 'FCXF-X-02-S03'
            }, {
                'name': 'FCXF-X-02-T03'
            }]
        }, {
            'name': 'P04',
            'location': [878, 280],
            'subset': [{
                'name': 'FCXF-X-02-S04'
            }, {
                'name': 'FCXF-X-02-T04'
            }]
        }, {
            'name': 'P05',
            'location': [878, 320],
            'subset': [{
                'name': 'FCXF-X-02-S05'
            }, {
                'name': 'FCXF-X-02-T05'
            }]
        }, {
            'name': 'P06',
            'location': [878, 360],
            'subset': [{
                'name': 'FCXF-X-02-S06'
            }, {
                'name': 'FCXF-X-02-T06'
            }]
        }, {
            'name': 'P07',
            'location': [319, 387],
            'subset': [{
                'name': 'FCXF-X-02-A01'
            }]
        }]
    }, {
        'name': 'FCXF-X-03',
        'image': 'image/FCXF-X-03',
        'location': [568, 175],
        'subset': [{
            'name': 'P01',
            'location': [289, 283],
            'subset': [{
                'name': 'FCXF-X-03-S01'
            }, {
                'name': 'FCXF-X-03-T01'
            }]
        }, {
            'name': 'P02',
            'location': [289, 323],
            'subset': [{
                'name': 'FCXF-X-03-S02'
            }, {
                'name': 'FCXF-X-03-T02'
            }, {
                'name': 'FCXF-X-03-D01'
            }]
        }, {
            'name': 'P03',
            'location': [289, 363],
            'subset': [{
                'name': 'FCXF-X-03-S03'
            }, {
                'name': 'FCXF-X-03-T03'
            }]
        }, {
            'name': 'P04',
            'location': [878, 280],
            'subset': [{
                'name': 'FCXF-X-03-S04'
            }, {
                'name': 'FCXF-X-03-T04'
            }]
        }, {
            'name': 'P05',
            'location': [878, 320],
            'subset': [{
                'name': 'FCXF-X-03-S05'
            }, {
                'name': 'FCXF-X-03-T05'
            }]
        }, {
            'name': 'P06',
            'location': [878, 360],
            'subset': [{
                'name': 'FCXF-X-03-S06'
            }, {
                'name': 'FCXF-X-03-T06'
            }]
        }, {
            'name': 'P07',
            'location': [289, 303],
            'subset': [{
                'name': 'FCXF-X-03-S07'
            }, {
                'name': 'FCXF-X-03-T07'
            }]
        }, {
            'name': 'P08',
            'location': [289, 343],
            'subset': [{
                'name': 'FCXF-X-03-S08'
            }, {
                'name': 'FCXF-X-03-T08'
            }]
        }, {
            'name': 'P09',
            'location': [878, 300],
            'subset': [{
                'name': 'FCXF-X-03-S09'
            }, {
                'name': 'FCXF-X-03-T09'
            }]
        }, {
            'name': 'P10',
            'location': [878, 340],
            'subset': [{
                'name': 'FCXF-X-03-S10'
            }, {
                'name': 'FCXF-X-03-S10'
            }]
        }, {
            'name': 'P11',
            'location': [319, 387],
            'subset': [{
                'name': 'FCXF-X-03-A01'
            }]
        }, {
            'name': 'P12',
            'location': [844, 387],
            'subset': [{
                'name': 'FCXF-X-03-A02'
            }]
        }]
    }, {
        'name': 'FCXF-X-04',
        'image': 'image/FCXF-X-04',
        'location': [797, 166],
        'subset': [{
            'name': 'P01',
            'location': [289, 283],
            'subset': [{
                'name': 'FCXF-X-04-S01'
            }, {
                'name': 'FCXF-X-04-T01'
            }]
        }, {
            'name': 'P02',
            'location': [289, 323],
            'subset': [{
                'name': 'FCXF-X-04-S02'
            }, {
                'name': 'FCXF-X-04-T02'
            }, {
                'name': 'FCXF-X-04-D01'
            }]
        }, {
            'name': 'P03',
            'location': [289, 363],
            'subset': [{
                'name': 'FCXF-X-04-S03'
            }, {
                'name': 'FCXF-X-04-T03'
            }]
        }, {
            'name': 'P04',
            'location': [878, 280],
            'subset': [{
                'name': 'FCXF-X-04-S04'
            }, {
                'name': 'FCXF-X-04-T04'
            }]
        }, {
            'name': 'P05',
            'location': [878, 320],
            'subset': [{
                'name': 'FCXF-X-04-S05'
            }, {
                'name': 'FCXF-X-04-T05'
            }]
        }, {
            'name': 'P06',
            'location': [878, 360],
            'subset': [{
                'name': 'FCXF-X-04-S06'
            }, {
                'name': 'FCXF-X-04-T06'
            }]
        }, {
            'name': 'P07',
            'location': [319, 387],
            'subset': [{
                'name': 'FCXF-X-04-A01'
            }]
        }]
    }, {
        'name': 'FCXF-X-05',
        'image': 'image/FCXF-X-05',
        'location': [955, 193],
        'subset': [{
            'name': 'P01',
            'location': [581, 387],
            'subset': [{
                'name': 'FCXF-X-05-D01'
            }, {
                'name': 'FCXF-X-05-T01'
            }]
        }]
    }]
}]
