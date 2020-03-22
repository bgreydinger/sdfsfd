from flask import url_for, render_template, redirect, request
from flask import current_app as app
from .forms import ContactForm

# @app.route('/', methods=('GET', 'POST'))
# def home():
#     form = ContactForm()
#     if form.validate_on_submit():
#         return redirect(url_for('success'))
#     return render_template('home.html',
#                            form=form)
#
#
# @app.route('/success', methods=('GET', 'POST'))
# def success():
#     return render_template('success.html',
#                            template='success-template')

@app.route('/', methods=('GET', 'POST'))
def home():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    elif request.method == "POST" and not form.validate():
        error = 1
    else:
        error = 0
    return render_template('home.html',
                           form=form,
                           errors = error)


@app.route('/success')
def success():
    return render_template('success.html')
