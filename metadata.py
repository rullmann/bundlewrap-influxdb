@metadata_processor
def dnf(metadata):
    if node.has_bundle('dnf'):
        metadata.setdefault('dnf', {})
        metadata['dnf'].setdefault('repositories', {})
        metadata['dnf']['repositories'].setdefault('influxdb', {})
        metadata['dnf']['repositories']['influxdb'].setdefault(
            'name',
            'InfluxDB Repository - RHEL 7',
        )
        metadata['dnf']['repositories']['influxdb'].setdefault(
            'baseurl',
            'https://repos.influxdata.com/rhel/7/x86_64/stable',
        )
        metadata['dnf']['repositories']['influxdb'].setdefault(
            'gpgkey',
            'https://repos.influxdata.com/influxdb.key',
        )
    return metadata, DONE
