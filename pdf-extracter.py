import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from llm import ask_ollama

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""

    for page_num in range(len(doc)):
        page = doc[page_num]
        # Try text extraction first
        text = page.get_text()

        if text.strip():  # If text exists, use it
            full_text += text + "\n"
        else:
            # Otherwise, use OCR
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            ocr_text = pytesseract.image_to_string(img, lang='rus+eng')
            full_text += ocr_text + "\n"

    return full_text


if __name__ == "__main__":

    print("starting the OCR process.....")
    pdf_file = "/home/manas/Documents/World-War-RAG/pdfs/2_47____bg.pdf"
    text = extract_text_from_pdf(pdf_file)
    print(text)

    prompt = f"""
        If the following paragraph is in russian translate it to english and if it is in english. 
        Try to make it grammatically and structurally correct without changing its meaning.
        The format of your output should be: 

        Result: 
        <actual output>

        DONT mention anything else but the actual translation/enhancement        
        Paragraph: {text}


    """

    result = ask_ollama(prompt)

    print(f"mistral result: {result}")

