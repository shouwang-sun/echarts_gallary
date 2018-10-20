# -*- coding: utf-8 -*-
__author__ = 'SUNShouwang'

import numpy as np
from PIL import Image, ImageDraw


class View(object):

    def __init__(self, image):
        self.image = Image.open(image)
        self.image_size = np.array(self.image.size, dtype=np.float)
        self.image_drawer = ImageDraw.Draw(self.image)
        self.project_matrix = np.zeros((2, 4))

    def calibrate(self, pixel_a, pixel_b, point_a, point_b):
        pass

    def project(self, point_x):
        if isinstance(point_x, (tuple, list)): point_x = np.array(point_x)
        pixel_x = np.dot(self.project_matrix, np.append(point_x, 1))
        return pixel_x.round().astype(np.int).tolist()

    def draw(self, pixel_x, show=False):
        x, y = pixel_x
        r = self.image_size.min()/100
        self.image_drawer.ellipse([x-r, y-r, x+r, y+r], fill='red', outline='red')
        if show:
            self.image.show()

    def remap_to_container(self, pixel_x, container_size):
        if isinstance(pixel_x, (tuple, list)): pixel_x = np.array(pixel_x)
        if isinstance(container_size, (tuple, list)): container_size = np.array(container_size)
        pixel_x = pixel_x - self.image_size / 2
        pixel_x = pixel_x * (container_size / self.image_size).min()
        pixel_x = pixel_x + container_size / 2
        return  pixel_x.round().astype(int).tolist()


class ElevationView(View):
    def calibrate(self, pixel_a, pixel_b, point_a, point_b):
        # override calibrate method of the base class
        if isinstance(pixel_a, (tuple, list)): pixel_a = np.array(pixel_a, dtype=np.float)
        if isinstance(pixel_b, (tuple, list)): pixel_b = np.array(pixel_b, dtype=np.float)
        if isinstance(point_a, (tuple, list)): point_a = np.array(point_a, dtype=np.float)
        if isinstance(point_b, (tuple, list)): point_b = np.array(point_b, dtype=np.float)
        du, dv = pixel_b - pixel_a
        dx, dy, dz = point_b - point_a
        self.project_matrix[0, 2] = du / dz
        self.project_matrix[1, 1] = dv / dy
        self.project_matrix[:, 3] = pixel_a - np.dot(self.project_matrix, np.append(point_a, 1))


class PlanView(View):
    def calibrate(self, pixel_a, pixel_b, point_a, point_b):
        # override calibrate method of the base class
        if isinstance(pixel_a, (tuple, list)): pixel_a = np.array(pixel_a, dtype=np.float)
        if isinstance(pixel_b, (tuple, list)): pixel_b = np.array(pixel_b, dtype=np.float)
        if isinstance(point_a, (tuple, list)): point_a = np.array(point_a, dtype=np.float)
        if isinstance(point_b, (tuple, list)): point_b = np.array(point_b, dtype=np.float)
        du, dv = pixel_b - pixel_a
        dx, dy, dz = point_b - point_a
        self.project_matrix[0, 2] = du / dz
        self.project_matrix[1, 0] = dv / dx
        self.project_matrix[:, 3] = pixel_a - np.dot(self.project_matrix, np.append(point_a, 1))


class SectionView(View):
    def calibrate(self, pixel_a, pixel_b, point_a, point_b):
        # override calibrate method of the base class
        if isinstance(pixel_a, (tuple, list)): pixel_a = np.array(pixel_a, dtype=np.float)
        if isinstance(pixel_b, (tuple, list)): pixel_b = np.array(pixel_b, dtype=np.float)
        if isinstance(point_a, (tuple, list)): point_a = np.array(point_a, dtype=np.float)
        if isinstance(point_b, (tuple, list)): point_b = np.array(point_b, dtype=np.float)
        du, dv = pixel_b - pixel_a
        dx, dy, dz = point_b - point_a
        self.project_matrix[0, 0] = du / dx
        self.project_matrix[1, 1] = dv / dy
        self.project_matrix[:, 3] = pixel_a - np.dot(self.project_matrix, np.append(point_a, 1))


if __name__ == '__main__':

    from prepare_plot_data.fcxf_sensor_data import sensor_location
    elevation_view = ElevationView('image/elevationView.png')
    pixel_a, pixel_b = (315, 328), (1820, 379)
    point_a, point_b = (0, 64, -1600), (0, -64, 1600)
    elevation_view.calibrate(pixel_a, pixel_b, point_a, point_b)
    for sensor, location in  sensor_location.iteritems():
        projection = elevation_view.project(location)
        elevation_view.draw(projection)
        projection = elevation_view.remap_to_container(projection, (1200, 600))
        print 'coordinates of {} in elevation view: {}'.format(sensor, projection)
    elevation_view.image.show()
# --------------------------------------------------------------------------------
    plan_view = PlanView('image/planView.png')
    pixel_a, pixel_b = (346, 894), (1756, 300)
    point_a, point_b = (425, 0, -1500), (-425, 0, 1500)
    plan_view.calibrate(pixel_a, pixel_b, point_a, point_b)
    for sensor, location in sensor_location.iteritems():
        projection = plan_view.project(location)
        plan_view.draw(projection)
        projection = plan_view.remap_to_container(projection, (1200, 600))
        print 'coordinates of {} in plan view: {}'.format(sensor, projection)
    plan_view.image.show()
# --------------------------------------------------------------------------------
    section_view = SectionView('image/FCXF-X-03.png')
    pixel_a, pixel_b = (1787, 2417), (5804, 1709)
    point_a, point_b = (425, 0, 0), (-425, 150, 0)
    section_view.calibrate(pixel_a, pixel_b, point_a, point_b)
    for sensor, location in  sensor_location.iteritems():
        if location[2] == 0:
            projection = section_view.project(location)
            section_view.draw(projection)
            projection = section_view.remap_to_container(projection, (1200, 600))
            print 'coordinates of {} in section view: {}'.format(sensor, projection)
    section_view.image.show()
