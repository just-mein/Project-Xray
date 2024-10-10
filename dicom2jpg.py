import os
import dicom2jpg

def convert_dicom_to_jpg(dicom_dir, export_location):
    # Kiểm tra và tạo thư mục lưu file JPG nếu nó chưa tồn tại
    if not os.path.exists(export_location):
        os.makedirs(export_location)
    # Sử dụng dicom2jpg để chuyển đổi tất cả các file DICOM trong thư mục
    dicom2jpg.dicom2jpg(dicom_dir, target_root=export_location)
    print(f"All DICOM files in {dicom_dir} have been converted to JPG and saved in {export_location}")

if __name__ == '__main__':
    dicom_dir = r'F:\RADIAN_1038_BVNTP\X-ray Disease\Dicom Disease\XQ Risk 2'
    export_location = r'F:\RADIAN_1038_BVNTP\X-ray Disease\Dicom Disease\XQ Risk 2'
    convert_dicom_to_jpg(dicom_dir, export_location)