#sample application to demo locust 
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
#renders html output
def home():
    headers = {'Content-Type': 'text/html'}
    return flask.make_response(flask.render_template('index.html'),200,headers)
@app.route('/register',methods=['POST'])
def register():
    name = flask.request.args.get('name','')
    age = flask.request.args.get('age','')
    if name is not '':
       return "Thanks for registering"
    else:
       return "Please enter name and age"
app.run(host='0.0.0.0',port=5000)
