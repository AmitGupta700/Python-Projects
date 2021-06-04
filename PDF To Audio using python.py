import PyPDF2
import pyttsx3

path= open('python book.pdf', 'rb')
pdfReader= PyPDF2.PdfFileReader(path)

from_page = pdfReader.getPage(1)
Text = from_page.extractText()

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()