# from ddtrace import patch_all, tracer
# patch_all()

import typing
from logging import Logger
from time import time
from azure.functions import AppExtensionBase, Context, HttpResponse

import os

class TimerExtension(AppExtensionBase):
    """A Python worker extension to record elapsed time in a function invocation
    """
    # from ddtrace import patch_all, tracer
    # patch_all()

    @classmethod
    def init(cls):
        print("=========== in init NEW =============")
        cls.start_timestamps: typing.Dict[str, float] = {}

    @classmethod
    def configure(cls, *args, append_to_http_response:bool=False, **kwargs):
        # Customer can use TimerExtension.configure(append_to_http_response=)
        # to decide whether the elapsed time should be shown in HTTP response
        cls.append_to_http_response = append_to_http_response


    @classmethod
    def pre_invocation_app_level(
        cls, logger: Logger, context: Context,
        func_args: typing.Dict[str, object],
        *args, **kwargs
    ) -> None:
        logger.info(f'Recording start time of {context.function_name}')
        # span = tracer.trace('top.level.span')  # span is started once created
        # cls.span = span
        # print(span)
        cls.start_timestamps[context.invocation_id] = time()

    @classmethod
    def post_invocation_app_level(
        cls, logger: Logger, context: Context,
        func_args: typing.Dict[str, object],
        func_ret: typing.Optional[object],
        *args, **kwargs
    ) -> None:
        if context.invocation_id in cls.start_timestamps:
            # Get the start_time of the invocation
            start_time: float = cls.start_timestamps.pop(context.invocation_id)
            end_time: float = time()
            # Calculate the elapsed time
            elapsed_time = end_time - start_time
            logger.info(f'Time taken to execute {context.function_name} is {elapsed_time} sec')
            # print(cls.span)
            # cls.span.finish()

            # Append the elapsed time to the end of HTTP response
            # if the append_to_http_response is set to True
            if cls.append_to_http_response and isinstance(func_ret, HttpResponse):
                func_ret._HttpResponse__body += f' (TimeElapsed: {elapsed_time} sec)'.encode()