import asyncio
import unittest
from asyncio import coroutine
from unittest.mock import MagicMock, Mock

import asynctest

from cbpi_api.sensor import CBPiSensor
from test.helper import CraftBeerPiMock


class TestSensor(CBPiSensor):

    def init(self):
        print("OOHOO")

    async def run(self, cbpi):
        self.log_data(100)
        print("######", await cbpi.bus.fire(topic=""))



class TestSensor(asynctest.TestCase):
    use_default_loop = True

    forbid_get_event_loop = False


    async def test_something(self):
        print("HALLO")
        c = CraftBeerPiMock()


        print(await c.test())
        config = dict(cbpi=None, id=1)
        sensor = TestSensor(**config)
        sensor.init()
        sensor.log_data(100)
        await sensor.run(c)
        self.assertEqual('foo'.upper(), 'FOO')
        pass

