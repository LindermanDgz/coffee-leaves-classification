def _binarize(self):
    GREEN_LIMIT_BELOW = 30
    GREEN_LIMIT_ABOVE = 120
    _, segments_below_green = cv.threshold(self.masked_roi_hue,
                                           GREEN_LIMIT_BELOW,
                                           179,
                                           cv.THRESH_BINARY)
    _, segments_above_green = cv.threshold(self.masked_roi_hue,
                                           GREEN_LIMIT_ABOVE,
                                           179,
                                           cv.THRESH_BINARY_INV)
    self.binary = cv.bitwise_and(segments_below_green, segments_above_green)
