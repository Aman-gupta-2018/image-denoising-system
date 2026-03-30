# Advanced Traditional Denoisers Implementation

## Non-Local Means Denoiser

def non_local_means(image, h=10):
    import cv2
    import numpy as np
    
    denoised_image = cv2.fastNlMeansDenoisingColored(image, None, h, h, 7, 21)
    return denoised_image

## Bilateral Filter Denoiser

def bilateral_filter(image, d=9, sigmaColor=75, sigmaSpace=75):
    import cv2
    
    denoised_image = cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)
    return denoised_image

## Morphological Operations Denoiser

def morphological_operations(image):
    import cv2
    import numpy as np
    
    kernel = np.ones((5,5),np.uint8)
    denoised_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    denoised_image = cv2.morphologyEx(denoised_image, cv2.MORPH_OPEN, kernel)
    return denoised_image
