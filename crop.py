import os

def rename_files_in_directory(directory_path):
    # Kiểm tra đường dẫn thư mục
    if not os.path.exists(directory_path):
        print(f"Directory {directory_path} does not exist.")
        return

    # Quét tất cả các file trong thư mục
    for filename in os.listdir(directory_path):
        full_path = os.path.join(directory_path, filename)
        # Kiểm tra có phải file không, có kết thúc bằng '00001.dcm' không
        if os.path.isfile(full_path) and filename.endswith('00001.dcm'):
            # Tạo tên mới bằng cách bỏ '00001' và giữ lại đuôi '.dcm'
            new_filename = filename[:-9] + '.dcm'  # Bỏ '00001' (5 ký tự) và giữ lại '.dcm'
            new_full_path = os.path.join(directory_path, new_filename)
            # Đổi tên file
            os.rename(full_path, new_full_path)
            print(f"Renamed {filename} to {new_filename}")
        else:
            print(f"Skipped {filename}")

# Gọi hàm để đổi tên các file trong thư mục chỉ định
rename_files_in_directory(r'F:\RADIAN_1038_BVNTP\X-ray Normal\XQkhongbenh')
