FROM centos:latest

RUN yum install cronie git python-setuptools -y 

RUN git clone https://github.com/JackWink/Weather.git
RUN cd Weather && python setup.py install && cd .. && rm -rf Weather

RUN echo "*/5 * * * * /var/www/cgi-bin/getWeather.sh" >> /new_cron; crontab /new_cron; rm /new_cron

CMD ["-D", "FOREGROUND"]
ENTRYPOINT ["/sbin/crond -n"]
