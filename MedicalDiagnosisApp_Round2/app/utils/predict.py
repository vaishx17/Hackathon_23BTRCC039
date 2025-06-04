# app/utils/predict.py

import torch
from torchvision import models, transforms
from PIL import Image
import io
import os

# Load the model architecture (ResNet18)
model = models.resnet18(pretrained=False)
num_ftrs = model.fc.in_features
model.fc = torch.nn.Linear(num_ftrs, 3)  # 3 classes: COVID-19, NORMAL, PNEUMONIA

# Load the trained weights
model_path = os.path.join("models", "model.pth")
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
model.eval()

# Class labels
classes = ['COVID-19', 'NORMAL', 'PNEUMONIA']

# Image transform
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# Prediction function
def predict_image(image_bytes):
    try:
        image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        input_tensor = transform(image).unsqueeze(0)  # Add batch dimension

        with torch.no_grad():
            outputs = model(input_tensor)
            probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
            confidence, predicted = torch.max(probabilities, 0)

        return classes[predicted.item()], round(confidence.item(), 3)

    except Exception as e:
        return "Error", 0.0
