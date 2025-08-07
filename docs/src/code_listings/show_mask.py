def show_mask(self):
    plt.imshow(self.mask, cmap='gray')
    plt.title("Máscara")
    plt.axis("off")
    plt.show()
