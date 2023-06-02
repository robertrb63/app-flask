from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('name.html')

@app.route('/lenguajes')
def mostrarLenguajes():
    misLenguajes=("PHP", "Python", "Java", "JavaScripot", "Perl", "Ruby", "Rust")
    return render_template('lenguajes.html', lenguajes=misLenguajes)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=False)
