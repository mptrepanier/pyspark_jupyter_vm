This repository contains files necessary for getting a PySpark notebook up and running on a VirtualBox machine. The notebook will be running at localhost:8888.

# QuickStart Guide from Scratch

1) Install VirtualBox for your system: https://www.virtualbox.org/wiki/Downloads
2) Install Vagrant for your system: https://www.vagrantup.com/downloads.html
3) Install Git for your system: https://git-scm.com/downloads
    - Include Git Bash in your installation.
4) Clone this repository to your system.
5) In the Git Bash terminal, navigate to the location where this repo was cloned.
6) Run `vagrant up` at the command line.
    - This will download/install the VM and the relevant software.
7) Once installed, run `vagrant ssh` to ssh into the Vagrant VM.
8) Open your preferred web browser and navigate to localhost:8888.
9) Enjoy your Jupyter Notebook!

# Installation Specs

* Ubuntu 16.04.2
* Spark 2.0.2
* Java 1.8
* Anaconda 2