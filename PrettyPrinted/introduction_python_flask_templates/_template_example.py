from flask import Flask, render_template
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    names = {'name' : 'Cursos'}
    items = [{'text': 'Python'}, {'text': 'JavaScript'}, {'text': 'Django'}]
    return render_template("layout.html", names=names, lanuage='Python', lang=False, framework='Flask', items=items)



if __name__=="__main__":
    app.run(debug=True)
