FROM centos:latest

RUN yum install epel-release -y
RUN yum install httpd cronie perl perl-CGI git python-setuptools net-snmp-utils bind-utils -y

RUN git clone https://github.com/JackWink/Weather.git
RUN git clone https://github.com/zimmertr/Personal-Website-With-JS-Terminal-Emulator.git
RUN cd Weather && python setup.py install && cd .. && rm -rf Weather
RUN cd Personal-Website-With-JS-Terminal-Emulator && cp -r cgi-bin/ /var/www/ && cp -r {index.html,files} /var/www/html/&& cd .. && rm -rf Personal-Website-With-JS-Terminal-Emulator 
RUN echo "*/5 * * * * /var/www/cgi-bin/getWeather.sh" >> /root/existing_cron; crontab /root/existing_cron; rm /root/existing_cron
RUN /var/www/cgi-bin/getWeather.sh
RUN crond

RUN echo 'LoadModule cgi_module modules/mod_cgi.so' >> /etc/httpd/conf/httpd.conf

CMD ["-D", "FOREGROUND"]
ENTRYPOINT ["/usr/sbin/httpd"]
