import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 加载数据集
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# 数据预处理
# 归一化到 0-1 范围，并添加通道维度（CNN需要）
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

# 转换标签为one-hot格式
train_labels = tf.keras.utils.to_categorical(train_labels)
test_labels = tf.keras.utils.to_categorical(test_labels)

# 构建CNN模型
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# 编译模型
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
# 训练模型
history = model.fit(train_images, train_labels,
                    epochs=5,
                    batch_size=64,
                    validation_split=0.1)

# # 评估模型
# test_loss, test_acc = model.evaluate(test_images, test_labels)
# print(f'Test accuracy: {test_acc:.4f}')
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
    
    # # 可视化预处理结果
    # plt.imshow(img[0,:,:,0], cmap='gray')
    # plt.title("预处理后的图像")
    # plt.show()
    
    return img

ok = 0
# 6. 进行预测
for i in range(100):

    prediction = model.predict(process_image(r"c:\Users\hemingyang\Pictures\num_5.jpg"))
    predicted_number = np.argmax(prediction)

    if (predicted_number == 5):
        ok += 1
    print(f"预测结果：数字 {predicted_number}")
    print(f"置信度分布：{prediction[0].round(2)}")

accuracy = ok/10
print(f"accuracy: {accuracy}")