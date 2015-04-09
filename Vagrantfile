# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

$script = <<SCRIPT
  apt-get install -y unzip python-pip haproxy
  pip install web.py
  mkdir -p /var/consul
  chown vagrant:vagrant /var/consul

  wget -q --no-check-certificate -O /tmp/envconsul.tar.gz https://github.com/hashicorp/envconsul/releases/download/v0.5.0/envconsul_0.5.0_linux_amd64.tar.gz  && tar -xzvf /tmp/envconsul.tar.gz -C /usr/local/bin/ --strip-components=1

  wget -q --no-check-certificate -O /tmp/consul.zip https://dl.bintray.com/mitchellh/consul/0.5.0_linux_amd64.zip  && unzip /tmp/consul.zip -d /usr/local/bin/

  wget -q --no-check-certificate -O /tmp/consul-ui.zip https://dl.bintray.com/mitchellh/consul/0.5.0_web_ui.zip  && unzip /tmp/consul-ui.zip -d /opt/consul-ui/

  wget -q --no-check-certificate -O /tmp/consul-template.tar.gz https://github.com/hashicorp/consul-template/releases/download/v0.8.0/consul-template_0.8.0_linux_amd64.tar.gz  && tar -xzvf /tmp/consul-template.tar.gz -C /usr/local/bin/ --strip-components=1

  rm -rf /tmp/*

  echo '127.0.0.1 web.foobar.com\n' >> /etc/hosts
  echo '127.0.0.1 woot.foobar.com\n' >> /etc/hosts
SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.network :private_network, ip: "192.168.42.13"
  config.vm.provision "shell", inline: $script
  config.vm.hostname = "consul-demo"

  config.vm.provider "virtualbox" do |v|
    v.memory = 4096
    v.cpus = 2
  end
end
