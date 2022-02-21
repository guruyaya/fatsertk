import pytest
from .helper import async_test
from tortoise import Tortoise
import os
from tortoisec.model1 import Event

@async_test
async def test_main():
    try:
        os.remove('db.sqlite3')
    except FileNotFoundError:  # pragma: nocoverage
        pass
    except OSError as e:
        if e.errno != 22:  # fix: "sqlite://:memory:" in Windows
            raise e

    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['tortoisec.model1']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()

    event = await Event.create(name="Test")
    assert event.id == 1





