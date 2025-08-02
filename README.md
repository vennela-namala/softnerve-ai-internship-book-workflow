---
title: Automated Book Publication Workflow
emoji: 📚
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: "1.30.0"
app_file: app.py
pinned: false
---

# Automated Book Publication Workflow

## Overview
This project scrapes chapter content, allows manual rewriting (spinning), and supports multiple review iterations.

## Usage
1. Input chapter URL
2. Fetch content and read
3. Rewrite content manually
4. Save iterations using the Save button

## edits/ Folder
This folder stores all manually rewritten versions of the chapter. Each version can be saved as a separate file to track the review process.

Example:
- edits/chapter_1_edited.txt (latest version)
- edits/chapter_1_v1.txt (first rewrite)
- edits/chapter_1_v2.txt (second rewrite)

## Note
No AI tools were used for rewriting; all manual edits are your original work.
