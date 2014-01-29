solr:
  pkg.installed:
    - names:
      - solr-tomcat

  service.running:
    - enabled: True

schema.xml:
    file.managed:
        - name: /etc/solr/conf/schema.xml
        - source: salt://solr/schema.xml
        - require:
            - pkg: solr-tomcat
