# ExtractDataFromPDForImage

Python code to extract/read data from pdf and image files using tesseract ocr.  
Tesseract OCR is one the best tools to read data from pdf or image.  
This code snippet shows how we can read data from pdf or images using few lines of python code.  
This code reads data from pdf as well as images. For pdf files, we have set the page limit as 5 to read data as it takes longer time to read larger files.  
we can change this limit by changeing a variable in code.  

# Requirements

Tesseract ocr  
You can refer this article to install tesseract ocr - https://pythonforundergradengineers.com/how-to-install-pytesseract.html   
Link to directly download exe file for windows - https://sourceforge.net/projects/tesseract-ocr-alt/  

We also need to install poppler for pdf2image library.
Link to download poppler - https://blog.alivate.com.au/poppler-windows/  

# Python packages 
PIL  
pytesseract  
pdf2image  
cv2  
PyPDF2  
re  

# Troubleshoot 
If code gives "The requested operation requires elevation" error, you might need to try changing the tesseract executable to run as admin property:   
Right Click tesseract.exe -> Properties -> Compability -> Check/Uncheck Run this program as an administrator -> OK .

# Extract Data from PDF and Images   
To extract data from PDF file and Images. It also save the last image or document processed.    
This code can also handles PDF with different orientation (Upside down, 90 rotated)

# Extract Data from PDF    
To extract data from PDF without saving any temp file.    
This code does not have functionality to handle poorly oriented documents.
