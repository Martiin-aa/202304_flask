from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def home():
    session['counter'] = session.get('counter', 0) + 1
    return render_template('base.html', counter=session['counter'])

@app.route('/increment', methods=['POST'])
def increment():
    print(request.form)
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    print(request.form)
    session['counter'] = 0
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
