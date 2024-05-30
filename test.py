import asyncio
import threading

async def main():
    # Your async code here
    print("Hello, World!")

def run_loop_in_thread(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

loop = asyncio.new_event_loop()
t = threading.Thread(target=run_loop_in_thread, args=(loop,))
t.start()