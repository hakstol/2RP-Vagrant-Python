#!/bin/bash

sudo apt-get -y update

sudo apt-get -y install vagrant

sudo apt-get -y install virtualbox

sudo apt-get -y install vim

mkdir vagrant-python

cd vagrant-python

vagrant init centos/7

vagrant plugin install vagrant-disksize

sudo vim Vagrantfile

# Sobrescrever o arquivo com essa configuração

# Vagrant.configure("2") do |config|

#   config.vm.box = "centos/7"
  
#   config.disksize = "50GB"
  
#   config.vm.network "forwarded_port", guest: 80, host: 8081

#   config.vm.provider "virtualbox" do |vb|
  
# 	  vb.name = "teste-zeppelin"
# 	  vb.cpus = "2"
# 	  vb.memory = "8192"
#   end
  
# end

vagrant up

vagrant ssh




