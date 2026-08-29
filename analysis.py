from collections import Counter
log_file = "sample_logs.txt"
failed_ips = []

with open(log_file, "r") as file:
  for line in file:
    if "Failed password" in line:
      ip = line.split("from ")[1].strip()
      failed_ips.append(ip)
      
ip_counts = Counter(failed_ips)

for ip, count in ip_counts.items():
  print(f"{ip}: {count} failed login attempts")
