# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class FileSchemaTestClass(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    @classmethod
    @property
    def file(cls) -> typing.Type['File']:
        return File
    
    
    class files(
        schemas.ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['File']:
            return File


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        file: typing.Union['File', schemas.Unset] = schemas.unset,
        files: typing.Union[files, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Type[schemas.Schema],
    ) -> 'FileSchemaTestClass':
        return super().__new__(
            cls,
            *args,
            file=file,
            files=files,
            _configuration=_configuration,
            **kwargs,
        )

from petstore_api.model.file import File
