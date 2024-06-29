# coding: utf-8

"""
    GroundX API

    Ground Your RAG Apps in Fact not Fiction

    The version of the OpenAPI document: 1.0.0
    Contact: support@groundx.ai
    Created by: https://www.groundx.ai/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from groundx.type.document_type import DocumentType

class RequiredDocumentRemoteUploadRequestDocumentsItem(TypedDict):
    # the bucketId of the bucket which this remote file will be uploaded to.
    bucketId: int

    # The URL of the document being uploaded to GroundX.
    sourceUrl: str


class OptionalDocumentRemoteUploadRequestDocumentsItem(TypedDict, total=False):
    # The name of the file being uploaded
    fileName: str

    fileType: DocumentType

    # Custom metadata which can be used to influence GroundX's search functionality. This data can be used to further hone GroundX search.
    searchData: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class DocumentRemoteUploadRequestDocumentsItem(RequiredDocumentRemoteUploadRequestDocumentsItem, OptionalDocumentRemoteUploadRequestDocumentsItem):
    pass
