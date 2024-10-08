import nextcord, set12, aiohttp
from io import BytesIO

image_cache = {}


async def send_image(ctx, table_type):
    if table_type in image_cache:
        data = image_cache[table_type]
    else:
        url = set12.table[table_type]
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return await ctx.send("Could not download file...")
                data = BytesIO(await resp.read())

    await ctx.send(file=nextcord.File(data, "${table_type}.png"))


async def send_message():
    return
