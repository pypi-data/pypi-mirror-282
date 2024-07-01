import logging
import typing

logger = logging.getLogger("dork")


class SearchBase(object):
    def __init__(self, fields="url", **kwargs):
        self.fields = fields

    def _query(self, dork: str, page: int) -> typing.Optional[typing.List[dict]]:
        ...

    def query(self, dork: str, start_page=1, end_page=1) -> typing.Iterable[typing.Dict]:
        current_page = start_page
        while True:
            items = self._query(dork, page=current_page)
            if not items:
                break
            logger.info(f"fetch page [{current_page}] ok")
            for item in items:
                yield item
            if current_page >= end_page:
                break
            current_page += 1
