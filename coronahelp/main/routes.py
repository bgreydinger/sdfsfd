from flask import url_for, render_template, redirect, request
from flask import current_app as app
from .forms import *
from .filewriter import *
from .mailserver import *

@app.route('/', methods=('GET', 'POST'))
def home():
    reqform = ReqForm()
    delform = DelForm()
    error = 0
    # if '''click on button''':
    #     return redirect(url_for('cancel'))
    return render_template('home.html',
                           reqform=reqform,
                           delform=delform,
                           errors=error)


@app.route('/req', methods=('GET', 'POST'))
def req():
    reqform = ReqForm()
    delform = DelForm()
    if reqform.validate_on_submit():
        appendfile("req.csv", reqform)
        mail(reqform.name.data, reqform.tel.data, "recipient")
        return redirect(url_for('success'))
    elif request.method == "POST" and not reqform.validate():
        error = 1
    else:
        error = 0
    return render_template('home.html',
                           reqform=reqform,
                           delform=delform,
                           errors = error)


@app.route('/delv', methods=('GET', 'POST'))
def delv():
    reqform = ReqForm()
    delform = DelForm()
    if delform.validate_on_submit():
        appendfile("del.csv", delform)
        mail(delform.name.data, delform.tel.data, "delivery")
        return redirect(url_for('success'))
    elif request.method == "POST" and not delform.validate():
        error = 2
    else:
        error = 0
    return render_template('home.html',
                           reqform=reqform,
                           delform=delform,
                           errors = error)


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/cancel', methods=('GET', 'POST'))
def cancel():
    reqform = ReqForm()
    delform = DelForm()
    error = 0
    return render_template('cancel.html',
                           reqform=reqform,
                           delform=delform,
                           errors=error)
