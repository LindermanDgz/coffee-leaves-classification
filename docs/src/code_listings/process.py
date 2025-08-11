def process(self):
    self._generate_image_rgb()
    self._create_polygon()
    self._create_roi()
    self._create_mask()
    self._create_masked_roi()
    self._compute_histogram()
    self._binarize()
    self._categorize()
    self._processed = True
