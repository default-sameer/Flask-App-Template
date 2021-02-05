from flask import render_template, url_for, request, redirect
from app import app
from app.forms import Users

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = Users()
    if request.method == 'POST':
        form.username.data
        form.email.data
        form.password.data
#        return redirect(url_for('index'))
        return 'Successful login for ' + form.username.data
    return render_template('form.html', form=form, title='Form')


