# influxdb

This bundle will install [influxdb](https://www.influxdata.com/time-series-platform/influxdb/) as part of the TICK stack.

A manual setup may be required beforehands.
A good start to create your first user can be [this guide](https://www.digitalocean.com/community/tutorials/how-to-monitor-system-metrics-with-the-tick-stack-on-centos-7).

## Requirements

* Bundles:
  * [dnf](https://github.com/rullmann/bundlewrap-dnf)

## Setup notes

Set-up a username and password within influxdb before connecting other services.
To do so assign this bundle to a node and set `http_auth_enabled` to False before the initial apply.

## Integrations

* Bundles:
  * [telegraf](https://github.com/rullmann/bundlewrap-telegraf)

## Metadata

    'metadata': {
        'influxdb': {
            'http_auth_enabled': True, # optional, can be changed to False while setting up influxdb
        },
    }
