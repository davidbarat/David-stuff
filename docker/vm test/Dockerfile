FROM repo AS build

WORKDIR /build
RUN pwd

COPY etc/ssh ssh/
RUN CHMOD 640 ssh/ssh_host_ecdsa_key
RUN CHMOD 640 ssh/ssh_host_ed25519_key
RUN CHMOD 640 ssh/ssh_host_rsa_key
RUN CHMOD 640 ssh/ssh_host_ecdsa_key.pub
RUN CHMOD 640 ssh/ssh_host_ed25519_key.pub
RUN CHMOD 640 ssh/ssh_host_rsa_key.pub
RUN groudadd --gid 998 ssh_keys
RUN chgrp ssh_keys ssh/*ssh_host_ecdsa_key

COPY etc/sudoers.d/20-AdminPF sudoers.d/
RUN chmod 440 sudoers.d/20-AdminPF
COPY home/pfadmin/.ssh key/.ssh
RUN chmod 700 key/.ssh
RUN chmod 600 key/.ssh/id_rsa
RUN chmod 600 key/.ssh/authorized_keys
RUN chmod 644 key/.ssh/id_rsa.pub

COPY usr/bin usr/
RUN chmod 755 usr/*

FROM repo
ENV container docker
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *;do [ $i == \
    systemd-tmpfiles-setup.service ] || rm -f $i; done); \
    rm -f /etc/systemd/system/*.wants/*;\
    rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
    rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
    rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
    rm -f /lib/systemd/system/basic.target.wants/*; \
    rm -f /lib/systemd/system/anaconda.target.wants/*; 
VOLUME [ "/sys/fs/cgroup" ]

RUN curl -s http || tar xvf ; /bin/update-ca-trust

RUN yum - y install vim less curl htop openssh-clients sudo openssh-server ksh hostname unzip ;\
    yum clean all ;\
    systemctl enable sshd.service

COPY --from=build --chown=root:ssh_keys /build/ssh/*key /etc/ssh
COPY --from=build --chown=root:root /build/ssh/*.pub /etc/ssh/

RUN groupadd --gid 2005 pfadmin ;\
    groupadd --gid 205 web;\


    ])

COPY --chown=pfadmin:pfadmin --from=build /build/key/ /home/pfadmin

COPY --from=build /build/sudoers.d /etc/sudoers.d

COPY --from=build /build/usr /usr/bin

RUN mkdir /applis; chown pfmgr:pfapp /applis

ADD wlb.tar /apps
ADD web.tar /apps/toolboxes/web/
ADD exploit.tar /apps/toolboxes/exploit/

RUN mkdir /apps/toolboxes/.logs; mkdir /etc/local

EXPOSE 22

CMD ["/usr/sbin/init"]