# Base denoiser class

class BaseDenoiser:
    def __init__(self):
        pass

    def denoise(self, image):
        raise NotImplementedError("Denoise method needs to be implemented")
