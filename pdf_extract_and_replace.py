import pymupdf

def extract_text_from_pdf(pdf_path):
    
    pdf_document = pymupdf.open(pdf_path)
    
    extracted_text = " "
    
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        
        page_text = page.get_text()
        
        extracted_text += page_text + "\n"
    
    return extracted_text

pdf_path = 'C:/Users/chris.schwartz/OneDrive - TCI Products Co/Desktop/GHS Backup/GHS labels/TCI Labels/Thinners - 110/DT5/AF/PDF/DT5 F-Style Gallon.pdf'
text = extract_text_from_pdf(pdf_path)

print(text)