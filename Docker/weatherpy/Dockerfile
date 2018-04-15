FROM centos:latest

RUN yum install cronie git python-setuptools -y 

RUN git clone https://github.com/JackWink/Weather.git
RUN cd Weather && python setup.py install && cd .. && rm -rf Weather

RUN touch /root/crontab
RUN echo '*/5 * * * * /usr/bin/weatherpy | /usr/bin/head -n -1 > /var/www/cgi-bin/weather.txt 2>&1' > /root/crontab
RUN echo '*/5 * * * * /usr/bin/weatherpy -feat civilian >> /var/www/cgi-bin/weather.txt' > /root/crontab
run echo "*/5 * * * * /usr/bin/echo 'last run at' $date >> /var/www/cgi-bin/weather.txt" > /root/crontab
RUN crontab /root/crontab

CMD ["-n", "FOREGROUND"]
ENTRYPOINT ["/usr/sbin/crond"]
