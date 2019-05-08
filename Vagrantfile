# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "generic/fedora30"

  config.vm.box_check_update = false
  config.vm.network "private_network", ip: "192.168.33.10"

  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "4096"
  end

  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.install_mode = "pip"
    ansible.version = "2.2.1.0"
  end

end
