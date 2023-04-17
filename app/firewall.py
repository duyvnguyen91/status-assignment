import paramiko
import traceback
import time
import datetime

key = paramiko.RSAKey.from_private_key_file("/Users/duyvnguyen/.ssh/duynv-test.pem")
now = datetime.datetime.now()
username = "ec2-user"

def add_firewall_rule(comment, host, src_hosts, port):
  str_src_hosts = ','.join(src_hosts)
  check_rule = "sudo iptables -C INPUT -s {} -p tcp --dport {} -j ACCEPT".format(str_src_hosts, port) + " -m comment --comment " + '"' + comment + '"' + "||"
  rule = "sudo iptables -A INPUT -s {} -p tcp --dport {} -j ACCEPT".format(str_src_hosts, port) + " -m comment --comment " + '"' + comment + '"'
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
    chan.send(check_rule+rule+"\n")
    print("%s is running. Sleep for %d seconds!" % (comment, sleep_time))
    time.sleep(sleep_time)

    print("Host %s was exported Successfully!" % host)
    chan.send('quit\n')
    ssh_client.close()
    
  except:
    print("Can't connect to %s" % host)
    traceback.print_exc()
    print("Thread exit!\n")
    return