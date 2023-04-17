from app.firewall import *
from app.vm_scan import *

def main():    
  all_ip, metrics_prod_ip, metrics_test_ip, logs_prod_ip, logs_test_ip, backup_prod_ip, backup_test_ip, app_prod_ip, app_test_ip = vm_scan()
  
  # Applying rule for logs.*
  for host in logs_prod_ip:
    add_firewall_rule("Allow Logstash", host, ['0.0.0.0/0'], 5141)
  for host in logs_test_ip:
    add_firewall_rule("Allow Logstash", host, ['0.0.0.0/0'], 5141)

  # Applying rule for all host
  for host in all_ip:
    add_firewall_rule("Allow Node Exporter", host, metrics_prod_ip, 9100)
    add_firewall_rule("Allow Node Exporter", host, metrics_test_ip, 9100)
  
  # Applying rule for app_prod_ip 
  for host in app_prod_ip:
    add_firewall_rule("Allow Node Exporter", host, metrics_prod_ip, 9104)
    add_firewall_rule("Allow Node Exporter", host, metrics_test_ip, 9104)
    add_firewall_rule("Allow Node Exporter", host, backup_prod_ip, 3306)
    add_firewall_rule("Allow Node Exporter", host, backup_test_ip, 3306)

  # Applying rule for app_test_ip 
  for host in app_test_ip:
    add_firewall_rule("Allow Node Exporter", host, metrics_prod_ip, 9104)
    add_firewall_rule("Allow Node Exporter", host, metrics_test_ip, 9104)
    add_firewall_rule("Allow Node Exporter", host, backup_prod_ip, 3306)
    add_firewall_rule("Allow Node Exporter", host, backup_test_ip, 3306)

if __name__ == "__main__":
  main()