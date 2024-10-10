import os
import shutil
import numpy as np

# Định nghĩa đường dẫn gốc và đường dẫn cho train, val và test
base_dir = r'.\Dataset'
train_dir = os.path.join(".", 'train')
val_dir = os.path.join(".", 'val')
test_dir = os.path.join(".", 'test')

# Tạo các thư mục train, val và test nếu chưa tồn tại
for dir in [train_dir, val_dir, test_dir]:
    if not os.path.exists(dir):
        os.makedirs(dir)
    for sub_dir in ['1_Normal', '2_Disease']:
        if not os.path.exists(os.path.join(dir, sub_dir)):
            os.makedirs(os.path.join(dir, sub_dir))

# Phần trăm dữ liệu cho test
test_ratio = 0.2
# Phần trăm dữ liệu cho validation từ train
val_ratio = 0.2

# Hàm để phân chia dữ liệu và sao chép các file theo study
def split_data_by_study(source, train_dir, val_dir, test_dir, test_ratio, val_ratio):
    files = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]
    
    # Lấy danh sách các study
    studies = set(f.split('-')[0] for f in files)
    studies = list(studies)
    np.random.shuffle(studies)
    
    test_split_idx = int(len(studies) * test_ratio)
    test_studies = studies[:test_split_idx]
    remaining_studies = studies[test_split_idx:]
    
    val_split_idx = int(len(remaining_studies) * val_ratio)
    val_studies = remaining_studies[:val_split_idx]
    train_studies = remaining_studies[val_split_idx:]
    
    # Hàm để sao chép file vào thư mục đích
    def copy_files(studies, dest_dir):
        for study in studies:
            study_files = [f for f in files if f.startswith(study)]
            for f in study_files:
                shutil.copy(os.path.join(source, f), os.path.join(dest_dir, f))
    
    # Sao chép các file vào thư mục tương ứng
    copy_files(train_studies, train_dir)
    copy_files(val_studies, val_dir)
    copy_files(test_studies, test_dir)

# Áp dụng hàm split_data_by_study cho mỗi thư mục con
for category in ['1_Normal', '2_Disease']:
    source_dir = os.path.join(base_dir, category)
    split_data_by_study(source_dir, os.path.join(train_dir, category), os.path.join(val_dir, category), os.path.join(test_dir, category), test_ratio, val_ratio)
