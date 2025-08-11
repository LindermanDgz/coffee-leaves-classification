def _create_roi(self):
    x,y,w,h = cv.boundingRect(self.polygon)
    self.roi_rgb = self.image_rgb[y:y+h, x:x+w].copy()
    self.roi_hsv = cv.cvtColor(self.roi_rgb, cv.COLOR_RGB2HSV)
