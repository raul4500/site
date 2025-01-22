from flask import *
from database import init_db
from controllers.__init__ import *

app = Flask(__name__)
app.register_blueprint(viagem_controller)
app.register_blueprint(cliente_controller)
app.secret_key = '1234566789'
if __name__ == "__main__":
    init_db(app)
    app.run(debug = True)
