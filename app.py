from docx import Document
from docx.shared import Inches

document = Document()

# profile picture
document.add_picture('profile.png',width=Inches(1.25))

# name phone number and email details
name = input('name? ')
phone_number = input('phone number? ')
email = input('email? ')

document.add_paragraph(
    name + '|' + phone_number + '|' + email
)

# about me

document.add_heading('About me')
document.add_paragraph(input('About yourself? '))


document.save('cv.docx')