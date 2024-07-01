# Copyright 2024 Superlinked, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from abc import ABC, abstractmethod

from beartype.typing import Generic, Sequence, TypeVar
from typing_extensions import Annotated, Self

from superlinked.framework.common.dag.context import ExecutionContext
from superlinked.framework.common.storage_manager.storage_manager import (
    SearchIndexParams,
    StorageManager,
)
from superlinked.framework.common.util.generic_class_util import GenericClassUtil
from superlinked.framework.common.util.time_util import now
from superlinked.framework.common.util.type_validator import TypeValidator
from superlinked.framework.dsl.index.index import Index
from superlinked.framework.dsl.source.source import SourceT
from superlinked.framework.dsl.storage.vector_database import VectorDatabase

ExecutorT = TypeVar("ExecutorT", bound="Executor")


class App(ABC, Generic[ExecutorT]):
    """
    Abstract base class for an App, a running executor that can for example do queries or ingest data.
    """

    def __init__(
        self,
        executor: ExecutorT,
    ) -> None:
        """
        Initialize the App.

        Args:
            executor (ExecutorT): The executor instance.
        """
        self._executor = executor
        self._storage_manager = StorageManager(
            self._executor._vector_database._vdb_connector
        )
        self.now = now()
        self.__init_search_indices()

    @property
    def executor(self) -> ExecutorT:
        """
        Get the executor.

        Returns:
            ExecutorT: The executor instance.
        """
        return self._executor

    @property
    def storage_manager(self) -> StorageManager:
        """
        Get the storage manager.

        Returns:
            StorageManager: The storage manager instance.
        """
        return self._storage_manager

    def __init_search_indices(self) -> None:
        search_index_params = [
            SearchIndexParams(
                index._dag.index_node.node_id,
                index._dag.index_node.length,
                index._fields,
            )
            for index in self.executor._indices
        ]
        self.storage_manager.init_search_indices(search_index_params)


class Executor(ABC, Generic[SourceT]):
    """
    Abstract base class for an executor.
    """

    @TypeValidator.wrap
    def __init__(
        self,
        sources: Sequence[SourceT],
        indices: Annotated[Sequence[Index], TypeValidator.list_validator(Index)],
        vector_database: VectorDatabase,
        context: ExecutionContext,
    ) -> None:
        """
        Initialize the Executor.

        Args:
            sources (list[SourceT]): The list of sources.
            indices (list[Index]): The list of indices.
            vector_database (VectorDatabase): The vector database which the executor will use.
            context (Mapping[str, Mapping[str, Any]]): The context mapping.
        """
        TypeValidator.validate_list_item_type(
            sources, GenericClassUtil.get_single_generic_type(self), "sources"
        )
        self._sources = sources
        self._indices = indices
        self._vector_database = vector_database
        self._context = context

    @property
    def context(self) -> ExecutionContext:
        """
        Get the context.

        Returns:
            Mapping[str, Mapping[str, Any]]: The context mapping.
        """
        return self._context

    @abstractmethod
    def run(self) -> App[Self]:
        """
        Abstract method to run the executor.

        Returns:
            App[Self]: An instance of App.
        """
