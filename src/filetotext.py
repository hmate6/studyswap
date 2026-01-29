import os

from PyPDF2 import PdfReader
from docx import Document

def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def read_pdf(file_path):
    text = []
    with open(file_path, 'rb') as f:
        reader = PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text)

def read_docx(file_path):
    doc = Document(file_path)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return "\n".join(text)

def read_doc(file_path):
    import textract
    try:
        text = textract.process(file_path).decode('utf-8')
        return text
    except Exception as e:
        print(f"Failed to read {file_path}: {e}")
        return ""

def file_to_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.txt':
        return read_txt(file_path)
    elif ext == '.pdf':
        return read_pdf(file_path)
    elif ext == '.docx':
        return read_docx(file_path)
    elif ext == '.doc':
        return read_doc(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")