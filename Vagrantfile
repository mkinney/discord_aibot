# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-22.10"
  config.vm.provision "file", source: "./provision.sh", destination: "/tmp/provision.sh"
  config.vm.provision "file", source: "./.env", destination: "/tmp/.env"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "14336"
    vb.cpus = 4
    vb.customize ["modifyvm", :id, "--chipset", "ich9"]
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get -y install python3.10-venv python3-pip
    useradd -m -s /bin/bash dbots
    sudo -u dbots echo "alias act='source venv/bin/activate'" >> /home/dbots/.bashrc
    sudo su - dbots /tmp/provision.sh
  SHELL
end
