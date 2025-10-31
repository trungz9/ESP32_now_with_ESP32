import network
import aioespnow
import asyncio

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.config(channel=1)
sta.disconnect()

e = aioespnow.AIOESPNow()
e.active(True)

async def receive_messages():
    async for mac, msg in e:
        print(f"Received from {mac.hex().upper()}: {msg.decode()}")

asyncio.run(receive_messages())
