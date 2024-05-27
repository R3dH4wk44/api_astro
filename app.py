from flask import Flask
from flasgger import Swagger
from controllers.user import user
from controllers.rocketlaunch import launch


app = Flask(__name__)

swagger = Swagger(app)

app.register_blueprint(user)
app.register_blueprint(launch)
app.debug = True


@app.route('/')
def hola():
    return 'Hola'

if __name__ == '__main__':
    app.run(debug = True)