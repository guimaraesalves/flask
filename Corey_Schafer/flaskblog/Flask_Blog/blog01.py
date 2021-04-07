from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Mateus Guimarães Alves',
        'title': 'Projeto 1 - Meu próprio Blog',
        'content': 'Um blog para  o meu portifólio',
        'date_posted': 'Abril 07, 2021'
    },
    {
        'author': 'Mateus Guimarães Alves',
        'title': 'Projeto 2 - Hank-Pessoa',
        'content': 'Um Chatbot para conversar com o Poeta Fernando Pessoa ',
        'date_posted': 'Abril 07, 2021'
    },
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
