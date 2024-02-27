import speedtest
net_speed = speedtest.Speedtest()
# Step 1 - Get list of server
print ("Loading server list...")

list_of_server = list(net_speed.get_servers())
print(list_of_server)
#Step 2- Choosing the best server
print("Choosing  Best Server...")
best = list(net_speed.get_best_server())
print (best)
# print(f"Server Found: {best['host']} Located in {best['country']}")
print("Performing Download Test")
download_results = net_speed.download()
print("Performing Upload Test")
upload_results = net_speed.upload()
ping_results = net_speed.results.ping
print(download_results )
print(upload_results)
print(ping_results)
print(f"Download Speed : {download_results/1024/1024:.2f} Mbps")
print(f"Upload Speed : {upload_results/1024/1024:.2f} Mbps")
print(f"Ping Speed : {ping_results:.2f} Mbps")