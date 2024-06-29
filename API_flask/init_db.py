from app import app,db # cria o banco de dados
#db.create_all() 
with app.app_context(): #pega o que foi definido antes, os modelos, com isso cria no banco
    db.create_all()
