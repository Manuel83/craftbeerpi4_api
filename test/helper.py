from asynctest import MagicMock, CoroutineMock


class AsyncMock(MagicMock):
    async def __call__(self, *args, **kwargs):
        return super(AsyncMock, self).__call__(*args, **kwargs)

class BusMock():

    fire = CoroutineMock(return_value=3)
    fire_sync = MagicMock()

class CraftBeerPiMock(CoroutineMock):



    bus = BusMock()
    test = CoroutineMock(return_value=3)

