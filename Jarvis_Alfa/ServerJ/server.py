from flask import Flask, render_template, send_file, redirect, url_for
from flask_bootstrap import Bootstrap
import os
import sys

# Identificar a pasta raiz do projeto
pasta_raiz_projeto = os.path.join("C:\\", "Phantasy", "Alfa", "Jarvis_Alfa")
pasta_raiz_servidor = os.path.join("C:\\", "ServerFox")

# Adicionar a pasta raiz do projeto ao path do sistema
sys.path.append(pasta_raiz_projeto)

app = Flask(__name__, template_folder=os.path.join(pasta_raiz_projeto, 'ServerJ', 'html', 'template'))
Bootstrap(app)

# Caminho para a pasta que o servidor irá compartilhar
pasta_compartilhada = os.path.join(pasta_raiz_servidor)

@app.route('/download/<arquivo>')
def baixar_arquivo(arquivo):
    caminho_completo = os.path.join(pasta_raiz_projeto, 'ServerJ', 'html', 'template', arquivo)
    return send_file(caminho_completo, as_attachment=True)

@app.route('/visualizar/<arquivo>')
def visualizar_arquivo(arquivo):
    caminho_completo = os.path.join(pasta_raiz_projeto, 'ServerJ', 'html', 'template', arquivo)
    try:
        with open(caminho_completo, 'r', encoding='utf-8') as file:
            conteudo = file.read()
        return render_template('tema1.html', arquivo=arquivo, conteudo=conteudo)
    except UnicodeDecodeError:
        return 'Este arquivo não pode ser visualizado.'

@app.route('/executar/<arquivo>')
def executar_arquivo(arquivo):
    caminho_completo = os.path.join(pasta_raiz_projeto, 'ServerJ', 'html', 'template', arquivo)
    try:
        return send_file(caminho_completo, as_attachment=True)
    except Exception as e:
        return str(e)

@app.route('/')
def home():
    caminho_completo = pasta_compartilhada
    
    arquivos = []
    if os.path.isdir(caminho_completo):
        arquivos = os.listdir(caminho_completo)
    
    return render_template('web_index.html', arquivos=arquivos)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
