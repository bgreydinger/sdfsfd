from flask import Flask, render_template
from flask import Flask, url_for, render_template, redirect
from forms import ContactForm

app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('home.html', form=form, template="form-template")

if __name__ == '__main__':
    app.run(debug=True)
