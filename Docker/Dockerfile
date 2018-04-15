FROM centos:latest

RUN yum install epel-release -y
RUN yum install httpd cronie perl perl-CGI git python-setuptools net-snmp-utils bind-utils -y

RUN git clone https://github.com/JackWink/Weather.git
RUN cd Weather && python setup.py install
RUN crond; crontab -l > /root/existing_cron; echo "*/5 * * * * /var/www/cgi-bin/getWeather.sh" >> /root/existing_cron; crontab /root/existing_cron; rm /root/existing_cron
RUN weatherpy > /dev/null

RUN echo 'LoadModule cgi_module modules/mod_cgi.so' >> /etc/httpd/conf/httpd.conf

CMD ["-D", "FOREGROUND"]
ENTRYPOINT ["/usr/sbin/httpd"]
