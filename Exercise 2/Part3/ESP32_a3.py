import network
import aioespnow
import asyncio

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.config(channel=1)
sta.disconnect()

e = aioespnow.AIOESPNow()
e.active(True)

broadcast_mac = b'\xff\xff\xff\xff\xff\xff'

async def send_broadcast():
    count = 0
    while True:
        msg = f"Broadcast message #{count}"
        await e.asend(broadcast_mac, msg)
        print(f"Sent: {msg}")
        count += 1
        await asyncio.sleep(2)

asyncio.run(send_broadcast())
