import pytest
import asyncio

from snakestream import Stream
from conftest import MyObject


@pytest.mark.asyncio
async def test_find_min_value_normal_input():
    input_list = [1, 2, 3, 4, 5]
    # when
    it = await Stream.of(input_list) \
        .min(lambda x, y: x > y)
    # then
    assert it == 1


@pytest.mark.asyncio
async def test_find_min_value_async_input():
    async def async_comparator(x: int, y: int) -> bool:
        await asyncio.sleep(0.01)
        return x > y

    input_list = [1, 2, 3, 4, 5]
    # when
    it = await Stream.of(input_list) \
        .min(async_comparator)
    # then
    assert it == 1


@pytest.mark.asyncio
async def test_find_min_value_empty_input():
    input_list = []
    # when
    it = await Stream.of(input_list) \
        .min(lambda x, y: x > y)
    # then
    assert it is None


@pytest.mark.asyncio
async def test_find_min_value_list_with_dupe_items():
    input_list = [1, 1, 2, 3, 4, 5]
    # when
    it = await Stream.of(input_list) \
        .min(lambda x, y: x > y)
    # then
    assert it == 1

    input_list = [1, 2, 3, 4, 5, 5]
    # when
    it = await Stream.of(input_list) \
        .min(lambda x, y: x > y)
    # then
    assert it == 1


@pytest.mark.asyncio
async def test_find_min_value_negative_values():
    input_list = [-1, -2, -3, -4, -5]
    # when
    it = await Stream.of(input_list) \
        .min(lambda x, y: x > y)
    # then
    assert it == -5


@pytest.mark.asyncio
async def test_find_min_value_custom_comparator():
    input_list = ['a', 'bb', 'ccc']
    # when
    it = await Stream.of(input_list) \
        .min(lambda x, y: len(x) > len(y))
    # then
    assert it == 'a'


@pytest.mark.asyncio
async def test_find_min_value_object_comparator() -> None:
    # when
    input_list = [MyObject(1, "object1"), MyObject(2, "object2"), MyObject(3, "object3"), MyObject(2, "object2"),
                  MyObject(3, "object3")]
    it = await Stream.of(input_list) \
        .min(lambda x, y: x.id > y.id)
    # then
    assert it == MyObject(1, "object1")
