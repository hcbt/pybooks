#!/usr/bin/env python3

import asyncio
import aiofiles.os

async def rename(filename, new_filename):
    await aiofiles.os.rename(filename, new_filename)