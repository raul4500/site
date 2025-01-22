from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import session as cookies_session
from database import*
from repository.__init__ import*
from datetime import*

viagem_controller = Blueprint('viagem_controller', __name__)

viagemRepository = ViagemRepository()
pagamentoRepository = PagamentoRepository()
reservaRepository = ReservaRepository()

@viagem_controller.route('/')
def index():
    viagens = viagemRepository.getAllViagens()
    usuario = cookies_session.get('usuario_nome')
    return render_template('index.html', viagens=viagens, usuario=usuario)

@viagem_controller.route('/logout')
def logout():
    cookies_session['usuario_senha'] = None
    cookies_session['usuario_nome'] = None
    return redirect(url_for('controller.index'))

#@viagem_controller.route('/cadastrar/<id>', methods=['GET', 'POST'])
#def cadastrar(id):
#    if id=='1':
#        url = '/cadastrar/1'
#        if request.method == 'POST':
#            nome = request.form['nome']
#            email = request.form['email']
#            telefone = request.form['telefone']
#            clienteRepository.createCliente(nome, email, telefone)
#            return redirect(url_for('controller.mostrar_clientes'))
#        return render_template('cadastrar_cliente.html', url=url)
#    elif id=='2':
#        url = '/cadastrar/2'
#        if request.method == 'POST':
#            destino = request.form['destino']
#            data_inicio = request.form['data_inicio']
#            data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d').date()
#            data_fim = request.form['data_fim']
#            data_fim = datetime.strptime(data_fim, '%Y-%m-%d').date()
#            preco = request.form['preco']
#            viagemRepository.createViagem(destino, data_inicio, data_fim, preco)
#            return redirect(url_for('controller.index'))
#        return render_template('cadastrar_viagem.html', url=url)
#
#@viagem_controller.route('/clientes')
#def mostrar_clientes():
#    clientes = clienteRepository.getAllClientes()
#    return render_template('clientes.html', clientes=clientes)
#
#@viagem_controller.route('/clientes/editar/<int:id>', methods=['GET', 'POST'])
#def editar_cliente(id):
#    if request.method == 'POST':
#        nome = request.form['nome']
#        email = request.form['email']
#        telefone = request.form['telefone']
#        clienteRepository.updateCliente(id, nome, email, telefone)
#        flash('Cliente atualizado com sucesso!', 'success')
#        return redirect(url_for('controller.mostrar_clientes'))
#    return render_template('cadastrar_cliente.html', url=f'/clientes/editar/{id}')
#
#@viagem_controller.route('/clientes/deletar/<int:id>', methods=['GET','POST'])
#def deletar_cliente(id):
#    clienteRepository.deleteCliente(id)
#    flash('Cliente deletado com sucesso!', 'success')
#    return redirect(url_for('controller.mostrar_clientes'))

@viagem_controller.route('/editar/viagem/<int:id>', methods=['GET', 'POST'])
def editar_viagem(id):
    url = f'/editar/viagem/{id}'
    if request.method == 'POST':
        destino = request.form['destino']
        data_inicio = request.form['data_inicio']
        data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d').date()
        data_fim = request.form['data_fim']
        data_fim = datetime.strptime(data_fim, '%Y-%m-%d').date()
        preco = request.form['preco']
        viagemRepository.updateViagem(id, destino, data_inicio, data_fim, preco)
        return redirect(url_for('controller.index'))
    return render_template('cadastrar_viagem.html', url=url)

@viagem_controller.route('/deletar/viagem/<int:id>')
def deletar_viagem(id):
    viagemRepository.deleteViagem(id)
    flash('Viagem deletada com sucesso!', 'success')
    return redirect(url_for('controller.index'))

#@viagem_controller.route('/reserva/<int:id>', methods=['GET', 'POST'])
#def nova_reserva(id):
#    url = f'/reserva/{id}'
#    if request.method == 'POST':
#        cliente_id = request.form.get('clientes')
#        viagem_id = request.form.get('viagens')
#        reservaRepository.createReserva(str(cliente_id), str(viagem_id))
#        flash('Reserva criada com sucesso!', 'success')
#        return render_template('pagamento.html', url=id)
#    clientes = clienteRepository.getAllClientes()
#    viagens = viagemRepository.getAllViagens()
#    return render_template('reserva.html', clientes=clientes, viagens=viagens, url=url)

@viagem_controller.route('/reservas/deletar/<int:id>', methods=['POST'])
def deletar_reserva(id):
    reservaRepository.deleteReserva(id)
    flash('Reserva deletada com sucesso!', 'success')
    return redirect(url_for('controller.index'))

@viagem_controller.route('/registrar_pagamento/<int:id>', methods=['GET', 'POST'])
def novo_pagamento(id):
    if request.method == 'POST':
        valor = request.form['valor']
        data_pagamento = request.form['data_pagamento']
        data_pagamento = datetime.strptime(data_pagamento, '%Y-%m-%d').date()
        pagamentoRepository.createPagamento(id , data_pagamento, valor, status='Confirmado')
        flash('Pagamento registrado com sucesso!', 'success')
        return redirect(url_for('controller.index'))
    return render_template('pagamento.html', url=id)

@viagem_controller.route('/pagamentos/deletar/<int:id>', methods=['GET', 'POST'])
def deletar_pagamento(id):
    pagamentoRepository.deletePagamento(id)
    flash('Pagamento deletado com sucesso!', 'success')
    return redirect(url_for('controller.index'))
