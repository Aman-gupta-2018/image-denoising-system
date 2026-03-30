# Traditional denoising methods

import cv2

class TraditionalDenoiser:
    @staticmethod
    def gaussian_blur(image, kernel_size=(5, 5), sigma=0):
        return cv2.GaussianBlur(image, kernel_size, sigma)

    @staticmethod
    def median_blur(image, kernel_size=5):
        return cv2.medianBlur(image, kernel_size)
