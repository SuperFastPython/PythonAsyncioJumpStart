# SuperFastPython.com
# example of an asyncio sequential port scanner
import asyncio

# returns True if a connection can be made
async def test_port_number(host, port, timeout=3):
    # create coroutine for opening a connection
    coro = asyncio.open_connection(host, port)
    # execute the coroutine with a timeout
    try:
        # open the connection and wait for a moment
        _,writer = await asyncio.wait_for(coro, timeout)
        # close connection once opened
        writer.close()
        # indicate the connection can be opened
        return True
    except asyncio.TimeoutError:
        # indicate the connection cannot be opened
        return False

# main coroutine
async def main(host, ports):
    # report a status message
    print(f'Scanning {host}...')
    # scan ports sequentially
    for port in ports:
        if await test_port_number(host, port):
            print(f'> {host}:{port} [OPEN]')

# define a host and ports to scan
host = 'python.org'
ports = range(1, 1024)
# start the asyncio program
asyncio.run(main(host, ports))
