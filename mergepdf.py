import PyPDF2
import sys
import os

def merge_pdfs_from_directory(directory, output):
    pdf_merger = PyPDF2.PdfMerger()
    
    # List all PDF files in the directory
    pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
    pdf_files.sort()  # Optional: Sort files alphabetically
    
    for pdf in pdf_files:
        pdf_path = os.path.join(directory, pdf)
        pdf_merger.append(pdf_path)
    
    with open(output, 'wb') as output_pdf:
        pdf_merger.write(output_pdf)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python merge_pdfs.py input_directory output.pdf")
        sys.exit(1)
    
    input_directory = sys.argv[1]
    output_pdf = sys.argv[2]
    
    merge_pdfs_from_directory(input_directory, output_pdf)
    print(f"Merged PDFs from {input_directory} into {output_pdf}")