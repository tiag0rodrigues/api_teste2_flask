from flask import Flask, make_response, jsonify, request, redirect, url_for, render_template

Usuario = [
    {'nome': 'Pedro', 'peso': 74}
]

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def index():
    return render_template('index.html', list_users=Usuario)

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['nome']
    weight = request.form['peso']
    
    user = dict()
    user = {'nome': name, 'peso': weight}

    Usuario.append(user)
    
    f = open('usuario.txt', 'a')
    f.write('{}\n'.format(user))
    f.close()
    
    return redirect(url_for('index'))


@app.route('/edit/<rnome>', methods=['POST', 'GET'])
def edit_user(rnome):
    return render_template('edit.html', name=rnome)

@app.route('/update/<rnome>', methods=['POST'])
def update_user(rnome):
    new_name = request.form['nome']            
    new_weight = request.form['peso']     

    contador=0
    for user in Usuario:
        if user['nome']==rnome:
            user_aux = {'nome': new_name, 'peso': new_weight}
            break
        contador = contador+1 

    Usuario[contador] = user_aux
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)