# Fedora workstation provisionner.

## What's this

This repo contains my Fedora workstation auto provisionner. This install my stuff to dev and other tools.

This version of the software support Fedora 33.

## How it works

### Requirements

- [ansible](https://www.ansible.com/)

### Commands

```shell
git clone https://github.com/bzhazreal/fedora-workstation-provisionner.git
cd fedora-workstation-provisionner
sudo dnf install ansible
ansible-playbook playbook.yml --extra-vars="ansible_become_pass=<YOUR PASSWORD> username=<YOUR USERNAME>"
```

