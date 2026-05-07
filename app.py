import base64
import re
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Oscar Owino | Portfolio", layout="wide")

BASE_DIR = Path(__file__).parent
HTML_FILE = BASE_DIR / "index.html"
IMAGE_FILE = BASE_DIR / "20260215_152108.jpg"

# Read the HTML
html_content = HTML_FILE.read_text(encoding="utf-8")

# Read and encode the image as base64
image_bytes = IMAGE_FILE.read_bytes()
image_b64 = base64.b64encode(image_bytes).decode("utf-8")
image_data_uri = f"data:image/jpeg;base64,{image_b64}"

# Replace the local image path in the HTML with the embedded image
html_content = re.sub(
    r'src="[^"]*20260215_152108\.jpg"',
    f'src="{image_data_uri}"',
    html_content,
    count=1
)

# Render the HTML
st.components.v1.html(html_content, height=5000, scrolling=True)