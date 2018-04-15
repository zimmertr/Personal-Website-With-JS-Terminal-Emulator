FROM centos:latest

RUN yum install cronie git python-setuptools -y 

RUN git clone https://github.com/JackWink/Weather.git
RUN cd Weather && python setup.py install && cd .. && rm -rf Weather

RUN touch /root/{crontab,weather_updator.sh}
RUN chmod +x /root/weather_updator.sh
RUN echo '#!/bin/bash' > /root/weather_updator.sh
RUN echo 'date=$(date)' >> /root/weather_updator.sh
RUN echo '/usr/bin/weatherpy | /usr/bin/head -n -1 > /root/weather.txt 2>&1' >> /root/weather_updator.sh
RUN echo '/usr/bin/weatherpy -feat civilian >> /root/weather.txt' >> /root/weather_updator.sh
RUN echo "echo 'Last updated:' \$date >> /root/weather.txt" >> /root/weather_updator.sh

RUN echo "*/3 * * * * /root/weather_updator.sh" >> /root/crontab
RUN crontab /root/crontab

RUN touch /root/weather.txt

CMD ["-n"]
ENTRYPOINT ["/usr/sbin/crond"]
