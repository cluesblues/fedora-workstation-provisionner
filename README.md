# Fedora workstation provisionner.

![](https://github.com/bzhazreal/fedora-workstation-provisionner/workflows/build/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## What's this

This repo contains my Fedora workstation auto provisionner. This install my stuff to dev and other tools.

This version of the software support Fedora 33.

## How it works

### Requirements

- [ansible](https://www.ansible.com/)

### Production commands

```shell
###
#
# Execute the provisionner
#
###
git clone https://github.com/bzhazreal/fedora-workstation-provisionner.git
cd fedora-workstation-provisionner
sudo dnf install ansible
ansible-playbook playbook.yml --extra-vars="ansible_become_pass=<YOUR PASSWORD> username=<YOUR USERNAME>"

###
#
# Execute only one tag
#
###
ansible-playbook playbook.yml --extra-vars="ansible_become_pass=<YOUR PASSWORD> username=<YOUR USERNAME>" --tags <tag_name>
```

### Development setup

Use fedora virtual machine with production command.

Use the dockerfile

```shell
###
#
# Build the container
#
###
docker build -t fedora-workstation-test .

###
#
# Remove container after build
#
###
docker rmi fedora-workstation-test
```