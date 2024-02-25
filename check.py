import asyncio
import aiohttp

async def make_request(session, url):
    async with session.get(url) as response:
        return await response.text()

async def load_test(url, num_requests):
    async with aiohttp.ClientSession() as session:
        tasks = [make_request(session, url) for _ in range(num_requests)]
        responses = await asyncio.gather(*tasks)
        return responses

if __name__ == "__main__":
    server_url = "http://192.168.1.53/"
    num_requests = 100  

    loop = asyncio.get_event_loop()
    responses = loop.run_until_complete(load_test(server_url, num_requests))

    
    for i, response in enumerate(responses):
        print(i)
