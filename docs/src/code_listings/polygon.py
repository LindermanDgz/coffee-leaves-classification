def _create_polygon(self):
    polygon_points = [list(point.values()) for point in self.geometry]
    self.polygon = np.array(polygon_points)
