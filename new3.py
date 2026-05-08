# IMPORTING

from flask import Flask, render_template, request

# INTERACTION
app = Flask(__name__)


# MAPPING
@app.route('/')
@app.route('/register')
# INPUTS
def homepages():
    return render_template('register.html')


#MAPPING
@app.route('/confirmation', methods=['POST', 'GET'])
#INPUTS
def register():
    if request.method == 'POST':
        n = request.form.get('name')
        c = request.form.get('city')
        p = request.form.get('phone_number')
        return render_template('confirm.html', name=n, city=c, phone_number=p)
    return None


# MAIN
if __name__ == '__main__':
    app.run(debug=True)
