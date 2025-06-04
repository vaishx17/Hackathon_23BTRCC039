import os
import torch
from torch import nn, optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader

# ✅ Paths
train_dir = "chest_xray/Data/train"
val_dir = "chest_xray/Data/val"

# ✅ Image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# ✅ Load data
train_dataset = datasets.ImageFolder(train_dir, transform=transform)
print(train_dataset.class_to_idx)  # Check class mapping
val_dataset = datasets.ImageFolder(val_dir, transform=transform)


train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=16)

# ✅ Load pre-trained ResNet18
model = models.resnet18(pretrained=True)
model.fc = nn.Linear(model.fc.in_features, 3)  # 3 classes: Normal, Pneumonia, COVID

# ✅ Setup
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# ✅ Train for 5 epochs
for epoch in range(5):
    model.train()
    total_loss = 0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1}, Training Loss: {total_loss/len(train_loader):.4f}")

# ✅ Save model
os.makedirs("models", exist_ok=True)
torch.save(model.state_dict(), "models/model.pth")
print("✅ Model saved to models/model.pth")
