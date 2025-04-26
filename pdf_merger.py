import os
from PyPDF2 import PdfMerger

def merge_pdfs(folder_path, output_file):
    # create a PdfMerger object
    merger = PdfMerger()

    # get all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(folder_path, file_name)
            print(f"Adding {file_name} to the merger...")
            merger.append(file_path)

    # write out the merged PDF
    with open(output_file, "wb") as output_pdf:
        merger.write(output_pdf)
    print(f"All PDFs merged into {output_file}")


def main():
    folder_path = input("Provide folder path: ")
    # example: C:/Users/user/Documents/pdf

    output_file = input("Provide output file: ")
    # example: C:/Users/user/Desktop/output/merged_output.pdf

    merge_pdfs(folder_path, output_file)


if __name__ == "__main__":
    main()
