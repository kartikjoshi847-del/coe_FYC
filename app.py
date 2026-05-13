
import streamlit as st
from PIL import Image, ImageOps
import io

# Page configuration
st.set_page_config(page_title="Document Scanner Lite", page_icon="📄")

st.title("📄 Document to B&W PDF")
st.write("Upload an image, convert it to a black-and-white document, and download as PDF.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the image
    image = Image.open(uploaded_file)
    
    # Display original image
    st.image(image, caption="Original Image", use_container_width=True)
    
    if st.button("Process and Convert"):
        # 1. Convert to Grayscale (Black and White feel)
        # Using ImageOps.grayscale for a clean document look
        bw_image = ImageOps.grayscale(image)
        
        # Optional: Increase contrast for better readability like Adobe Scan
        # bw_image = ImageOps.autocontrast(bw_image)

        st.image(bw_image, caption="Processed Image", use_container_width=True)

        # 2. Convert to PDF
        pdf_buffer = io.BytesIO()
        
        # Ensure image is in RGB mode for PDF saving if it's not already
        # though grayscale (L) works with most PDF converters
        bw_image.save(pdf_buffer, format="PDF", resolution=100.0)
        pdf_buffer.seek(0)

        # 3. Download Button
        st.success("Conversion successful!")
        st.download_button(
            label="Download PDF",
            data=pdf_buffer,
            file_name="scanned_document.pdf",
            mime="application/pdf"
        )
