#!/bin/bash

export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

echo "Hello spark 2!"

# hadoop SSH key
# https://stackoverflow.com/questions/15195048/hadoop-require-roots-password-after-enter-start-all-sh
ssh-keygen -q -t rsa -N '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

/etc/init.d/ssh start

start-master.sh
start-worker.sh spark://0.0.0.0:7077

tail -f /dev/null