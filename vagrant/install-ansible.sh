#!/usr/bin/env bash

# Check if ansible is installed on the vagrant box first
if [ $(dpkg-query -W -f='${Status}' ansible 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
	export DEBIAN_FRONTEND=noninteractive
	echo "Adding Ansible PPA"
    apt-add-repository ppa:ansible/ansible &> /dev/null || exit 1
    echo "Ansible PPA installed"

    echo "Updating APT"
    apt-get update -qq &> /dev/null || exit 1
    echo "APT Updated"

    echo "Installing Ansible"
    apt-get install -qq ansible &> /dev/null || exit 1
    echo "Ansible installed"
fi
