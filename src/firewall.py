import paramiko
import logging
import traceback
import time
import datetime

log = logging.getLogger()
log.setLevel(logging.INFO)

key = paramiko.RSAKey.from_private_key_file("/Users/duyvnguyen/.ssh/duynv-test.pem")
now = datetime.datetime.now()
username = "ec2-user"
# logstash_rule = 'sudo iptables -A INPUT -p tcp --dport 5141 -j ACCEPT'
# node_exporter_rule = "sudo iptables -A INPUT -s {} -p tcp --dport 9100 -j ACCEPT".format(metrics_hosts)
# mysql_exporter_rule = "sudo iptables -A INPUT -s {} -p tcp --dport 9104 -j ACCEPT".format(metrics_hosts)
# database_rule = "sudo iptables -A INPUT -s {} -p tcp --dport 3306 -j ACCEPT".format(backup_hosts)

class firewall:
  def logstash_rule(host):
    rule = "sudo iptables -A INPUT -p tcp --dport 5141 -j ACCEPT"
    try:
      ssh_client = paramiko.SSHClient()
      ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      
      print("Connecting to server %s" % host)
      ssh_client.connect(host, username=username, pkey=key)
      print("Successfully connected to server %s." % host)
      chan = ssh_client.invoke_shell()
      time.sleep(2)

      if not chan.send_ready():
          raise("Channel not ready!")

      sleep_time = 2
      chan.send(rule+"\n")
      print("%s is running. Sleep for %d seconds!" % (rule, sleep_time))
      time.sleep(sleep_time)

      print("Host %s was exported Successfully!" % host)
      chan.send('quit\n')
      ssh_client.close()
      
    except:
      print("Can't connect to %s" % host)
      traceback.print_exc()
      print("Thread exit!\n")
      return
    
  def node_exporter_rule(host, dest_hosts):
    str_dest_host = ','.join(dest_hosts)
    rule = "sudo iptables -A INPUT -s {} -p tcp --dport 9100 -j ACCEPT".format(str_dest_host)
    try:
      ssh_client = paramiko.SSHClient()
      ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      
      print("Connecting to server %s" % host)
      ssh_client.connect(host, username=username, pkey=key)
      print("Successfully connected to server %s." % host)
      chan = ssh_client.invoke_shell()
      time.sleep(2)

      if not chan.send_ready():
          raise("Channel not ready!")

      sleep_time = 2
      chan.send(rule+"\n")
      print("%s is running. Sleep for %d seconds!" % (rule, sleep_time))
      time.sleep(sleep_time)

      print("Host %s was exported Successfully!" % host)
      chan.send('quit\n')
      ssh_client.close()
      
    except:
      print("Can't connect to %s" % host)
      traceback.print_exc()
      print("Thread exit!\n")
      return

  def mysql_exporter_rule(host, dest_hosts):
    str_dest_host = ','.join(dest_hosts)
    rule = "sudo iptables -A INPUT -s {} -p tcp --dport 9104 -j ACCEPT".format(str_dest_host)
    try:
      ssh_client = paramiko.SSHClient()
      ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      
      print("Connecting to server %s" % host)
      ssh_client.connect(host, username=username, pkey=key)
      print("Successfully connected to server %s." % host)
      chan = ssh_client.invoke_shell()
      time.sleep(2)

      if not chan.send_ready():
          raise("Channel not ready!")

      sleep_time = 2
      chan.send(rule+"\n")
      print("%s is running. Sleep for %d seconds!" % (rule, sleep_time))
      time.sleep(sleep_time)

      print("Host %s was exported Successfully!" % host)
      chan.send('quit\n')
      ssh_client.close()
      
    except:
      print("Can't connect to %s" % host)
      traceback.print_exc()
      print("Thread exit!\n")
      return
    
  def database_rule(host, dest_hosts):
    str_dest_host = ','.join(dest_hosts)
    rule = "sudo iptables -A INPUT -s {} -p tcp --dport 3306 -j ACCEPT".format(str_dest_host)
    try:
      ssh_client = paramiko.SSHClient()
      ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      
      print("Connecting to server %s" % host)
      ssh_client.connect(host, username=username, pkey=key)
      print("Successfully connected to server %s." % host)
      chan = ssh_client.invoke_shell()
      time.sleep(2)

      if not chan.send_ready():
          raise("Channel not ready!")

      sleep_time = 2
      chan.send(rule+"\n")
      print("%s is running. Sleep for %d seconds!" % (rule, sleep_time))
      time.sleep(sleep_time)

      print("Host %s was exported Successfully!" % host)
      chan.send('quit\n')
      ssh_client.close()
      
    except:
      print("Can't connect to %s" % host)
      traceback.print_exc()
      print("Thread exit!\n")
      return