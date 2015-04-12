# Consul-Demo

A little taste of [Consul](consul.io) for configuration management.

## Why

* You need help managing configuration settings
* You want different settings across your environments
* You need to change your configuration as your environment changes
* You don't want to manage env-specific values with your source code

## What

* [Consul](consul.io): Service Discovery and configuration made easy.
* Key/Value Store, Service Registry, Change Notification, DNS Service
* You can use without going "all-in".
* No docker required (but docker friendly).

## How? - Basic Config

* Use environment variables! [Read about them via the 12-factor app](http://12factor.net/config)
* Consul offers key/value store
* Use [envconsul](https://github.com/hashicorp/envconsul) to set env vars for a process 
* Monitors consul, refreshes process

## How? - File Templating

* [consul-template](https://github.com/hashicorp/consul-template) lets you write config files (similar to confd)
* Monitors consul, writes new file
* Optionally will trigger a command, like reloading HAProxy

## Docker Friendly

* [Registrator](https://github.com/gliderlabs/registrator) automatically scans the docker 
  daemon and registered services (also works with etcd)
* [Progrium/docker-consul](https://github.com/progrium/docker-consul) packages consul in a container, with ui.
* Provides a backend for [Swarm Discovery](https://docs.docker.com/swarm/discovery/) (along with etcd/zookeeper).

## Explore This Repo

* An Ubuntu 14.04 Vagrantfile, with a shell provisioner for installing consul and friends
* start-consul-standalone, a helper script to start a standalone server (no clustering required)
* envconsul sample scripts, including a simple python web app
* consul-template sample scripts for an haproxy config file, with health checks

