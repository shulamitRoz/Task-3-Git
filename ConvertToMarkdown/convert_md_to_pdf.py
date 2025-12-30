import pdfkit
import markdown

with open("guide.md", "r", encoding="utf-8") as md_file:
    md_text = md_file.read()

html_text = markdown.markdown(md_text)

config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

pdfkit.from_string(html_text, "guide.pdf", configuration=config)

print("PDF successfully created: guide.pdf")
