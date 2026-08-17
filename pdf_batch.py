import os
import pymupdf

def batch_replace_pdf_text(input_dir, output_dir, replacements):
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for filename in os.listdir(input_dir):
        if not filename.lower().endswith('.pdf'):
            continue
        
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, f"updated_{filename}")
        
        doc = pymupdf.open(input_path)
        print(f"Processing: {filename}...")
        
        for page in doc:
            for target_text, replacement in replacements.items():
                text_instances = page.search_for(target_text)
                
                for rect in text_instances: 
                    page.add_redact_annot(rect)
                    page.apply_redactions()
                    page.insert_font(fontname="Calibri", fontfile="C:/windows/Fonts/CALIBRI.TTF")
                    
                    page.insert_text(
                        pymupdf.Point(rect.x0, rect.y1 - 2),
                        replacement,
                        fontsize=8,
                        fontname="Calibri",
                        color=(0, 0, 0)
                )
        
        doc.save(output_path, garbage=3, deflate=True)
        doc.close
        print(f"Saved to: {output_path}")
        
if __name__ == "__main__":
    
    SOURCE_FOLDER = '/Users/chris.schwartz/OneDrive - TCI Products Co/Desktop/GHS Backup/GHS labels/TCI Labels/Thinners - 110/DT5/AF/PDF'
    DEST_FOLDER = '/Users/chris.schwartz/OneDrive - TCI Products Co/Desktop/GHS Backup/GHS labels/TCI Labels/Thinners - 110/DT5/AF/PDF/UPDATED'
    
    TEXT_MAPPING = {
        "www.P65Warnings.ca.gov." : "Changed"
    }
    

    batch_replace_pdf_text(SOURCE_FOLDER, DEST_FOLDER, TEXT_MAPPING)
    