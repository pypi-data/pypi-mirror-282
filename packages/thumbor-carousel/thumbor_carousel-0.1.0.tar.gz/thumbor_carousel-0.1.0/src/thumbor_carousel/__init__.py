import base64
import json

import tornado
from thumbor.filters import BaseFilter, filter_method
from thumbor.loaders import LoaderResult
from thumbor.utils import logger


class Filter(BaseFilter):
    """
        Filter for creating a carousel from multiple images.

        Usage:
            /filters:carousel(
                <urls_json>,
                <img_count>,
                <carousel_padding_x>,
                <carousel_padding_y>,
                <carousel_padding_color>,
                <img_padding_x>,
                <img_padding_y>,
                <img_padding_color>,
                <more_text_size>,
                <more_text_color>
            )
    """

    def __init__(self, params, context=None):
        super().__init__(params, context)
        self.img_count: int = 0
        self.carousel_padding: tuple[int, int, str] = (0, 0, 'ffffff00')
        self.img_padding: tuple[int, int, str] = (0, 0, 'ffffff00')
        self.more_text: tuple[int, str] = (10, 'ffffff00')
        self.images: list[bytes] = []
        self.storage = self.context.modules.storage

    def padding(self, engine, padding_x: int, padding_y: int, color: str):
        offset_x = padding_x
        offset_y = padding_y

        new_width = engine.size[0] + (2 * padding_x)
        new_height = engine.size[1] + (2 * padding_y)

        new_engine = self.context.modules.engine.__class__(self.context)
        new_engine.image = new_engine.gen_image((new_width, new_height), color)
        new_engine.enable_alpha()
        new_engine.paste(engine, (offset_x, offset_y))

        engine.image = new_engine.image

    def join(self, engines, count: int):
        width = sum([engine.size[0] for engine in engines])
        height = engines[0].size[1]

        new_engine = self.context.modules.engine.__class__(self.context)
        new_engine.image = new_engine.gen_image((width, height), 'ffffff00')
        new_engine.enable_alpha()

        offset_x = 0
        index = 0
        for engine in engines:
            new_engine.paste(engine, (offset_x, 0))
            offset_x += engine.size[0]
            index += 1
            if index >= count:
                break

        return new_engine

    async def load_images(self, urls_json: str):
        engines = []

        urls = json.load(urls_json)
        if len(urls) <= 0:
            raise tornado.web.HTTPError(400, "No images provided")

        for url in urls:
            if not self.validate(url):
                raise tornado.web.HTTPError(400)

            buffer = await self.storage.get(url)
            if buffer is not None:
                self.images.append(buffer)
                continue

            result = await self.context.modules.loader.load(
                self.context, url
            )

            if isinstance(result, LoaderResult) and not result.successful:
                logger.warning(
                    "bad image result error=%s metadata=%s",
                    result.error,
                    result.metadata,
                )
                raise tornado.web.HTTPError(
                    400,
                    "bad image result error=%s metadata=%s".format(result.error, result.metadata)
                )

            if isinstance(result, LoaderResult):
                buffer = result.buffer
            else:
                buffer = result

            await self.storage.put(url, buffer)
            await self.storage.put_crypto(url)

            engine = self.context.modules.engine.__class__(self.context)
            engine.load(buffer, None)
            engine.enable_alpha()
            engines.append(engine)

        return engines

    def validate(self, url):
        if not hasattr(self.context.modules.loader, "validate"):
            return True

        if not self.context.modules.loader.validate(self.context, url):
            logger.warning('image source not allowed: "%s"', url)
            return False
        return True

    @filter_method(
        BaseFilter.String,  # urls_json (string of image urls JSON)
        BaseFilter.PositiveNonZeroNumber,  # img_count (number of images in carousel)
        BaseFilter.PositiveNonZeroNumber,  # carousel_padding_x (x axis padding for carousel)
        BaseFilter.PositiveNonZeroNumber,  # carousel_padding_y (y axis padding for carousel)
        BaseFilter.String,  # carousel_padding_color (color for carousel padding)
        BaseFilter.PositiveNonZeroNumber,  # img_padding_x (x axis padding for images)
        BaseFilter.PositiveNonZeroNumber,  # img_padding_y (y axis padding for images)
        BaseFilter.String,  # img_padding_color (color for images padding)
        BaseFilter.PositiveNonZeroNumber,  # more_text_size (size of more text)
        BaseFilter.String,  # more_text_color (color of more text)
    )
    async def carousel(
            self,
            urls_json: str,
            img_count: int,
            carousel_padding_x: int,
            carousel_padding_y: int,
            carousel_padding_color: str,
            img_padding_x: int,
            img_padding_y: int,
            img_padding_color: str,
            more_text_size: int,
            more_text_color: str
    ):
        image_engines = await self.load_images(urls_json)

        logger.info('hihi')

        for engine in image_engines:
            self.padding(engine, img_padding_x, img_padding_y, img_padding_color)

        carousel_engine = self.join(image_engines, img_count)
        self.padding(carousel_engine, carousel_padding_x, carousel_padding_y, carousel_padding_color)

        self.engine = carousel_engine
