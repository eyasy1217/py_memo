#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import yaml


default_config_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', 'config.yaml'
)


class Config:
    @classmethod
    def set_config(cls):
        with open(default_config_path) as f:
            config = yaml.safe_load(f)['default']

        cls.url = config['url']