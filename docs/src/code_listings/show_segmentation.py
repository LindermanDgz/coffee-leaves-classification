def show_binary(self):
    plt.imshow(self.binary, cmap='gray')
    plt.title(f"Segmentación")
    plt.axis("off")
    plt.show()
