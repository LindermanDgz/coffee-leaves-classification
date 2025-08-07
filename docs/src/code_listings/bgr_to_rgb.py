def _generate_image_rgb(self):
    self.image_rgb = cv.cvtColor(self.image_bgr, cv.COLOR_BGR2RGB)
