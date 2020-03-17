from flask import render_template

@app.route('/')
@app.route('/sensehat')
def sensehat():
    return render_template('sensehat.html')

if __name__  == "__main__":
	app.run(host="10.120.145.36",port="8000", debug=True)