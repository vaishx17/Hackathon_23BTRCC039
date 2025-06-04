# train_dummy_model.py

import torch
import torch.nn as nn
import os

# A simple dummy CNN-like model
class DummyModel(nn.Module):
    def __init__(self):
        super(DummyModel, self).__init__()
        self.fc = nn.Linear(10, 2)  # Input: 10 features, Output: 2 classes

    def forward(self, x):
        return self.fc(x)

# Create model instance
model = DummyModel()

# Ensure the models/ directory exists
os.makedirs("models", exist_ok=True)

# Save the dummy model to a file
torch.save(model.state_dict(), "models/model.pth")

print("✅ Dummy model saved at models/model.pth")
