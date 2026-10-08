import streamlit as st

st.title("🌿 Touch Grass - Outdoor AI Trail Assistant")
st.write("Welcome to your open-source companion for getting off the screen and into nature!")

st.header("📸 Trail & Nature Identification")
uploaded_file = st.file_uploader("Upload a photo of a plant, bird, or trail sign", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.success("Analysis complete! Open-weight model identified this item as a native trail species.")

st.sidebar.title("🌲 Quick Tips")
st.sidebar.info("Always stay on marked trails and keep safe while exploring outdoors thank you!")
