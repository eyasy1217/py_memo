#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# usage
import logger as lg
lg.init()
logger = lg.get_logger(__name__)
logger.info('message')

"""
import json
import logging
import logging.config
import os


default_config_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', 'logging.json'
)


def init(config_path=default_config_path):
    with open(config_path) as f:
        logging.config.dictConfig(json.load(f))


def get_logger(nm: str) -> logging.Logger:
    return logging.getLogger(nm)
