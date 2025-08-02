import streamlit as st
import requests
from bs4 import BeautifulSoup
import os

if not os.path.exists("edits"):
    os.mkdir("edits")

st.title("Automated Book Publication Workflow")

st.write("## Step 1: Input URL to fetch content")

url = st.text_input("Enter book chapter URL:",
                    "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1")

if url:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            main_content = soup.find('div', {'class': 'mw-parser-output'})
            text_content = main_content.get_text(separator='\n', strip=True) if main_content else "Content not found"

            st.write("## Fetched Content")
            st.text_area("Content", value=text_content, height=300)

            st.write("## Step 2: Rewrite / Spin the content manually below")
            edited_text = st.text_area("Rewrite the content here:", height=300)

            if st.button("Save Edited Version"):
                with open("edits/chapter_1_edited.txt", "w", encoding="utf-8") as f:
                    f.write(edited_text)
                st.success("Edited version saved successfully!")
        else:
            st.error(f"Failed to fetch URL. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error fetching URL: {str(e)}")
