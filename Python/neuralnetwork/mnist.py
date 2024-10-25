import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image

# 定义神经网络模型
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(28 * 28, 128)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)
        self.fc2 = nn.Linear(128, 10)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, x):
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        x = self.softmax(x)
        return x

# 创建模型实例并加载预训练的权重
model = SimpleNN()
model.load_state_dict(torch.load('model.pth'))
model.eval()

# 定义图像预处理步骤
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),  # 确保图像是灰度图像
    transforms.Resize((28, 28)),  # 调整图像大小到28x28
    transforms.ToTensor(),  # 转换为张量
    transforms.Normalize((0.5,), (0.5,))  # 归一化
])

# 加载和预处理自定义图片
image_path = r"C:\Users\hemingyang\Pictures\images.png"  # 替换为你的图像路径
image = Image.open(image_path)
image = transform(image)
image = image.unsqueeze(0)  # 增加一个维度，批次大小为1

# 进行预测
with torch.no_grad():
    output = model(image)
    _, predicted = torch.max(output.data, 1)
    print(f'Predicted label: {predicted.item()}')
