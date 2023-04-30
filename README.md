# futoshiki

## Purpose

INF401 project

FUTOSHIKI solver

## Run project

Pynecone (python frontend package) need nodejs (v12.22.0+) to work.  
Run the following commande to check if you got it installed :

    node -v

If needed here are the commands to install it (https://www.vultr.com/docs/install-nvm-and-node-js-on-ubuntu-20-04/) :

    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
    source ~/.bashrc
    nvm install node

It's optional but we highly recommand to create a Python virtual environment.  
It will avoid to install packages of this project globally.

    python3 -m pip install virtualenv
    sudo apt install python3.8-venv
    python3 -m venv env && source env/bin/activate

Install all dependencies and run the server :    

    pip install -r requirements.txt && pc run

Then : Using any browser, connect to the localhost server (port 3000 by default) : http://localhost:3000

## Ressources

Docs : https://pynecone.io/docs/getting-started/introduction

Existing project : https://github.com/pynecone-io/pynecone