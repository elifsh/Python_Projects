from pdf2docx import Converter

input_file = "sample.pdf"
output_file = "sample.docx"

cv = Converter(input_file)
cv.convert(output_file)
cv.close()

