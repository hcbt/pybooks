#!/usr/bin/env python3
#no user info calls implemented

import asyncio

import utils.config
import utils.client

class Search():
### item
    async def get_item(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = await utils.client.get_request(endpoint, params)
        return response.get("items", [{}])[0]

    async def get_kind(self, item):
        return item.get("kind")

    async def get_id(self, item):
        return item.get("id")

    async def get_etag(self, item):
        return item.get("etag")

    async def get_self_link(self, item):
        return item.get("selfLink")

#volumeInfo
    async def get_volume_info(self, item):
        return item.get("volumeInfo", {})

    async def get_title(self, item):
        volume_info = item.get("volumeInfo", {})
        return volume_info.get("title", None)

    async def get_subtitle(self, item):
        volume_info = item.get("volumeInfo", {})
        return volume_info.get("subtitle", None)

    async def get_authors(self, item):
        volume_info = item.get("volumeInfo", {})
        authors = ", ".join(map(str, volume_info.get("authors", [])))
        return authors

    async def publisher(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["volumeInfo"]
        if "publisher" in info:
            return response["items"][0]["volumeInfo"]["publisher"]

    async def published_date(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["volumeInfo"]
        if "publishedDate" in info:
            return response["items"][0]["volumeInfo"]["publishedDate"]        
        
    async def description(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["volumeInfo"]
        if "description" in info:
            return response["items"][0]["volumeInfo"]["description"]

    async def industry_identifiers(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["volumeInfo"]
        if "industryIdentifiers" in info:
            return str(response["items"][0]["volumeInfo"]["industryIdentifiers"]).replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("'", "").replace("type: ", "").replace(", identifier: ", ": ")

    async def page_count(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["volumeInfo"]
        if "pageCount" in info:
            return response["items"][0]["volumeInfo"]["pageCount"]

    async def dimensions(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["volumeInfo"]
        if "dimensions" in info:
            return response["items"][0]["volumeInfo"]["dimensions"]

    async def print_type(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["volumeInfo"]
        if "printType" in info:
            return response["items"][0]["volumeInfo"]["printType"]

    async def main_category(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["volumeInfo"]
        if "mainCategory" in info:
            return response["items"][0]["volumeInfo"]["mainCategory"]

    async def categories(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["volumeInfo"]
        if "categories" in info:
            return response["items"][0]["volumeInfo"]["categories"]

    async def average_rating(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["volumeInfo"]
        if "averageRating" in info:
            return response["items"][0]["volumeInfo"]["averageRating"]

    async def ratings_count(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["volumeInfo"]
        if "ratingsCount" in info:
            return response["items"][0]["volumeInfo"]["ratingsCount"]

    async def content_version(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["volumeInfo"]
        if "contentVersion" in info:
            return response["items"][0]["volumeInfo"]["contentVersion"]

    async def images(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["volumeInfo"]
        if "imageLinks" in info:
            return response["items"][0]["volumeInfo"]["imageLinks"]

    async def language(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["volumeInfo"]
        if "imageLinks" in info:
            return response["items"][0]["volumeInfo"]["imageLinks"]

    async def canonical_volume_link(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["volumeInfo"]
        if "canonicalVolumeLink" in info:
            return response["items"][0]["volumeInfo"]["canonicalVolumeLink"]

"""
#saleInfo
    async def sale_country(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["saleInfo"]
        if "country" in info:
            return response["items"][0]["saleInfo"]["country"]

    async def saleability(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["saleInfo"]
        if "saleability" in info:
            return response["items"][0]["saleInfo"]["saleability"]

    async def on_sale_date(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["saleInfo"]
        if "onSaleDate" in info:
            return response["items"][0]["saleInfo"]["onSaleDate"]

    async def is_ebook(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["saleInfo"]
        if "isEbook" in info:
            return response["items"][0]["saleInfo"]["isEbook"]

    async def list_price(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["saleInfo"]
        if "listPrice" in info:
            return response["items"][0]["saleInfo"]["listPrice"]

    async def retail_price(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["saleInfo"]
        if "retailPrice" in info:
            return response["items"][0]["saleInfo"]["retailPrice"]

    async def buy_link(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["saleInfo"]
        if "buyLink" in info:
            return response["items"][0]["saleInfo"]["buyLink"]

#accessInfo
    async def access_country(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["accessInfo"]
        if "country" in info:
            return response["items"][0]["accessInfo"]["country"]

    async def access_viewability(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["accessInfo"]
        if "viewability" in info:
            return response["items"][0]["accessInfo"]["viewability"]

    async def access_epub(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["accessInfo"]
        if "epub" in info:
            return response["items"][0]["accessInfo"]["epub"]

    async def access_pdf(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["accessInfo"]
        if "pdf" in info:
            return response["items"][0]["accessInfo"]["pdf"]

    async def web_reader_link(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["accessInfo"]
        if "webReaderLink" in info:
            return response["items"][0]["accessInfo"]["webReaderLink"]

    async def access_view_status(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["accessInfo"]
        if "accessViewStatus" in info:
            return response["items"][0]["accessInfo"]["accessViewStatus"]

    async def download_access(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["accessInfo"]
        if "downloadAccess" in info:
            return response["items"][0]["accessInfo"]["downloadAccess"]

    async def quote_sharing_allowed(self, query):
        endpoint = "/volumes"
        params = {"q": query}
        response = utils.client.get_request(endpoint, params)
        info = response["items"][0]["accessInfo"]
        if "quoteSharingAllowed" in info:
            return response["items"][0]["accessInfo"]["quoteSharingAllowed"]
"""