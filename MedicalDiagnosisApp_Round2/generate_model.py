import torch
from torchvision import models

# Create a ResNet18 model with 3 output classes
model = models.resnet18(pretrained=True)
model.fc = torch.nn.Linear(model.fc.in_features, 3)

# Save the model's state_dict
torch.save(model.state_dict(), "models/model.pth")

print("✅ Dummy model with 3 output classes saved to 'models/model.pth'")
