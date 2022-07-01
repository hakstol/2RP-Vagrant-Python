vagrant init centos/7

vagrant plugin install vagrant-disksize

start Vagrantfile

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
