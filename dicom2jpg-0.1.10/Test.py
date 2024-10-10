import os

def rename_files_in_directory(directory_path):
    # Quét tất cả các file trong thư mục
    for filename in os.listdir(directory_path):
        # Kiểm tra có phải file không và có kết thúc bằng '00001' không
        if os.path.isfile(os.path.join(directory_path, filename)) and filename.endswith('00001'):
            # Tạo tên mới bằng cách bỏ '00001' cuối tên file
            new_filename = filename[:-5]
            # Đổi tên file
            os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))
            print(f"Renamed {filename} to {new_filename}")

# Gọi hàm để đổi tên các file trong thư mục chỉ định
rename_files_in_directory('F:/RADIAN_1038_BVNTP/RADIANT_BVNTP')