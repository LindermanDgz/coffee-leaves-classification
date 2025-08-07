def _create_mask(self):
    self.mask = np.zeros(self.roi_hsv.shape[:2], np.uint8)
    polygon_start = self.polygon.min(axis=0)
    polygon_at_zero = self.polygon-polygon_start
    CONTOURS = -1 # All contours
    COLOR = (255, 255, 255) # White
    THICKNESS = -1 # Fill
    self.mask = cv.drawContours(self.mask, [polygon_at_zero], CONTOURS, COLOR, THICKNESS)
    self.area = cv.countNonZero(self.mask)
