from flask import Flask
from configuration import configure_all

# inicializar o Flask
app = Flask(__name__) 

#route
configure_all(app)

#execucao
app.run(debug=True) #modo desenvolvedor 
