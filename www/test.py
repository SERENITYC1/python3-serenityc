# -*- coding:utf-8 -*-
import orm,asyncio
from models import User,Blog,Comment
loop = asyncio.get_event_loop()

async def destory_pool():
#global __pool
    if orm.__pool is not None :
        orm.__pool.close()
        await orm.__pool.wait_closed()


async def test():
    await orm.create_pool(loop=loop,user='www-data', password='www-data', database='awesome')
    u = User(name='Test',email='test@example.com',passwd='1234567890',image='about:blank')
    await  u.save()
    await destory_pool()

loop.run_until_complete(test())
loop.close()