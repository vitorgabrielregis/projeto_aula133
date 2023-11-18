# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Vitor" # escreva seu nome
    idade = "16" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/pai")
def pai():
    nome_pai = "Lindbergh"
    idade_pai = "45"
    return render_template('pai.html', nome=nome_pai, idade=idade_pai)


# defina a rota para a página da mãe
@app.route("/mae")
def pai():
    nome_pai = "Angélica"
    idade_pai = "45"
    return render_template('mae.html', nome=nome_pai, idade=idade_mae)


# defina a rota para a página do amigo


# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
