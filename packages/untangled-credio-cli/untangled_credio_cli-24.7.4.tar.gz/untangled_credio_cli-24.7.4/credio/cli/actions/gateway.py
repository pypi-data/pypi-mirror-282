import json
import aiohttp
from aiohttp import ClientSession

from credio.config import storage, store
from credio.util.type import Object
from credio.cli.actions.config import (
    DEFAULT_AUTH_TOKEN_KEY,
    DEFAULT_CONFIG_FOLDER,
    DEFAULT_CREDENTIAL_FILE,
    DEFAULT_GATEWAY_BASE_URL,
)


def store_auth_token(value: str):
    return storage.store(
        DEFAULT_CONFIG_FOLDER, name=DEFAULT_CREDENTIAL_FILE, data=value.encode()
    )


def get_auth_token():
    try:
        credentials = Object(
            json.loads(
                storage.retrieve(DEFAULT_CONFIG_FOLDER, name=DEFAULT_CREDENTIAL_FILE)
            )
        )
        return credentials.select(DEFAULT_AUTH_TOKEN_KEY, str)
    except:
        raise Exception("Please log in to continue!")


class API:
    @property
    def base_url(self):
        return store.get("GATEWAY_BASE_URL") or DEFAULT_GATEWAY_BASE_URL

    @property
    def session(self):
        return ClientSession(base_url=self.base_url)

    @property
    def auth_session(self):
        auth_token = get_auth_token()
        return ClientSession(
            base_url=self.base_url,
            headers={f"{aiohttp.hdrs.AUTHORIZATION}": "Bearer %s" % auth_token},
        )

    async def logout(self):
        store_auth_token("")

    async def register(self, email: str, password: str):
        async with self.session as session:
            async with session.post(
                "/account/register",
                json={
                    "email": email,
                    "password": password,
                },
            ) as res:
                r = Object(await res.json())
                if not res.ok:
                    raise Exception(r.select("message"))
                return "Success."

    async def authenticate(self, email: str, password: str):
        async with self.session as session:
            async with session.post(
                "/account/authenticate",
                json={
                    "email": email,
                    "password": password,
                },
            ) as res:
                r = Object(await res.json())
                if not res.ok:
                    raise Exception(r.select("message"))
                auth_token = r.select("token")
                store_auth_token(json.dumps({f"{DEFAULT_AUTH_TOKEN_KEY}": auth_token}))
                return "Success."

    async def info(self):
        async with self.auth_session as session:
            async with session.get("/account") as res:
                r = Object(await res.json())
                if not res.ok:
                    raise Exception(r.select("message"))
                return r.select("email")
