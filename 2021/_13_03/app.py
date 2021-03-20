from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = '124'

data = [
    None, None, None,
    None, None, None,
    None, None, None,
]

players = ['X', 'O']
ch = 0


def check_win():
    global data
    if data[0] == data[1] == data[2] or data[0] == data[3] == data[6] or data[0] == data[4] == data[8]:
        return data[0]
    if data[2] == data[4] == data[6] or data[2] == data[5] == data[8]:
        return data[2]
    if data[6] == data[7] == data[8] or data[1] == data[4] == data[7]:
        return data[7]
    if data[3] == data[4] == data[5]:
        return data[4]
    return False


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        global ch
        place = int(tuple(dict(request.form).keys())[0]) - 1
        if data[place]:
            return render_template('index.html', data=enumerate(data))
        data[place] = players[ch]
        ch = (ch + 1) % 2
        print(data)
        print(check_win())
    if check_win():
        return render_template('index.html', data=enumerate(data), win=check_win())
    return render_template('index.html', data=enumerate(data))


@app.route('/reset')
def reset():
    global data, ch
    ch = 0
    data = [
        None, None, None,
        None, None, None,
        None, None, None,
    ]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
