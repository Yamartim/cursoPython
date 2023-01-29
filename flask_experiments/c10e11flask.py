from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'amogussusimpostorbaka' # chave de encriptação dos cookies para segurança do usuario, se nao tiver isso nao da pra usar o obj session

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Hack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista = [jogo1, jogo2, jogo3]


usuario1 = Usuario("Martim Lima", "Yama", "gameing")
usuario2 = Usuario("Philips Brigles", "Burguer", "amogus")
usuario3 = Usuario("Gomez Aki", "Luvas", "natural20")

usuarios = { usuario1.nickname : usuario1,
             usuario2.nickname : usuario2,
             usuario3.nickname : usuario3 }

# a rota define a pagina que vai ser feita
@app.route('/')
def pgprincipal():
    # podemos executar qualqyuer codigo python na função... 
    # e no final chamamos render_template pra criar a pagina

    # passamos variaveis pro template e fazemos elas aparecerem no html
    return render_template('testeflask.html.j2', titulo='Jogos', jogos=lista)

@app.route('/create') # assim a rota <endereço>/create tera a pagina do formulario
def pgcreate():

    not_logged_in = 'usuario_logado' not in session or session['usuario_logado'] is None
    # se nao tem um usuario gravado no dict da sessao ou tem mas é none pq foi deslogado

    if not_logged_in:
        # se o usuario tentar dar create sem estar logado, manda ele pra pagina de login mas armazena que ele tava nessa pagina pra mandar ele pra ca logo depois
        return redirect(url_for('pglogin', proxima=url_for('pgcreate')))
        # no redirect podemos botar a string da rota da pagina direto ou obter ela pelo url_for com o nome da função
        # url_for é boa pratica porque podemos mudar os urls do site a vontade e os links vao ficar atrelados as funções em si
    
    return render_template('testeflaskform.html.j2', titulo='Novo Jogo')

@app.route('/cr', methods=['POST',]) # definir methods pro python receber informações do formulario da pagina
def cr():

    # por meio do objeto request do flask podemos acessar o dict form e pegar os dados dos formularios pelos nomes definidos nas tags html
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria, console)

    lista.append(jogo) # criamos um novo objeto jogo e adicionamos a lista e voltamos pra pagina principal
    return redirect(url_for('pgprincipal')) # redirect ao inves de renderizar uma pagina nova com atributos indesejados da função cr manda o usuario pra uma rota ja definida



@app.route('/login')
def pglogin():
    proxima = request.args.get('proxima') 
    # pegando a pagina anterior pelo querystring da url e passando pra proxima pagina pro usuario continuar a navegação de onde parou
    return render_template('login.html', proxima = proxima)

@app.route('/autenticar', methods=['POST', ])
def autenticar():

    login_usr = request.form['usuario']
    login_pass = request.form['senha']

    usuario_cadastrado = login_usr in usuarios # confere se o usuario existe
    senha_correta = login_pass == usuarios[login_usr].senha # confere se a senha bate

    if usuario_cadastrado and senha_correta:
        usr = usuarios[login_usr]
        session['usuario_logado'] = usr.nickname # se acertar guardamos o nome do usuario na session (cookies) pra saber q esta logado
        flash(usr.nickname + ' logou com sucesso!') # flash manda uma mensagem pra pagina que podemos capturar no jira2 e mostrar pro usuario
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina) # como esta logado, manda de volta pra home
    else:
        flash('Usuário não logado.') # mostra mensagem que nao logou
        return redirect(url_for('pglogin')) # manda de volta pra tela de login



@app.route('/logout')
def logout():
    session['usuario_logado'] = None # tirando esse elemento do dict pra limpar
    flash('Logout efetuado com sucesso!') # mandando mensagem pro usuario
    return redirect(url_for('pgprincipal')) # voltando pra home

# essa função roda o aplicativo web
# o parametro opcional debug=True faz com que o app detecte mudanças no arquivo python assim podemos testar dinamicamente
app.run(debug=True)