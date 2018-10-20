# -*- coding: utf-8 -*-
__author__ = 'SUNShouwang'

import codecs
import json

import numpy as np

from prepare_plot_data.fcxf_sensor_data import sensor_location
from prepare_plot_data.projection import ElevationView, PlanView


def group_by_location(groups, sensor, sensor_location):
    grouped = False
    for i, group in enumerate(groups):
        for grouped_sensor in group:
            proj_1 = np.array(sensor_location[sensor])
            proj_2 = np.array(sensor_location[grouped_sensor])
            distance = np.linalg.norm(proj_1 - proj_2)
            if distance <= 100:
                groups[i].append(sensor)
                grouped = True
                break
        if grouped:
            break
    if not grouped:
        groups.append([sensor])
    return groups


def group_by_type(groups, sensor, sensor_type):
    for i, group in enumerate(groups):
        grouped_sensor = group[0]
        if sensor_type[grouped_sensor] == sensor_type[sensor]:
            groups[i].append(sensor)
            break
    else:
        groups.append([sensor])
    return groups


def group_center(sensor_group, sensor_projection):
    projections = map(lambda sensor: np.array(sensor_projection[sensor]), sensor_group)
    projections = np.vstack(projections)
    center = np.mean(projections, axis=0).round().astype(int).tolist()
    return center


view = ElevationView('image/bridge.png')
pixel_a = (315, 328)
pixel_b = (1820, 379)
point_a = (0, 64, -1600)
point_b = (0, -64, 1600)
view.calibrate(pixel_a, pixel_b, point_a, point_b)

sensor_projection = dict()
for name, location in sensor_location.iteritems():
    projection = view.project(location)
    view.draw(projection)
    projection = view.remap_to_container(projection, [1200, 1200])
    sensor_projection[name] = projection
view.image.show()

sensors = sensor_projection.keys()
sensors.sort()
location_groups = reduce(lambda groups, sensor: group_by_location(groups, sensor, sensor_projection), sensors, [])
group_centers = map(lambda location_group: group_center(location_group, sensor_projection), location_groups)

bridge_view = list()
for center, group in zip(group_centers, location_groups):
    bridge_view.append({'center': center, 'group': group})

view = PlanView('image/bridge.png')
pixel_a = (346, 1885)
pixel_b = (1756, 1291)
point_a = (425, 0, -1500)
point_b = (-425, 0, 1500)
view.calibrate(pixel_a, pixel_b, point_a, point_b)

sensor_projection = dict()
for name, location in sensor_location.iteritems():
    projection = view.project(location)
    view.draw(projection)
    projection = view.remap_to_container(projection, [1200, 1200])
    sensor_projection[name] = projection
view.image.show()

sensors = sensor_projection.keys()
sensors.sort()
location_groups = reduce(lambda groups, sensor: group_by_location(groups, sensor, sensor_projection), sensors, [])
group_centers = map(lambda location_group: group_center(location_group, sensor_projection), location_groups)

for center, group in zip(group_centers, location_groups):
    bridge_view.append({'center': center, 'group': group})


with codecs.open('data/bridgeView.json', 'w', encoding='utf-8') as json_output_file:
    json.dump(
        bridge_view,
        json_output_file,
        ensure_ascii=False,
        encoding='utf-8',
        indent=4,
        separators=[',', ': '],
        sort_keys=True
    )

""" For bridgeViewSunBurst
view = ElevationView('image/elevationView.png')
pixel_a = (315, 328)
pixel_b = (1820, 379)
point_a = (0, 64, -1600)
point_b = (0, -64, 1600)
view.calibrate(pixel_a, pixel_b, point_a, point_b)

for name, location in sensor_location.iteritems():
    projection = view.project(location)
    projection = view.remap_to_container(projection, [1200, 600])
    sensor_location[name] = projection

sensors = sensor_location.keys()
sensors.sort()
location_groups = reduce(lambda groups, sensor: group_by_location(groups, sensor, sensor_location), sensors, [])
group_centers = map(lambda location_group: group_center(location_group, sensor_location), location_groups)

# 嵌套调用map和reduce，简洁但晦涩
group_by_type_ = lambda sensors: reduce(lambda groups, sensor: group_by_type(groups, sensor, sensor_type), sensors, [])
location_type_groups = map(group_by_type_, location_groups)

sensor_tree = []
type_names = [u'加速度传感器', u'位移传感器', u'应变传感器', u'温度传感器', u'振弦应变传感器', u'振弦温度传感器']
for location_group, center in zip(location_type_groups, group_centers):
    location_level = {
        'name': location_group[0][0][:9],
        'center': center,
        'children': [{'name': type_name, 'children': []} for type_name in type_names]
    }
    sensor_tree.append(location_level)
    for type_group in location_group:
        sensor_level = [{'name': sensor_name, 'value': 1} for sensor_name in type_group]
        sensor_name = type_group[0]
        index = type_names.index(sensor_type[sensor_name])
        location_level['children'][index]['children'] = sensor_level

with codecs.open('data/bridgeSunburst.json', 'w', encoding='utf-8') as json_output_file:
    json.dump(
        sensor_tree,
        json_output_file,
        ensure_ascii=False,
        encoding='utf-8',
        indent=4,
        separators=[',', ': '],
        sort_keys=True
    )

# sensor_data = list()
# for name, location in sensor_location.iteritems():
#     sensor_data.append({
#         'name': name,
#         'location': location,
#         'type': sensor_type[name],
#         'unit': sensor_unit[sensor_type[name]],
#         'threshold': sensor_threshold[name]
#     })
"""
