from docx import Document

document = Document()

name = input('name? ')
phone_number = input('phone number? ')
email = input('email? ')

document.add_paragraph('hello')


document.save('cv.docx')