
ipchk = "192.168.0.1"
if ipchk:
    print("Looks like the IP address was set {} ".format(ipchk))
ipchk = input("Apply an IP address: ")

if ipchk:
    print("Looks like the IP address was set {} ".format(ipchk))

ipchk = input("Apply an IP address: ")
if ipchk:
    print("Looks like the IP address was set {} ".format(ipchk))
else:
    print("You did not provide input.")

ipchk = input("Apply an IP address: ")
if ipchk == "192.168.70.1":
    print("Looks like the IP address of the Gateway was set {} ".format(ipchk) + " This is not recommended.")
elif ipchk:  # if any data is provided, this will test true
    print("Looks like the IP address was set {} ".format(ipchk))  # indented under if
else:  # if data is NOT provided
    print("You did not provide input.")  # indented under else