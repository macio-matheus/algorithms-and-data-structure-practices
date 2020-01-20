import numpy as np
import pandas as pd


class LogisticRegression(object):

    def __init__(self, lr: float = 0.01, b: float = 0.1):
        self.lr = lr
        self.w = np.random.uniform(0, 1)
        self.b = b

    @staticmethod
    def square_loss(y_pred, target): return np.mean(pow(y_pred - target, 2))

    @staticmethod
    def sigmoid(x): return 1 / (1 + np.exp(-x))

    def fit(self, x_train: np, y_train: np):
        for i in range(10000):
            z = np.dot(x_train, self.w) + self.b
            y_pred = LogisticRegression().sigmoid(z)
            l = LogisticRegression().square_loss(y_pred, y_train)
            gradient_w = np.dot((y_pred - y_train).T, x_train) / x_train.shape[0]
            gradient_b = np.mean(y_pred - y_train)
            self.w = self.w - self.lr * gradient_w
            self.b = self.b - self.lr * gradient_b

            print(self.w, '----', self.b, '----', gradient_b, '----', l)

        return self.b


if __name__ == '__main__':

    age = [22, 25, 47, 52, 46, 56, 55, 60, 62, 61, 18, 28, 27, 29, 49, 55, 25, 58, 19, 18, 21, 26, 40, 45, 50, 54, 23]
    itens_buyer = [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0]
    df = pd.DataFrame({"age": age, "itens_buyer": itens_buyer})

    test = df.sample(7)
    train = df[~df.isin(test)]
    train.dropna(inplace=True)

    x_train, y_train = train.age, train["itens_buyer"]
    X_test, y_test = test.age, test["itens_buyer"]

    logistc_regression = LogisticRegression()
    logistc_regression.fit(x_train, y_train)
