
from PIL import Image
import streamlit as st
import requests
st.title("Tải ảnh lên")
uploaded_files = st.file_uploader(
    "Tải ảnh của bạn", type=["png", "jpg", "jpeg"]
)
#URL
api_url = "https://9d82-2001-ee0-4fe9-c610-171-712c-9b53-b754.ngrok-free.app/test_post/"


#Nếu người dùng đã tải ảnh lên
if uploaded_files is not None:

    image = Image.open(uploaded_files)
    st.image(image)
    try:
        image_bytes = uploaded_files.read()

        response = requests.post(
            api_url,
            files={"img": uploaded_files}
        )
        if response.status_code == 200:
            st.success("Tải ảnh lên thành công")
        else:
            st.error(f"Lỗi: {response.status_code}")
    except Exception as e:
        st.error(e)
else:
    st.info("Hãy chọn hình ảnh để tải lên!")


