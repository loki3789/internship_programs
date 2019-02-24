# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('0.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
number_of_pages=pdfReader.numPages
index_of_page=0
fhand=open("data.txt","w",encoding='utf8')
# creating a page object
for page in range(0,number_of_pages):

  pageObj = pdfReader.getPage(index_of_page)

# extracting text from page
  fhand.write(pageObj.extractText())

  index_of_page=index_of_page+1
  fhand.write("\n=====================================================================================================================\n")


# closing the pdf file object
pdfFileObj.close()
