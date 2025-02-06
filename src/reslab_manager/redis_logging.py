# -*- encoding: utf-8 -*-

import json
import logging
import os

import redis
from django.utils import timezone


class RedisHandler(logging.Handler):
    def __init__(self, host="redis", port=6379, password="", key="reslab_manager:logs"):
        super().__init__()
        self.redis = redis.StrictRedis(
            host=host, port=port, password=password, decode_responses=True
        )
        self.key = key

    def emit(self, record):
        log_entry = self.format(record)
        self.redis.rpush(self.key, log_entry)
