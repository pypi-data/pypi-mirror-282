'''
    __common.py
'''
from typing import Type
from typing import Any
from functools import partial
from rlabs_mini_cache.cache import Cache
from rlabs_mini_api.request import Request
from typing import Optional

from rlabs_mini_gitlab import checks
from rlabs_mini_gitlab import api_kwargs
from rlabs_mini_api.request import Request



def api_entry_protocol(
    cls: Type,
    kwargs: dict[str, Any],
    debug_message: str,
):
    '''
        API Entry Protocol

        This is called by all API endpoints on entry. It:

        1. Run some checks on the class 'cls'
        2. Logs 'debug_message'
        3. In the calling method (which is a class method from 'cls'),
           removes any parameters from 'kwargs' that are part of the method signature
           for the calling method.

        Args:
            - cls: class to run checks on
            - debug_message: debug message to log
    '''
    checks.class_is_configured(
        cls
    )
    cls.logger.debug(
        debug_message
    )
    api_kwargs.remove_grandparent_function_params(
        cls,
        kwargs
    )

def __mini_cache_read_fn(request: Request, key: str) -> dict | list:
    '''
        Mini Cache Read Fn

        THis is the Read from Source function for Mini Cache.

        'key' is ignored. but is included so it can be used by
        rlabs-mini-cache. Mini Cache will call this function
        as:

        __mini_cache_read_fn(key="some key")

        the 'key' is within the 'request' object, it's
        request.build_url()

        Args:
            - request: request to execute

        Returns:
            - data from the request
    '''
    return request.exec().python_data

def exec_cached_request(
        request: Request,
        mini_cache: Optional[Cache]
    ) -> dict | list:
    '''
        Execute Cached Request

        Executes a request. If 'mini_cache' is provided, read (execute) the request
        through 'mini_cache'. Else just read from source (execute the request
        directly).

        Args:
            - request: request to execute
    '''

    if mini_cache:
        #  -- Read through mini cache --

        # set read_fn
        mini_cache.read_fn = partial(
            __mini_cache_read_fn,
            request=request # bind request
        )

        # read from cache
        python_data = mini_cache.read(
            key=f"{request._http_method}_{request.build_url()}"
        )

    else:
        # -- Read directly from source --
        python_data = __mini_cache_read_fn(
            request=request,
            key=""
        )

    return python_data
