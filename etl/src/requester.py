from httpx import Client, Response


class request():
    @staticmethod
    def get(url: str, params: dict = None, ) -> Response:
        if params is None:
            params = dict()
        try:
            with Client(http2=True) as client:
                return client.get(
                    url=url,
                    params=params
                )
        except Exception as e:
            raise e