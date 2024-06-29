# -*- coding: utf-8 -*-
import logging
import traceback
import typing as t
from datetime import timedelta
from redis.exceptions import ConnectionError
from redis import Redis as Red, ConnectionPool
from redis.sentinel import Sentinel, MasterNotFoundError

EncodedT = t.Union[bytes, memoryview]
DecodedT = t.Union[str, int, float]
EncodableT = t.Union[EncodedT, DecodedT]
ExpiryT = t.Union[float, timedelta]
_StringLikeT = t.Union[bytes, str, memoryview]
KeyT = _StringLikeT
ChannelT = _StringLikeT
PatternT = _StringLikeT  # Patterns matched against keys, fields etc
FieldT = EncodableT  # Fields within hash tables, streams and geo commands
ScriptTextT = _StringLikeT
ResponseT = t.Union[t.Awaitable, t.Any]

__all__ = ['Redis']

logger = logging.getLogger(name="root")


class Redis(object):
    __db: int
    __url: str
    __port: int
    __host: str
    __password: str
    __serverName: str
    __socketTimeout: float
    __decodeResponses: bool
    __connectionPool: ConnectionPool

    def __init__(self, host: str = 'localhost', password: str = None, db: int = 0, port: int = 6379,
                 decode_responses: bool = False, socket_timeout: float = 0.5, server_name: str = 'mymaster',
                 connection_pool: ConnectionPool = None):
        self.__db = db
        self.__port = port
        self.__sentinel = None
        self.__password = password
        self.__serverName = server_name
        self.__socketTimeout = socket_timeout
        self.__connectionPool = connection_pool
        self.__decodeResponses = decode_responses
        self.__redis = self.__get_redis(host=host)

    @property
    def url(self) -> str:
        return self.__url

    @property
    def socket_timeout(self) -> float:
        return self.__socketTimeout

    @property
    def connection_pool(self) -> ConnectionPool:
        return self.__connectionPool

    @property
    def connection_details(self) -> t.List:
        if isinstance(self.host, t.List):
            c = [
                dict(
                    host=x[0], port=x[1], db=self.db, password=self.password, decode_responses=self.__decodeResponses,
                    url=self.__format_url(
                        host=x[0], port=x[1], db=self.db, decode_responses=self.__decodeResponses,
                        password=self.password
                    )
                ) for x in self.host
            ]
        elif self.__connectionPool:
            c = [self.__connectionPool]
        else:
            c = [
                dict(
                    host=self.host, port=self.port, db=self.db, password=self.password,
                    decode_responses=self.decode_responses,
                    url=self.__format_url(
                        host=self.host, port=self.port, db=self.db,
                        decode_responses=self.decode_responses, password=self.password
                    )
                )
            ]
        return c

    @property
    def server_name(self) -> str:
        return self.__serverName

    @property
    def decode_responses(self) -> bool:
        return self.__decodeResponses

    @property
    def db(self) -> int:
        return self.__db

    @property
    def host(self) -> t.Any:
        return self.__host

    @property
    def port(self) -> int:
        return self.__port

    @property
    def password(self) -> str:
        return self.__password

    @property
    def sentinel(self) -> Sentinel:
        return self.__sentinel

    @property
    def redis(self) -> Red:
        return self.__redis

    @staticmethod
    def __init_host(host: str) -> t.List or str:
        if host.find(":") != -1:
            if host.find(";") != -1:
                host_temp = host.split(';')
            else:
                host_temp = host.split(',')
            hosts = list()
            for host_sub in host_temp:
                host_sub = host_sub.strip()
                if host_sub.split(":")[-1].isdigit():
                    host_port = host_sub.split(":")
                    hosts.append((host_port[0], int(host_port[-1])))
                else:
                    raise ValueError("Parameter： host is invalid value.")
        else:
            hosts = host
        return hosts

    @staticmethod
    def __format_url(host: str, port: int, db: int, decode_responses: bool, password: str = None) -> str:
        if not password:
            password = "***"
        return f"redis://{password}@{host}:{port}/{db}?encoder=" + f"{'true' if decode_responses else 'false'}"

    def __init_sentinel_sentinels(self, hosts: t.List) -> Sentinel:
        # 连接哨兵服务器(主机名也可以用域名)
        try:
            __sentinel = Sentinel(hosts, password=self.__password, socket_timeout=self.__socketTimeout)
            # 如果连接不正常，下面的命令会触发异常
            __sentinel.master_for(service_name=self.__serverName).client()
            return __sentinel
        except (Exception, MasterNotFoundError, ConnectionError):
            try:
                __sentinel = Sentinel(
                    hosts, password=self.__password, sentinel_kwargs=dict(password=self.__password),
                    socket_timeout=self.__socketTimeout
                )
                # 如果连接不正常，下面的命令会触发异常
                __sentinel.master_for(service_name=self.__serverName).client()
                return __sentinel
            except (Exception, MasterNotFoundError, ConnectionError):
                logger.error(traceback.format_exc())

    def __get_redis(self, host: str) -> Red:
        if isinstance(self.__connectionPool, ConnectionPool):
            connection_kwargs = self.__connectionPool.connection_kwargs or dict()
            self.__db = connection_kwargs.get("db")
            self.__host = connection_kwargs.get("host")
            self.__port = connection_kwargs.get("port")
            self.__password = connection_kwargs.get("password")
            self.__decodeResponses = connection_kwargs.get("decode_responses")
        else:
            hosts = self.__init_host(host=host)
            if isinstance(hosts, t.List):
                # 连接哨兵服务器(主机名也可以用域名)
                sentinel = self.__init_sentinel_sentinels(hosts=hosts)
                if sentinel:
                    self.__sentinel = sentinel
                    master = self.__sentinel.discover_master(service_name=self.__serverName)
                    self.__host = master[0]
                    self.__port = master[1]
                else:
                    self.__host = hosts[0][0]
            else:
                self.__host = host
            self.__connectionPool = ConnectionPool(
                host=self.__host, port=self.__port, db=self.__db,
                password=self.__password, decode_responses=self.__decodeResponses
            )
        redis = Red(connection_pool=self.__connectionPool)
        self.__url = self.__format_url(
            host=self.__host, port=self.__port, db=self.__db, decode_responses=self.__decodeResponses
        )
        return redis

    def keys(self, pattern: PatternT = "*", **kwargs) -> t.Any:
        return self.__redis.keys(pattern=pattern, **kwargs)

    def get(self, name: KeyT) -> t.Any:
        return self.__redis.get(name=name)

    def set(self, name: KeyT, value: EncodableT, ex: t.Union[ExpiryT, None] = None, px: t.Union[ExpiryT, None] = None,
            nx: bool = False, xx: bool = False) -> t.Any:
        return self.__redis.set(name=name, value=value, ex=ex, px=px, nx=nx, xx=xx)

    def setex(self, name: KeyT, value: EncodableT, time: ExpiryT) -> t.Any:
        return self.__redis.setex(name=name, value=value, time=time)

    def setnx(self, name: KeyT, value: EncodableT) -> t.Any:
        return self.__redis.setnx(name=name, value=value)

    def delete(self, *names: KeyT) -> t.Any:
        return self.__redis.delete(*names)

    def hget(self, name: str, key: str) -> t.Union[t.Awaitable[t.Optional[str]], t.Optional[str]]:
        return self.__redis.hget(name=name, key=key)

    def hset(self, name: str, key: t.Optional[str] = None, value: t.Optional[str] = None,
             mapping: t.Optional[dict] = None, items: t.Optional[list] = None) -> t.Union[t.Awaitable[int], int]:
        return self.__redis.hset(name=name, key=key, value=value, mapping=mapping, items=items)

    def hgetall(self, name: str) -> t.Union[t.Awaitable[dict], dict]:
        return self.__redis.hgetall(name=name)

    def zrangebyscore(self, name: KeyT, mins: t.Union[float, str], maxs: t.Union[float, str],
                      start: t.Union[int, None] = None, num: t.Union[int, None] = None, withscores: bool = False,
                      score_cast_func: t.Union[type, t.Callable] = float) -> t.Any:
        return self.__redis.zrangebyscore(name=name, min=mins, max=maxs, start=start, num=num,
                                          withscores=withscores, score_cast_func=score_cast_func)

    def hmget(self, name: str, keys: t.List, *args: t.List) -> t.Union[t.Awaitable[t.List], t.List]:
        return self.__redis.hmget(name=name, keys=keys, *args)

    def zrange(self, name: KeyT, start: int, end: int, desc: bool = False, withscores: bool = False,
               score_cast_func: t.Union[type, t.Callable] = float, byscore: bool = False, bylex: bool = False,
               offset: int = None, num: int = None,
               ) -> t.Any:
        return self.__redis.zrange(name=name, start=start, end=end, desc=desc, withscores=withscores,
                                   score_cast_func=score_cast_func, byscore=byscore, bylex=bylex, offset=offset,
                                   num=num)

    def hexists(self, name: str, key: str) -> t.Union[t.Awaitable[bool], bool]:
        return self.__redis.hexists(name=name, key=key)

    def pipeline(self, transaction=True, shard_hint=None):
        return self.__redis.pipeline(transaction=transaction, shard_hint=shard_hint)

    def disconnect(self) -> t.NoReturn:
        return self.connection_pool.disconnect()

    def publish(self, channel: ChannelT, message: EncodableT, **kwargs) -> t.Any:
        return self.__redis.publish(channel=channel, message=message, **kwargs)

    def register_script(self, script: ScriptTextT) -> t.Any:
        """
        Register a Lua ``script`` specifying the ``keys`` it will touch.
        Returns a Script object that is callable and hides the complexity of
        deal with scripts, keys, and shas. This is the preferred way to work
        with Lua scripts.
        """
        return self.__redis.register_script(script=script)

    def llen(self, name: str) -> t.Union[t.Awaitable[int], int]:
        return self.__redis.llen(name=name)

    def lpop(self, name: str, count: t.Optional[int] = None) -> t.Union[str, t.List, None]:
        return self.__redis.lpop(name=name, count=count)

    def rpush(self, name: str, *values: FieldT) -> t.Union[t.Awaitable[int], int]:
        return self.__redis.rpush(name, *values)

    def lpos(self, name: str, value: str, rank: t.Optional[int] = None, count: t.Optional[int] = None,
             maxlen: t.Optional[int] = None) -> t.Union[str, t.List, None]:
        return self.__redis.lpos(name=name, value=value, rank=rank, count=count, maxlen=maxlen)

    def lrange(self, name: str, start: int, end: int) -> t.Union[t.Awaitable[list], list]:
        return self.__redis.lrange(name=name, start=start, end=end)

    def expire(self, name: KeyT, time: ExpiryT, nx: bool = False, xx: bool = False, gt: bool = False,
               lt: bool = False) -> ResponseT:
        return self.__redis.expire(name=name, time=time, nx=nx, xx=xx, gt=gt, lt=lt)


if __name__ == '__main__':
    redis_client_3 = Redis(host='127.0.0.1:26379', password="hello", db=3, decode_responses=True)
    redis_client_4 = Redis(host='127.0.0.1', password='hello', port=6379, db=3, decode_responses=True)
    redis_client_3.set(name="test00001", value="11111", ex=600)
    redis_client_4.set(name="test00002", value="11111", ex=600)
    print(redis_client_3.get("test00001"))
    print(redis_client_4.get("test00002"))
