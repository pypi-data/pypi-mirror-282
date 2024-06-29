from accions import *
from asyncio import run


# value = run(MultiWalk("","CM",[""],True,True))
# print(value['0'][0])


async def exec():
    value = await Get_async('181.232.180.7',"ConextVM","1.3.6.1.4.1.2011.6.128.1.1.2.43.1.3.4194403072.4")

    return value


print(run(exec()))


