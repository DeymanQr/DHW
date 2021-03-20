from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    # return "Hello, <b>world</b>!"
    return render_template('index.html', title='Main')


@app.route('/get_all_notes')
def get_notes():
    with open('db.txt', 'r', encoding='UTF-8') as f:
        notes = [i.strip() for i in f.readlines()]
        if request.args.get('part_of_note'):
            notes = [i.strip() for i in notes if request.args.get('part_of_note').lower() in i.lower()]
        return render_template('notes.html', notes=notes, title='Notes list')


@app.route('/find_note/<part_of_note>')
def find_note(part_of_note):
    with open('db.txt', 'r', encoding='UTF-8') as f:
        notes = [i.strip() for i in f.readlines() if part_of_note.lower() in i.lower()]
        return render_template('notes.html', notes=notes, title='Notes list')


@app.route('/add_note/<note>')
def add_note(note):
    try:
        with open('db.txt', 'a', encoding='UTF-8') as f:
            f.write(note+'\n')
            return 'Note added successfully'
    except Exception as e:
        return f'Error: {e}'


if __name__ == '__main__':
    app.run(debug=True)