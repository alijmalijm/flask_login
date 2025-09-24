from flask import Flask,jsonify, render_template, request, redirect, url_for

app = Flask(__name__)

# کد ورود ثابت
ACCESS_CODE = "123456"
@app.route('/')
def welcome():
    return render_template('welcome.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        code = request.form.get('code')
        if code == ACCESS_CODE:
            return redirect(url_for('secret'))
        else:
            return render_template('login.html', error="کد اشتباه است!")
    return render_template('login.html', error=None)

@app.route('/secret')
def secret():
    return render_template('secret.html')
@app.route("/healthz")
def healthz():
    return jsonify({"status": "ok"}), 200

#app.run(debug=True)
