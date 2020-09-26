#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# usage
import logger as lg
lg.init()
logger = lg.get_logger(__name__)
logger.info('message')
"""
import logging
import logging.config
import os
import yaml


default_config_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', 'logging.yaml'
)


def init(config_path=default_config_path):
    with open(config_path) as f:
        logging.config.dictConfig(yaml.safe_load(f))


def get_logger(nm: str) -> logging.Logger:
    return logging.getLogger(nm)
