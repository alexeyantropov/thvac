# thvac
The Teensy HVAC is a wrapper for the hvac module giving a simpler interface.

# WTF?
I use [hvac](https://github.com/hvac/hvac) in my everyday work and the official client basically provides a lot of bricks for building youown local client for your tasks and evironment. And it's OK.

However I recon there is a little problem and I want to code a tiny client using hvac (not bare Vault API) with a simplier to use interface based on my expirience with Vault and hvac.

# Developing and testing environment
All assets and docs for developing and testing in the 'develop' folder. It uses docker-compose, [the Vault docker image](https://hub.docker.com/_/vault), and [the Python image](https://hub.docker.com/_/python).

It is runned and developed on python 3.9 but I sure that another python version aren't a problem.
