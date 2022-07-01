#!/usr/bin/python

import os

# Instalação do Java
os.system('sudo yum -y update')
os.system('sudo yum -y install java-11-openjdk-devel')
os.system('sudo yum -y install java-11-openjdk')
os.system('sudo wget https://download.oracle.com/java/18/latest/jdk-18_linux-aarch64_bin.rpm')
os.system('sudo localinstall jre-18-linux-x64.rpm')


# Instalação do Apache Zeppelin
os.system('docker run -p 8888:8080 --rm --name zeppelin apache/zeppelin:0.10.1')

# Criação dos usuários

# Usuários admins
os.system('adduser 2rp-guilherme')
os.system('passwd ZCteAb0TMvQkg')
os.system('usermod -a -G sudo 2rp-guilherme')

os.system('sudo adduser 2rp-rene')
os.system('passwd HJndjeSdjeinS')
os.system('usermod -a -G sudo 2rp-rene')

os.system('sudo adduser 2rp-cristiano')
os.system('passwd fenwmiHDSsnDs')
os.system('usermod -a -G sudo 2rp-cristiano')

# Usuários comuns
os.system('adduser 2rp-kevin')
os.system('passwd mDkfekxlDgeFj')

os.system('adduser 2rp-mario')
os.system('passwd ikDmklFklmFkI')

os.system('adduser 2rp-lucas')
os.system('passwd kNBIVuOygyHUg')

os.system('adduser 2rp-ioram')
os.system('passwd UgdbhDYGssgru')

os.system('adduser 2rp-matheus')
os.system('passwd fheuNDsjdheIS')
