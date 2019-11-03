# Fedora workstation provisionner.

## What's this

This repo contains my Fedora workstation auto provisionner. This install my stuff to dev and other tools.

This version of the software support Fedora 30.

## Development.

### Requirements

- ansible
- vagrant

```shell
@TODO
```

## Production

- ansible

```shell
@TODO
```

# Feature:

- role :
    - common
        - Install keepassx, inkscape, git
        - Install rpm fusion free and non free
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
