from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    myList = [293, 374, 943, 518, 192]
    moreNumbers = [83398, 28739, 84379, 48983223, 298423, 47855, 3940843, 23483]
    evenMoreNumbers = [192, 392332334585484]
    return render_template('index.html', name='Guimarães', numbers=myList, moreNumbers=moreNumbers, evenMoreNumbers=evenMoreNumbers)

if __name__ == '__main__':
    app.run(debug=True)
