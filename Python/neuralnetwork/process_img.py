import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def process_image(image_path):
    # 2. 转换为灰度图
    img = Image.open(image_path).convert('L')
    
    # 3. 调整尺寸到28x28像素（与训练数据一致）
    img = img.resize((28, 28))
    
    # # 4. 反色处理（MNIST是白底黑字，普通照片通常是黑底白字）
    # img = np.invert(img)
    
    # 5. 归一化并调整维度
    img = np.array(img).astype('float32') / 255.0
    img = img.reshape(1, 28, 28, 1)  # 添加batch和通道维度
    
    # 可视化预处理结果
    plt.imshow(img[0,:,:,0], cmap='gray')
    plt.title("预处理后的图像")
    plt.show()
    
    return img

my_img = r"c:\Users\hemingyang\Pictures\num_5.jpg"
proc_img = process_image(my_img)
