#!/usr/bin/env python

from subprocess import call, Popen, PIPE

# Java install.
call('apt-get update', shell=True)
call('apt-get install default-jdk -y', shell=True)


# Anaconda download and installation.
call('wget -P /home/anaconda2/ https://repo.continuum.io/archive/Anaconda2-4.3.1-Linux-x86_64.sh', shell=True)
call('bash /home/anaconda2/Anaconda2-4.3.1-Linux-x86_64.sh -b -f -p /home/anaconda2/', shell=True)

# Spark download and installation.
call('wget -P /home http://mirror.fibergrid.in/apache/spark/spark-2.0.2/spark-2.0.2-bin-hadoop2.7.tgz', shell=True)
call('tar -zxvf /home/spark-2.0.2-bin-hadoop2.7.tgz -C /home', shell=True)
call('mv /home/spark-2.0.2-bin-hadoop2.7 /usr/lib/spark', shell=True)

# Setting Environment Variables
call ('cp /usr/lib/spark/conf/spark-env.sh.template /usr/lib/spark/conf/spark-env.sh', shell=True)
with open('/usr/lib/spark/conf/spark-env.sh', 'a') as f:
    f.write('PYSPARK_PYTHON=/home/anaconda2/bin/python' + '\n')

with open('/etc/environment', 'a') as f:
 	f.write('JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/' + '\n' 'SPARK_HOME=/usr/lib/spark' + '\n')

# Creating symbolic links for Spark to we can run its shells from the command line.
call('ln -s /usr/lib/spark/bin/pyspark /usr/local/bin/pyspark', shell=True)
call('chmod ugo+x /usr/local/bin/pyspark', shell=True)

call('ln -s /usr/lib/spark/bin/spark-shell /usr/local/bin/spark-shell', shell=True)
call('chmod ugo+x /usr/local/bin/spark-shell', shell=True)




