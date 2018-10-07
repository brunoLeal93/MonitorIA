from flask import render_template, url_for, redirect, request
from app import app, lm
from flask_login import login_user, current_user
from app.models.Forms import loginForm, listaForm, relForm, sentencaForm, othersconfigForm
from app.models.Collections import User, Lista, Sentenca, Monitorados, othersConfig


@lm.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()


@app.route('/', methods=('GET', 'POST'))
@app.route('/login', methods=('GET', 'POST'))
def login():
    form = loginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            check_user = User.objects.get_or_404(cod_usu=form.cod_func.data)

            if check_user:
                if check_user['senha_usu'] == form.senha_func.data:

                    login_user(check_user)
                    if current_user.is_authenticated:


                        return redirect(url_for('home'))

    return render_template('login.html', form=form)


@app.route('/home', methods=('GET', 'POST'))
def home():
    return render_template('home.html', current_user=current_user)


@app.route('/relatorio', methods=('GET', 'POST'))
def rel():
    form = relForm()
    monitorados = Monitorados.objects()

    return render_template('relatorio.html', form=form, monitorados=monitorados)

@app.route('/Lista', methods=('GET', 'POST'))
def lista():
    form = listaForm()

    listas = Lista.objects()
    if request.method == 'POST':
        if form.validate_on_submit():

            salvaLista = Lista()
            salvaLista.list_desc = form.desc_lista.data
            salvaLista.ptpositivo = form.ptspositivo.data
            salvaLista.ptnegativo = form.ptsnegativo.data
            salvaLista.save()

            print(salvaLista.list_desc)

            return redirect('lista')

    select = request.args.get('x.id')

    print(select)
    return render_template('lista.html', form=form, listas=listas)

@app.route('/Sentenca', methods=('GET', 'POST'))
def sentenca():
    form = sentencaForm()
    listas = Lista.objects()
    sentencas = Sentenca.objects()

    select = request.args.get('lista_selecionada')
    if select != 'None':
        print(select)
        if request.method == 'POST':
            if form.validate_on_submit():
                salvaSent = Sentenca()
                salvaSent.lista = select
                salvaSent.desc_palavra = form.desc_sent.data
                salvaSent.save()


    return render_template('sentenca.html', form=form, listas=listas, sentencas=sentencas)


@app.route('/config', methods=('GET', 'POST'))
def config():
    form=othersconfigForm()
    config = othersConfig.objects()

    for x in config:
        if form.validate_on_submit():
            dir= form.dirAudio.data.replace('\\','/')
            x.update(set__dir_audio=dir)

    return render_template('other_config.html', form=form , config=config)