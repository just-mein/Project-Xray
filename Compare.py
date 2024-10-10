import matplotlib.pyplot as plt
import numpy as np

# Dữ liệu cho các mô hình
models = ['CNN', 'VGG16', 'ResNet50', 'DenseNet121', 'Vision Transformer']
accuracy = [67.76, 72.83, 67.76, 76.92, 84.62]
sensitivity = [11.68, 19.29, 0.00, 76.65, 91.55]
specificity = [94.44, 98.31, 100.00, 77.05, 70.05]
f1_score = [0.19, 0.31, np.nan, 0.68, 0.89]

x = np.arange(len(models))

# Vẽ biểu đồ
fig, ax1 = plt.subplots(figsize=(14, 8))

# Vẽ biểu đồ cột cho Accuracy, Sensitivity, Specificity
bar_width = 0.2
ax1.bar(x - bar_width, accuracy, width=bar_width, label='Accuracy (%)')
ax1.bar(x, sensitivity, width=bar_width, label='Sensitivity (%)')
ax1.bar(x + bar_width, specificity, width=bar_width, label='Specificity (%)')

# Thiết lập trục và tiêu đề
ax1.set_xlabel('Models')
ax1.set_ylabel('Percentage')
ax1.set_title('Model Performance Comparison')
ax1.set_xticks(x)
ax1.set_xticklabels(models)
ax1.legend()

# Vẽ biểu đồ đường cho F1-Score trên trục thứ hai
ax2 = ax1.twinx()
ax2.plot(x, f1_score, color='r', marker='o', label='F1-Score (Disease)')
ax2.set_ylabel('F1-Score')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()
