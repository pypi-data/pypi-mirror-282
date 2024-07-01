# TODO: remove once all breaking changes related to deprecation are done
import inspect
from datetime import date
from functools import lru_cache

from .mini_logger import MiniLogger as logger


@lru_cache(maxsize=64)  # don't print the same warning multiple times
def deprecation_warning(old_name: str, new_name: str, start_date: date = None) -> None:
    if start_date and start_date < date.today():
        return
    warnings_message = f"{new_name} {old_name} and use the local version."
    try:
        warnings_message += " Called from: " + inspect.stack()[2].filename
    except Exception:
        pass
    logger.warning(warnings_message)
