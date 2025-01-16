# import streamlit as st
# from PIL import Image
# import numpy as np
# import requests
# import tempfile
# # URL của API
# API_URL = "https://9d82-2001-ee0-4fe9-c610-171-712c-9b53-b754.ngrok-free.app/test_post/"
#
# # Tạo biến tạm để lưu trữ ảnh
# if "img_taked" not in st.session_state:
#     st.session_state.img_taked = None
#
# # Tạo khu vực hiển thị camera
# # camera_placeholder = st.empty()
# camera_capture = st.camera_input("Camera", key="test_app")
#
# # Hiển thị ảnh đã chụp và kết quả dự đoán
# image_capture = st.empty()
#
# if camera_capture:
#     # Chuyển đổi frame sang định dạng PIL Image
#     st.session_state.img_taked = camera_capture
#     img_taked = Image.open(camera_capture)
#
#     # Gửi ảnh đến API để dự đoán
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
#         img_taked.save(temp.name)
#         with open(temp.name, "rb") as file:
#             files = {"file": file}
#             response = requests.post(API_URL, files=files)
#             print(response)
#
#     # Hiển thị kết quả dự đoán
#     if response.status_code == 200:
#         result = response.json()
#         st.success(f"Label: {result['label']}, Confidence: {result['confidence']}")
#     else:
#         st.error("Dự đoán thất bại. Vui lòng thử lại.")
#
# # Hiển thị ảnh đã chụp
# if st.session_state.img_taked is not None:
#     image_capture.image(st.session_state.img_taked, caption="Ảnh đã chụp", channels="RGB")
#
import streamlit as st
from PIL import Image
import requests
import tempfile

# Textddr nguoi dung nhap API

input_API = st.text_input("Nhập API", "API")
# URL của API
# API_URL = "http://127.0.0.1:8080/test_post/"

# Tạo biến tạm trong session_state để lưu trữ ảnh đã chụp
if "img_taked" not in st.session_state:
    st.session_state.img_taked = None

# Tạo khu vực hiển thị camera
camera_capture = st.camera_input("Chụp ảnh bằng camera", key="camera_input")

# Tạo placeholder để hiển thị ảnh
image_display = st.empty()

if camera_capture:
    try:
        # Chuyển đổi ảnh từ camera sang định dạng PIL
        img_taked = Image.open(camera_capture)

        # Lưu ảnh vào session_state
        st.session_state.img_taked = img_taked

        # Lưu ảnh tạm thời
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
            img_taked.save(temp.name)

            # Gửi ảnh tới API với trường tên là "img"
            with open(temp.name, "rb") as file:
                API_URL = input_API + "/test_post/"
                response = requests.post(API_URL, files={"img": file})


        # Kiểm tra phản hồi từ API
        if response.status_code == 200:
            st.success(response.text)
        else:
            st.error(f"Lỗi {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"Đã xảy ra lỗi: {str(e)}")

# Hiển thị ảnh đã lưu trong session_state nếu có
if st.session_state.img_taked is not None:
    image_display.image(st.session_state.img_taked, caption="Ảnh đã lưu", channels="RGB")

