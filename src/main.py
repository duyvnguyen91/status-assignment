from firewall import *
from vm_scan import *

test_hosts = ['54.169.28.64']

def main():    
  all_ip, metrics_prod_ip, metrics_test_ip, logs_prod_ip, logs_test_ip, backup_prod_ip, backup_test_ip, app_prod_ip, app_test_ip = vm_scan()
  
  # Applying rule for logs.*
  for host in logs_prod_ip:
    firewall.logstash_rule(host)
  for host in logs_test_ip:
    firewall.logstash_rule(host)

  # Applying rule for all host
  for host in all_ip:
    firewall.node_exporter_rule(host, metrics_prod_ip)
    firewall.node_exporter_rule(host, metrics_test_ip)
  
  # Applying rule for app_prod_ip 
  for host in app_prod_ip:
    firewall.mysql_exporter_rule(host, metrics_prod_ip)
    firewall.mysql_exporter_rule(host, metrics_test_ip)
    firewall.database_rule(host, backup_prod_ip)
    firewall.database_rule(host, backup_test_ip)

  # Applying rule for app_test_ip 
  for host in app_test_ip:
    firewall.mysql_exporter_rule(host, metrics_prod_ip)
    firewall.mysql_exporter_rule(host, metrics_test_ip)
    firewall.database_rule(host, backup_prod_ip)
    firewall.database_rule(host, backup_test_ip)

  # for host in test_hosts:
  #   print("Running logstash_rule")
  #   firewall.logstash_rule(host)
  #   print("Running node_exporter_rule")
  #   firewall.node_exporter_rule(host, metrics_prod_ip)
  #   firewall.node_exporter_rule(host, metrics_test_ip)
  #   print("Running mysql_exporter_rule")
  #   firewall.mysql_exporter_rule(host, metrics_prod_ip)
  #   firewall.mysql_exporter_rule(host, metrics_test_ip)
  #   print("Running database_rule")
  #   firewall.database_rule(host, backup_prod_ip)
  #   firewall.database_rule(host, backup_test_ip)
if __name__ == "__main__":
  main()