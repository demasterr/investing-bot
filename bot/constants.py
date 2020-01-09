from enum import Enum
from bot.settings import BASE_DIR, PLUGIN_STRATEGIES_DIR, PLUGIN_DATA_PROVIDERS_DIR
"""
bot constants
"""
DEFAULT_CONFIG = 'config.json'
DEFAULT_MAX_WORKERS = 2
BASE_DIR = BASE_DIR
PLUGIN_STRATEGIES_DIR = PLUGIN_STRATEGIES_DIR
PLUGIN_DATA_PROVIDERS_DIR = PLUGIN_DATA_PROVIDERS_DIR


class TimeUnit(Enum):

    second = 'SEC',
    minute = 'MIN',
    hour = 'HR',
    always = 'ALWAYS'

    # Static factory method to convert a string to TimeUnit
    @staticmethod
    def from_string(value: str):

        if value in ('SEC' 'sec', 'SECOND', 'second', 'SECONDS', 'seconds'):
            return TimeUnit.second

        elif value in ('MIN', 'min', 'MINUTE', 'minute', 'MINUTES', 'minutes'):
            return TimeUnit.minute

        elif value in ('HR', 'hr', 'HOUR', 'hour', 'HOURS', 'hour'):
            return


class ExecutionMode(Enum):

    synchronous = 'synchronous',
    asynchronous = 'asynchronous'

    @staticmethod
    def from_string(value: str):

        if value in ('async', 'asynchronous'):
            return ExecutionMode.asynchronous

        if value in ('sync', 'synchronous', 'synchronized'):
            return ExecutionMode.synchronous
