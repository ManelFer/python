from PIL import Image
from io import BytesIO
from PyPDF2 import PdfFileWriter, PdfFileReader

# Carrega a imagem
im = Image.open('imagem.jpeg')

# Cria um buffer de memória para armazenar o arquivo PDF
pdf_bytes = BytesIO()

# Cria um objeto PdfFileWriter para escrever no arquivo PDF
pdf_writer = PdfFileWriter()

# Adiciona a imagem ao arquivo PDF
pdf_writer.addPage(im.convert('RGB'))

# Grava o arquivo PDF no buffer de memória
pdf_writer.write(pdf_bytes)

# Salva o arquivo PDF em um arquivo
with open('imagem.pdf', 'wb') as f:
    f.write(pdf_bytes.getvalue())
