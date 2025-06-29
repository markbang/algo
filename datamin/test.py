import numpy as np


# 定义激活函数（这里使用sigmoid函数）
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))


# 定义损失函数（这里使用均方误差）
def mean_squared_error(y_true, y_pred):
    return np.mean(np.square(y_true - y_pred))


class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # 初始化权重和偏置
        self.weights1 = np.random.rand(input_size, hidden_size)
        self.bias1 = np.random.rand(1, hidden_size)
        self.weights2 = np.random.rand(hidden_size, output_size)
        self.bias2 = np.random.rand(1, output_size)

    def forward(self, X):
        # 前向传播
        self.z1 = np.dot(X, self.weights1) + self.bias1
        self.a1 = sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.weights2) + self.bias2
        self.y_pred = sigmoid(self.z2)
        return self.y_pred

    def backward(self, X, y, learning_rate):
        # 反向传播
        m = X.shape[0]
        dZ2 = self.y_pred - y
        dW2 = 1 / m * np.dot(self.a1.T, dZ2)
        db2 = 1 / m * np.sum(dZ2, axis=0, keepdims=True)
        dA1 = np.dot(dZ2, self.weights2.T)
        dZ1 = dA1 * sigmoid_derivative(self.z1)
        dW1 = 1 / m * np.dot(X.T, dZ1)
        db1 = 1 / m * np.sum(dZ1, axis=0, keepdims=True)
        # 更新权重和偏置
        self.weights2 -= learning_rate * dW2
        self.bias2 -= learning_rate * db2
        self.weights1 -= learning_rate * dW1
        self.bias1 -= learning_rate * db1


# 准备数据
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])  # 学习时间，睡眠时间
y = np.array([[0.7], [0.8], [0.9], [0.95]])  # 学习成绩

# 创建神经网络
nn = NeuralNetwork(input_size=2, hidden_size=4, output_size=1)

# 训练过程
epochs = 1000
learning_rate = 0.1
for epoch in range(epochs):
    y_pred = nn.forward(X)
    loss = mean_squared_error(y, y_pred)
    nn.backward(X, y, learning_rate)
    if (epoch + 1) % 100 == 0:
        print(f"Epoch {epoch + 1}, Loss: {loss:.4f}")

# 评估
new_X = np.array([[1, 2]])  # 新的输入数据
new_y_pred = nn.forward(new_X)
print("Predicted score for new data:", new_y_pred)
