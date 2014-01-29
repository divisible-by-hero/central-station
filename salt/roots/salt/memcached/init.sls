memcached:
    pkg.installed:
        - name: memcached
    file.managed:
        - name: /etc/memcached.conf
        - source: salt://memcached/memcached.conf
    service.running:
        - watch:
            - file: /etc/memcached.conf


python-memcache:
    pkg.installed:
        - name: python-memcache
    require:
        - pkg: memcached

libmemcached:
    pkg.installed:
        - name: libmemcached-dev
    require:
        - pkg: memcached