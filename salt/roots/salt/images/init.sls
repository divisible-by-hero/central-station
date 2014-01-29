image-packages:
  pkg:
    - installed
    - names:
      - zlib1g-dev
      - libfreetype6
      - libfreetype6-dev
      - libgtk2.0-dev
      - libavcodec-dev
      - libavformat-dev
      - libtiff4-dev
      - libswscale-dev
      - libjasper-dev
      - libjpeg-dev
      - libjpeg8-dev
      - libjpeg-turbo8-dev
      - libpng-dev
      - libevent-dev


image-symlink-1:
  cmd.run:
    - name: sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
    - user: vagrant

image-symlink-2:
  cmd.run:
    - name: sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
    - user: vagrant

image-symlink-3:
  cmd.run:
    - name: sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib
    - user: vagrant