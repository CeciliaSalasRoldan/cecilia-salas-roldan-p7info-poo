#Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

#Variáveis principais
aplicação = Flask(__name__)
aplicação.config.from_object('config')
#Banco de dados
datab = SQLAlchemy(aplicação)
migrate = Migrate(aplicação, datab)
#Manager
manager = Manager(aplicação)
manager.add_command('datab', MigrateCommand)