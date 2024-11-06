# PDF Merger

A simple Python script to merge all PDF files in a given folder into a single output PDF file.

## Features
- Scans a specified folder for all PDF files.
- Merges PDFs in the folder into a single file in the order they are found.
- Outputs the merged file to a specified path.

## Prerequisites
- Python 3.x installed
- `PyPDF2` library for PDF manipulation

## Installation

1. **Clone this repository or download the script directly**:
   ```bash
   git clone https://github.com/yourusername/pdf-merger.git
   cd pdf-merger
   ```
2. **Install the required libraries: ** Install `PyPDF2` if you haven't already:
   ```bash
   pip install PyPDF2
   ```
   
## Usage

1. Run the program
   ```bash
   python pdf_merger.py
   ```
2. When prompted, enter:
  - The path to the folder containing the PDF files you want to merge.
     - Example: `C:/Users/yourusername/Documents/pdf`
  - The output path and file name for the merged PDF.
    - Example: `C:/Users/yourusername/Desktop/output/merged_output.pdf`

