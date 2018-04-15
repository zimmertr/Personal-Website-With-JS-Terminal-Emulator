FROM centos:latest

RUN yum install epel-release -y
RUN yum install httpd perl perl-CGI git net-snmp-utils bind-utils -y

RUN git clone https://github.com/zimmertr/Personal-Website-With-JS-Terminal-Emulator.git
RUN cd Personal-Website-With-JS-Terminal-Emulator && cp -r cgi-bin/ /var/www/ && cp -r {index.html,files} /var/www/html/&& cd .. && rm -rf Personal-Website-With-JS-Terminal-Emulator 

RUN echo 'LoadModule cgi_module modules/mod_cgi.so' >> /etc/httpd/conf/httpd.conf

CMD ["-D", "FOREGROUND"]
ENTRYPOINT ["/usr/sbin/httpd"]
