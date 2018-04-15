FROM centos:latest

RUN yum install cronie git python-setuptools -y 

RUN git clone https://github.com/JackWink/Weather.git
RUN cd Weather && python setup.py install && cd .. && rm -rf Weather

RUN touch /root/{crontab,date_updator.sh}
RUN chmod +x /root/date_updator.sh
RUN echo '#!/bin/bash' > /root/date_updator.sh
RUN echo 'date=$(date)' >> /root/date_updator.sh
RUN echo 'last run at ' $date >> /root/weather.txt

RUN echo '*/5 * * * * /usr/bin/weatherpy | /usr/bin/head -n -1 > /root/weather.txt 2>&1' > /root/crontab
RUN echo '*/5 * * * * /usr/bin/weatherpy -feat civilian >> /root/weather.txt' >> /root/crontab
RUN echo "*/5 * * * * /root/date_updator.sh" >> /root/crontab

RUN crontab /root/crontab

CMD ["-n"]
ENTRYPOINT ["/usr/sbin/crond"]
