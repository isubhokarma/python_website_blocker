import time
from datetime import datetime as dtx

host_paths=r"C:\nWindows\System32\drivers\etc\hosts"
# 1.link to hosts file on windows to block websites
#2.to make the address with "\" a single entity
redirect="127.0.0.1"
#any false ip
website_list=["www.google.com", "www.googoel.co.in", "google.com", "google.co.in"]
#websites to block

while True:
	if dtx(dtx.now().year, dtx.now().month, dtx.now().day, 7) < dtx.now() < dtx(dtx.now().year, dtx.now().month, dtx.now().day, 18):
		print("working hours")
	else:
		print("Off hours")