#!/usr/bin/env python3

import json
import aiohttp
import asyncio

import utils.config

async def get_request(endpoint, params):
    async with aiohttp.ClientSession() as session:
        response = await session.get(utils.config.host + endpoint, params = params)
        if (response.status != 200):
            print("Wrong request")
        return await response.json()
