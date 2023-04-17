import json

with open('data/services.json') as f:
  data = json.load(f)

metrics_prod_ip = []
metrics_test_ip = []
logs_prod_ip = []
logs_test_ip = []
backup_prod_ip = []
backup_test_ip = []
app_prod_ip = []
app_test_ip = []

def vm_scan():
  for i in range(len(data)):
    # Getting Metrics Prod IP
    if data[i]['NodeMeta']['env'] == 'metrics' and data[i]['NodeMeta']['stage'] == 'prod':
      metrics_prod_ip.append(data[i]['Address'])
    # Getting Metrics Test IP
    if data[i]['NodeMeta']['env'] == 'metrics' and data[i]['NodeMeta']['stage'] == 'test':
      metrics_test_ip.append(data[i]['Address'])
    # Getting Logs Prod IP
    if data[i]['NodeMeta']['env'] == 'logs' and data[i]['NodeMeta']['stage'] == 'prod':
      logs_prod_ip.append(data[i]['Address'])
    # Getting Logs Test IP
    if data[i]['NodeMeta']['env'] == 'logs' and data[i]['NodeMeta']['stage'] == 'test':
      logs_test_ip.append(data[i]['Address'])
    # Getting Backup Prod IP
    if data[i]['NodeMeta']['env'] == 'backups' and data[i]['NodeMeta']['stage'] == 'prod':
      backup_prod_ip.append(data[i]['Address'])
    # Getting Backup Test IP
    if data[i]['NodeMeta']['env'] == 'backups' and data[i]['NodeMeta']['stage'] == 'test':
      backup_test_ip.append(data[i]['Address'])
    # Getting App Prod IP
    if data[i]['NodeMeta']['env'] == 'app' and data[i]['NodeMeta']['stage'] == 'prod':
      app_prod_ip.append(data[i]['Address'])
    # Getting App Test IP
    if data[i]['NodeMeta']['env'] == 'app' and data[i]['NodeMeta']['stage'] == 'test':
      app_test_ip.append(data[i]['Address'])
  all_ip = metrics_prod_ip + metrics_test_ip + logs_prod_ip + logs_test_ip + backup_prod_ip + backup_test_ip + app_prod_ip + app_test_ip
  
  return [all_ip, metrics_prod_ip, metrics_test_ip, logs_prod_ip, logs_test_ip, backup_prod_ip, backup_test_ip, app_prod_ip, app_test_ip]
  
  
