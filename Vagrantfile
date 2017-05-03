Vagrant.configure("2") do |config|

	# Virtualbox Base Machine
	config.vm.box = "ubuntu/xenial64" # Ubuntu 16.

	# Forward port 8123 on the VM to port 8123 on the host machine.
	config.vm.network "forwarded_port", guest: 8888, host:8888 

	# Configuring the VM
	config.vm.provider "virtualbox" do |vb|
		vb.memory = "8192"
		# Ubuntu 12 patch.
		# vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
		# vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
	end
	config.vm.provision "shell", :inline => "python3 /vagrant/install_environment.py"
	config.vm.provision "shell", :inline => "python3 /vagrant/init_notebook.py"
end


