# Copyright (c) Qotto, 2021

"""
Google Kubernetes Engine (GKE) logging handler

>>> import sys
>>> import logging
>>> logger = logging.getLogger('my_logger')
>>> logger.setLevel('DEBUG')
>>> handler = GkeHandler(stream=sys.stdout)
>>> logger.addHandler(handler)
>>> logger.info('test')
{\
"timestamp": {"seconds": ..., "nanos": ...}, "severity": "INFO", "message": "test", \
"file": "<doctest eventy.logging.gke_handler[6]>", "line": 1, "module": "<doctest eventy.logging", \
"function": "<module>", "logger_name": "my_logger", "thread": ...\
}
"""

import json
import logging
import math

from .info_providers import correlation_id_provider, request_id_provider, user_id_provider

__all__ = [
    'GkeHandler',
]

logger = logging.getLogger(__name__)


class GkeHandler(logging.StreamHandler):
    """
    GKE logging handler formats log messages to Google Kubernetes Engine JSON format
    """

    def __init__(self, stream=None, level='DEBUG') -> None:
        """
        Initialize the handler

        :param stream: output stream, default None, propagated to StreamHandler.__init__
        :param level: log level, default 'DEBUG', should be less than Logger.setLevel()
        """
        super().__init__(stream=stream)
        self.addFilter(correlation_id_provider)
        self.addFilter(request_id_provider)
        self.addFilter(user_id_provider)
        self.setLevel(level=level)

    def format(self, record: logging.LogRecord) -> str:
        """
        Override default formatting and create a JSON in GKE format

        :param record: log record to format
        :return: formatted JSON string
        """
        try:
            message = super().format(record)
        except Exception as e:
            logger.exception(f"Could not format log record from {record.pathname}:{record.lineno}. {e}.")
            message = f"{record.msg} (with args: {record.args})"

        subsecond, second = math.modf(record.created)
        payload = {
            'timestamp': {
                'seconds': int(second),
                'nanos': int(subsecond * 1e9),
            },
            'severity': record.levelname,
            'message': message,
            'file': record.pathname,
            'line': record.lineno,
            'module': record.module,
            'function': record.funcName,
            'logger_name': record.name,
            'thread': record.thread,
        }
        if hasattr(record, 'correlation_id'):
            payload['correlation_id'] = getattr(record, 'correlation_id')
        if hasattr(record, 'request_id'):
            payload['request_id'] = getattr(record, 'request_id')
        if hasattr(record, 'user_id'):
            payload['user_id'] = getattr(record, 'user_id')
        return json.dumps(payload)
