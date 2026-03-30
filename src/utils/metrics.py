# Performance metrics

def psnr(target, ref):
    mse = ((target - ref) ** 2).mean()
    if mse == 0:  
        return 100
    return 20 * np.log10(255.0 / np.sqrt(mse))

def ssim(img1, img2):
    return ... # Implement SSIM calculation
