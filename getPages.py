import os
import fitz  # PyMuPDF library

def get_number_of_pages(pdf_path):
    try:
        pdf_document = fitz.open(pdf_path)
        return pdf_document.page_count
    except Exception as e:
        print(f"Error while processing {pdf_path}: {e}")
        return None

def getPdfs(directory_path):
    if not os.path.exists(directory_path):
        print(f"Directory not found: {directory_path}")
        return

    paths_to_pdf_files = []
    for root, dirs, files  in os.walk(directory_path):
        for file in files:
            if file.lower().endswith(".pdf"):
                path = os.path.join(root, file)
                paths_to_pdf_files.append(path)

    paths_to_pdf_files = sorted(paths_to_pdf_files)
    return paths_to_pdf_files

def base(path):
    return os.path.basename(path)
            

def main():
    directory_path = "./readings/"
    pdf_files = getPdfs(directory_path)
    if not pdf_files:
        print(f"No PDF files found in {directory_path}")
        return

    print(f"")
    total_pages = 0
    for i in pdf_files:
        pageNums = get_number_of_pages(i)
        strNums = str(pageNums)
        if len(strNums) == 1:
            strNums = f" {strNums}"
        print(f"{strNums} : {(i)}")
        total_pages += pageNums
    print(f"Total pages: {total_pages}")
    

main()
