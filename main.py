import streamlit as st

from llm import get_item_description

st.title('Upload pics of items you want to sell')
st.warning('Only one pic per item')

if "products" not in st.session_state:
    st.session_state.products = []

# Sidebar for uploading an image
images = st.file_uploader("Upload items", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if images:
    for image in images:
        st.session_state.products.append({'name': image.name, 'image': image})

for product in st.session_state.products:
    with st.expander(product['name']):
        image = product['image']
        st.image(image, caption='Uploaded Image', width=100)
        with st.chat_message('Item Description'):
            st.write(get_item_description(image))
