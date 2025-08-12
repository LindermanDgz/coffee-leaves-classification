def describe(self):
    if not self._processed:
        print("Imagen aún no procesada")
        return
    self.show_summary()
    self.show_original_image()
    self.show_mask()
    self.show_roi()
    self.show_roi(hue=True)
    self.show_binary()
    self.show_histogram()
