pkg_dnf = {
    'influxdb': {
        'needs': ['action:dnf_makecache'],
    },
}

svc_systemd = {
    'influxdb': {
        'needs': ['pkg_dnf:influxdb'],
    },
}

files = {
    '/etc/influxdb/influxdb.conf': {
        'mode': '0444',
        'content_type': 'mako',
        'needs': ['pkg_dnf:influxdb'],
        'triggers': ['svc_systemd:influxdb:restart'],
    },
}
