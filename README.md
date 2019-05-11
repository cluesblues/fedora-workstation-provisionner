# Fedora workstation provisionner.

## What's this

This repo contains my Fedora workstation auto provisionner. This install my stuff to dev and other tools.

This version of the software support Fedora 30.

## Development.

### Requirements

- ansible
- vagrant
- VirtualBox

```shell
git clone https://framagit.org/bzhazreal/fedora-workstation-provisionner.git
cd fedora-workstation-provisionner

vagrant up --provider=virtualbox --provision
```

## Production

@TODO.


# Feature:

- role :
    - common
        - Install keepassx, inkscape, git
        - Install rpm fusion free and non free
        - Install telegram native app
        - Install vscodium and some extensions
    - docker
        - Install docker-ce
        - Install docker-compose
        - Add basic traefik docker-compose
        - @TODO : Actually repo file is custom and specify previous fedora release.
    - zsh
        - Install zsh
        - Install oh-my-zsh
        - Install zsh auto suggest extension
    - mailspring
        - Install mailspring from remote url
        - @TODO : manage mailspring config auto installation.
    - @TODO
        - Install backup files
