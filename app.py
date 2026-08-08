import streamlit as st
import qrcode
from io import BytesIO

# 1. Set up the title and header
st.title("QR Code Generator")
st.write("Enter a website URL or text below to generate a downloadable QR code.")

# 2. Text input box for user
user_input = st.text_input("Website URL or Text:", placeholder="https://example.com")

# 3. Generate button logic
if st.button("Generate QR Code"):
    if user_input:
        # Create the QR code object
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4,
        )
        qr.add_data(user_input)
        qr.make(fit=True)
        
        # Generate image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Convert image to bytes buffer so Streamlit can serve it
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        
        # Display the image on screen
        st.image(buffer, caption="Your Generated QR Code", width=250)
        
        # Add a download button
        st.download_button(
            label="Download PNG",
            data=buffer.getvalue(),
            file_name="qrcode.png",
            mime="image/png"
        )
    else:
        st.warning("Enter valid url boy")
# Hide Streamlit's default menu, footer, and the floating viewer badge
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            /* Hack to hide the floating "Hosted with Streamlit" badge */
            .viewerBadge_container__1QSob,
            .styles_viewerBadge__1yB5_,
            .viewerBadge_link__1S137,
            .viewerBadge_text__1JaDK { 
                display: none !important; 
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)