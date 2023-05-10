from flask import Flask, render_template, request, jsonify, redirect, url_for


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/tower", methods=['POST', 'GET'])
def tower():
    launch = False
    if request.method == 'POST':
        keyword = request.form['launchjob']
        id_inventory = request.form['id_inventory']
        template_id = request.form['template_id']
        launch = True
        return redirect(url_for('.status', id=str(job_info['job_id'])))
    else:
        return render_template('tower.html')
