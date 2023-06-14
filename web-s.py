#attempt at using a pdf-parser to read the ESG information from Apple's 2022 ESG Report
#we will use pypdf in order to read the PDF files
import pandas as pd
from PyPDF2 import PdfReader
reader = PdfReader("2022_Apple_ESG_Report.pdf")
#pdf and .py file must be in the same folder else the program will not be able to find the pdf
#things to consider regarding text extraction: paragraphs, page numbers, headers and footers, outlines, formatting, tables, captions, ligatures, svg images, mathematical formuli,
#whitespace characters, footnotes, hyperlinks and metadata, and linearization - taken from the pypdf docs

#let's try using Tabula in order to scrape tables from PDF files and covert a PDF file dirctly into a CSV file

#Update: we could not use tabula because I do not currently possess the administrative abilities to change the system environment variables so let us attempt this via Camelot

#Update: Camelot is proving to be problematic as well because it is returning a Deprecated error since an old method that it calls upon has since been removed from the library

#goal: take page 81 from the Apple ESG pdf and correctly return a table with all the qualities that are originally displayed within the document
page = reader.pages[80]
print(page.extract_text())