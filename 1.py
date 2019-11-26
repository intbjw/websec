# encoding: utf-8
print(__doc__)

# 引用数据库
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics

# 加载数据
digits = datasets.load_digits()
images_and_labels = list(zip(digits.images, digits.target))

# 显示训练数据
for index, (image, label) in enumerate(images_and_labels[:5]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)

# 数据预处理
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# 学习训练
classifier = svm.SVC(gamma=0.001)
classifier.fit(data[:n_samples // 2], digits.target[:n_samples // 2])

# 预测数值
expected = digits.target[n_samples // 2:]
predicted = classifier.predict(data[n_samples // 2:])

# 分类器测试及混淆矩阵
print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

# 显示预测数值
images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)

plt.show()
