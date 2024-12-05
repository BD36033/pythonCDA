# from routes.route import route
# from flask import Flask

# if __name__ == '__main__':
   
#     app = Flask(__name__, static_folder='static')
    
#     # Enregistrez les routes ici
#     app.register_blueprint(route)

#     app.run(debug=True)



# app.py
from flask import Flask
from routes.route import route  # Assurez-vous que le chemin est correct

app = Flask(__name__)

# Enregistrer le blueprint
app.register_blueprint(route)

if __name__ == '__main__':
    app.run(debug=True)