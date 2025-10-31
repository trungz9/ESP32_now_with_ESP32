import network    #type: ignore

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Get MAC address (returns bytes)
mac = wlan.config('mac')

# Convert to human-readable format
mac_address = ':'.join('%02x' % b for b in mac)

print("MAC Address:", mac_address)