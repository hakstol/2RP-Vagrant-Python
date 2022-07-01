#!/usr/bin/python

import os

# Instalação Python 3.6
os.system('sudo yum install -y python36u python36u-libs python36u-devel python36u-pip')

# Instalação Superset
os.system('pip install apache-superset')
# Criar um usuário
os.system('superset fab create-admin')
# Criar um Banco de Dados
os.system('superset db upgrade')
# Dados de exemplo
os.system('superset load_examples')
# Inicializar regras e permissões
os.system('superset init')
# Subir o Apache Superset
os.system('superset run -p 8088 --with-threads --reload --debugger')


#  Instalação MySQL
os.system('sudo yum install mysql mysql-server -y')
# Iniciar o serviço
os.system('systemctl start mysqld')
# Conexão com Superset
os.system('sudo mysql://supersetuser:superset@localhost:8088/apache_superset')

# Instalação Redis
os.system('yum -y install redis')
# Iniciar o serviço
os.system('systemctl start redis')

