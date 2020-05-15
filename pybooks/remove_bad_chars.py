#!/usr/bin/env python3
import asyncio

async def remove_bad_chars(filename):
    bad_chars = ["-", ".pdf"]

    for i in bad_chars:
        filename = str(filename).replace(i, "")

    return filename