from flask import Flask
from routes.home import home_route
from routes.cliente import cliente_route

# inicializar o Flask
app = Flask(__name__) 

#rotas
app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix='/clientes')


#execucao
app.run(debug=True) #modo desenvolvedor 
