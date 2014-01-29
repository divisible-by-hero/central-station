virtualenv-installed:
    cmd.run:
        - name: mkdir -p /home/vagrant/.virtualenvs
        - user: vagrant

virtualenv-exists:
    cmd.run:
        - name: virtualenv /home/vagrant/.virtualenvs/central-station
        - user: vagrant
        - unless: ls -nd /home/vagrant/.virtualenvs | grep -q "central-station"

