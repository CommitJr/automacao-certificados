import csv
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO

# Caminhos dos arquivos
arquivo_csv = "presenca.csv"
modelo_pdf = "modelo.pdf"  # seu arquivo modelo
saida_dir = "certificados/"  # pasta de saída (crie se não existir)

POSICAO_VERTICAL_NOME_ALUNO = 400 #eixo x
POSICAO_HORIZONTE_NOME_ALUNO = 395 #eixo y
import os
os.makedirs(saida_dir, exist_ok=True)

def gerar_certificado(nome):
    nome_limpo = nome.strip()
    nome_arquivo = os.path.join(saida_dir, f"certificado_{nome_limpo.replace(' ', '_')}.pdf")

    # Cria um PDF temporário com o nome do aluno
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)

    # ---- Ajuste a posição do nome conforme o modelo ----
    # coordenadas (x, y) em pontos, origem é canto inferior esquerdo da página
    can.setFont("Times-Italic", 26)
    can.drawCentredString(POSICAO_VERTICAL_NOME_ALUNO, POSICAO_HORIZONTE_NOME_ALUNO, nome_limpo)
    can.save()

    # Move o ponteiro para o início do buffer
    packet.seek(0)

    # Lê o modelo PDF e o texto temporário
    modelo = PdfReader(modelo_pdf)
    overlay = PdfReader(packet)

    pagina = modelo.pages[0]
    pagina.merge_page(overlay.pages[0])

    # Cria o novo PDF com o nome inserido
    writer = PdfWriter()
    writer.add_page(pagina)

    with open(nome_arquivo, "wb") as f:
        writer.write(f)

    print(f"✅ Certificado gerado: {nome_arquivo}")

# Leitura do CSV
with open(arquivo_csv, mode='r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        nome = linha["Nome do Aluno"]
        gerar_certificado(nome)
