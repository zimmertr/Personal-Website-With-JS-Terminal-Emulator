FROM centos:latest

RUN yum install epel-release -y
RUN yum install httpd cronie perl perl-CGI git python-setuptools net-snmp-utils bind-utils -y

RUN git clone https://github.com/JackWink/Weather.git
RUN git clone https://github.com/zimmertr/Personal-Website-With-JS-Terminal-Emulator.git
RUN cd Weather && python setup.py install && cd .. && rm -rf Weather
RUN cd Personal-Website-With-JS-Terminal-Emulator && cp -r cgi-bin/ /var/www/ && cp -r {index.html,files} /var/www/html/&& cd .. && rm -rf Personal-Website-With-JS-Terminal-Emulator 
RUN echo "*/5 * * * * /var/www/cgi-bin/getWeather.sh" >> /root/existing_cron; crontab /root/existing_cron; rm /root/existing_cron

RUN echo 'LoadModule cgi_module modules/mod_cgi.so' >> /etc/httpd/conf/httpd.conf

RUN touch /startup.sh; echo "/var/www/cgi-bin/getWeather.sh > /dev/null 2>&1" > /startup.sh; echo "/sbin/crond > /dev/null 2>&1" >> /startup.sh; echo "/usr/sbin/httpd" >> /startup.sh
RUN chmod +x /startup.sh

CMD ["-D", "FOREGROUND"]
ENTRYPOINT ["/usr/bin/bash /startup.sh"]
