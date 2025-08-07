def _create_masked_roi(self):
    self.masked_roi_rgb = cv.bitwise_and(self.roi_rgb,
                                         self.roi_rgb, mask=self.mask)
    self.masked_roi_hue = cv.bitwise_and(self.roi_hsv[:,:,0], self.mask)
