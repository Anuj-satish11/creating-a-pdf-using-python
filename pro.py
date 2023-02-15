import fpdf
import PyPDF2

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

def main():
    try:
        pdf = fpdf.FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        person = Person("John Doe", 30, "Male")
        pdf.cell(200, 10, txt=person.display_info(), ln=1)

        pdf.output("output.pdf")

        # Add watermark
        input_file = open("output.pdf", 'r')
        input_pdf = PyPDF2.PdfReader(input_file)
        watermark_file = open("watermark.pdf", 'rb')
        watermark_pdf = PyPDF2.PdfReader(watermark_file)

        pdf_page = input_pdf.getPage(0)
        watermark_page = watermark_pdf.getPage(0)
        pdf_page.mergePage(watermark_page)

        out = PyPDF2.PdfReader()
        out.addPage(pdf_page)

        merged_file = open("final_output.pdf", 'wb')
        out.write(merged_file)
        merged_file.close()
        watermark_file.close()
        input_file.close()

        print("Output written to 'final_output.pdf'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
