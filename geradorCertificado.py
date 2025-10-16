import csv
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from io import BytesIO
import os

arquivo_csv = "presenca.csv"
modelo_pdf = "modelo_certificado.pdf"
saida_dir = "certificados/"
os.makedirs(saida_dir, exist_ok=True)

POSICAO_X_NOME = 480
POSICAO_Y_NOME = 340

def ajustar_tamanho_fonte(can, texto, fonte, tamanho_inicial, largura_maxima):
    can.setFont(fonte, tamanho_inicial)
    while can.stringWidth(texto, fonte, tamanho_inicial) > largura_maxima and tamanho_inicial > 8:
        tamanho_inicial -= 1
    can.setFont(fonte, tamanho_inicial)
    return tamanho_inicial

def gerar_certificado(nome):
    nome_limpo = nome.strip()
    nome_arquivo = os.path.join(saida_dir, f"certificado_{nome_limpo.replace(' ', '_')}.pdf")

    # 📏 Lê o tamanho da página real do modelo
    modelo = PdfReader(modelo_pdf)
    pagina_modelo = modelo.pages[0]
    largura = float(pagina_modelo.mediabox.width)
    altura = float(pagina_modelo.mediabox.height)

    # 🧾 Cria o overlay com o mesmo tamanho do modelo
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=(largura, altura))

    fonte = "Times-Italic"
    tamanho_inicial = 26
    largura_maxima = largura * 0.8  # 80% da largura da página (ajuste como quiser)

    ajustar_tamanho_fonte(can, nome_limpo, fonte, tamanho_inicial, largura_maxima)

    # Centraliza horizontalmente com base na largura real
    x = POSICAO_X_NOME
    y = POSICAO_Y_NOME

    can.drawCentredString(x, y, nome_limpo)
    can.save()

    # Junta o overlay ao modelo
    packet.seek(0)
    overlay = PdfReader(packet)
    pagina_overlay = overlay.pages[0]
    pagina_modelo.merge_page(pagina_overlay)

    writer = PdfWriter()
    writer.add_page(pagina_modelo)

    with open(nome_arquivo, "wb") as f:
        writer.write(f)

    print(f"✅ Certificado gerado: {nome_arquivo}")

# Leitura do CSV
with open(arquivo_csv, mode='r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        nome = linha["Nome do Aluno"]
        gerar_certificado(nome)
