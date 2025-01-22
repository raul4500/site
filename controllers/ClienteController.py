from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import session as cookies_session
from database import*
from repository.__init__ import*
from datetime import*

cliente_controller = Blueprint('cliente_controller', __name__)

clienteRepository = ClienteRepository()

@cliente_controller.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['email']
        senha = request.form['senha']
        if nome=='admin':
            if senha=='admin':
                flash('Cliente criado com sucesso!', 'success')
                cookies_session['usuario_senha'] = senha
                cookies_session['usuario_nome'] = nome
            else:
                return redirect(url_for('cliente_controller.login')) 
        else:
            cookies_session['usuario_senha'] = senha
            cookies_session['usuario_nome'] = nome
        return redirect(url_for('cliente_controller.index'))
    return render_template('login.html')

@cliente_controller.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        nascimento = request.form['nascimento']
        rg = request.form['rg']
        telefone = request.form['telefone']
        senha = request.form['senha']
        #verificar inputs (nome, rg, essas coisas)
        clienteRepository.createCliente(nome, email, nascimento, rg, telefone)

        cookies_session['usuario_senha'] = senha
        cookies_session['usuario_nome'] = nome

        return redirect(url_for('cliente_controller.index'))
    return render_template('cadastrar.html')