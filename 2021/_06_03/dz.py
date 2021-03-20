from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = '124'
statuses = ['Very bad', 'Bad', 'Good', 'Too good to be a human!']


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = dict(request.form)
        if not data['weight'] or not data['height'] or not data['width']:
                flash('Not all arguments', category='error')
                return render_template('index.html')
        answer = int(data['width']) + int(data['height']) + int(data['weight'])
        status = statuses[answer%4]
        return render_template('index.html', answer=answer, status=status)
    return render_template('index.html')


@app.errorhandler(404)
def error(e):
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
