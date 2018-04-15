FROM centos:latest

RUN yum install cronie git python-setuptools -y 

RUN git clone https://github.com/JackWink/Weather.git
RUN cd Weather && python setup.py install && cd .. && rm -rf Weather

RUN crontab /root/crontab

CMD ["-D", "FOREGROUND"]
ENTRYPOINT ["/usr/sbin/crond"]
