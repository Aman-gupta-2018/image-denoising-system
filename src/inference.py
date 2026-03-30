import torch
import torchvision.transforms as transforms
from PIL import Image

# Load the trained model
model = torch.load('path_to_trained_model.pth')
model.eval()

# Function to denoise the image

def denoise_image(image_path):
    image = Image.open(image_path)
    transform = transforms.Compose([
        transforms.ToTensor(),
    ])
    image_tensor = transform(image).unsqueeze(0)  # Add batch dimension

    with torch.no_grad():
        denoised_image_tensor = model(image_tensor)

    denoised_image = transforms.ToPILImage()(denoised_image_tensor.squeeze(0))
    return denoised_image

# Example usage
# denoised_img = denoise_image('path_to_noisy_image.jpg')
# denoised_img.save('path_to_denoised_image.jpg')