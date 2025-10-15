# automacao-certificados
# 🧾 Gerador de Certificados em PDF

Este projeto gera **certificados personalizados em PDF** a partir de um **modelo base (`modelo.pdf`)** e de uma lista de alunos contida em um **arquivo CSV (`presenca.csv`)**.

Para cada aluno, o programa insere o **nome no modelo** e salva o arquivo resultante na pasta `certificados/`.

---

## 🚀 Funcionalidades

- Lê os nomes dos alunos a partir de um arquivo CSV.
- Usa um modelo de certificado em PDF como fundo.
- Insere automaticamente o nome do aluno nas coordenadas configuradas.
- Gera um PDF por aluno com o nome formatado
---

## ⚙️ Instalação e Execução

### 1️⃣ Criar ambiente virtual
```bash
python -m venv venv
source venv/bin/activate     # Linux / Mac
venv\Scripts\activate        # Windows

```
### 2️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 3️⃣ Executar o gerador
```bash
python gerar_certificados.py
```

### Ajuste da Posição do Nome origem é o canto inferior esquerdo da página
```bash
POSICAO_HORIZONTE_NOME_ALUNO = 300
POSICAO_VERTICAL_NOME_ALUNO = 460
```