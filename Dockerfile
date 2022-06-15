FROM ubuntu:18.04

# https://phoenixnap.com/kb/install-spark-on-ubuntu
# https://sparkbyexamples.com/spark/spark-installation-on-linux-ubuntu/
# https://sparkbyexamples.com/spark/spark-web-ui-understanding/

RUN apt update

RUN apt install default-jdk scala git -y
RUN apt install python3 -y
RUN java -version; javac -version; scala -version; git --version
RUN apt install wget
RUN apt install nano

RUN apt-get install -y openssh-server
RUN /etc/init.d/ssh start

#update again for pip
RUN apt update

RUN apt-get install python3-pip -y

RUN pip3 install pandas
RUN pip3 install numpy

# RUN wget https://downloads.apache.org/spark/spark-3.0.1/spark-3.0.1-bin-hadoop2.7.tgz
RUN wget https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz

RUN tar xvf spark-*

RUN mv spark-3.2.1-bin-hadoop3.2 /opt/spark

ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
ENV PYSPARK_PYTHON=/usr/bin/python3

COPY entrypoint.sh /usr/local/bin
# ENTRYPOINT ["entrypoint.sh"]
