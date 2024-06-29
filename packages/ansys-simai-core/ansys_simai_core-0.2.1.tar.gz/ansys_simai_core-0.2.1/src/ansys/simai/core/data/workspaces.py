# Copyright (C) 2023 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import warnings
from pprint import pformat
from typing import Any, BinaryIO, Dict, List, Optional, Union

from ansys.simai.core.data.base import DataModel, Directory
from ansys.simai.core.data.types import File, Identifiable, get_id_from_identifiable


class ModelManifest:
    """Provides information about a model associated with a workspace."""

    def __init__(self, raw_manifest: Dict[str, Any]):
        self._raw = raw_manifest

    def __repr__(self) -> str:
        return pformat(self._raw)

    @property
    def name(self) -> str:
        """Name of the model."""
        return self._raw["model_name"]

    @property
    def version(self) -> str:
        """Version of the software running the model."""
        return self._raw["coreml_version"]

    @property
    def description(self) -> str:
        """Short description of the model."""
        return self._raw["description"]

    @property
    def geometry(self) -> Dict[str, Any]:
        """Information on the geometry format expected by the model."""
        return self._raw["geometry"]

    @property
    def boundary_conditions(self) -> Dict[str, Any]:
        """Information on the boundary conditions expected by the model. For example, the prediction's input."""
        return self._raw["boundary_conditions"]

    @property
    def physical_quantities(self) -> Dict[str, Any]:
        """Information on the physical quantities generated by the model. For example, the prediction's output."""
        return self._raw["physical_quantities"]

    @property
    def post_processings(self) -> "List[Dict[str, Any]]":
        """Information on the postprocessings available for the model
        and the accepted parameters when relevant.
        """
        return self._raw["available-post-processings"]


class Workspace(DataModel):
    """Provides the local representation of a workspace object."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._model_manifest = None

    def __repr__(self) -> str:
        return f"<Workspace: {self.id}, {self.name}>"

    @property
    def name(self) -> str:
        """Name of the workspace."""
        return self.fields["name"]

    @property
    def model(self) -> ModelManifest:
        """Deprecated alias to :py:attr:`~model_manifest`."""
        warnings.warn(
            "workspace.model is deprecated, please use workspace.model_manifest", stacklevel=2
        )
        return self.model_manifest

    @property
    def model_manifest(self) -> ModelManifest:
        """:class:`~ansys.simai.core.data.workspaces.ModelManifest` instance containing
        information about the model associated with the workspace.
        """
        if self._model_manifest is None:
            self._model_manifest = ModelManifest(
                self._client._api.get_workspace_model_manifest(self.id)
            )
        return self._model_manifest

    def delete(self):
        """Delete the workspace."""
        return self._client._api.delete_workspace(self.id)

    def set_as_current_workspace(self) -> None:
        """Configure the client to use this workspace instead of the one currently configured."""
        self._client.current_workspace = self

    def download_model_evaluation_report(
        self, file: Optional[File] = None
    ) -> Union[None, BinaryIO]:
        """Download the PDF of the model evaluation report for the workspace.

        Args:
            file: Binary file-object or the path of the file to put the content into.

        Returns:
            ``None`` if a file is specified or a binary file-object otherwise.
        """
        return self._client._api.download_workspace_model_evaluation_report(self.id, file)


class WorkspaceDirectory(Directory[Workspace]):
    """Provides a collection of methods related to workspaces.

    This class is accessed through ``client._workspaces``.

    Example:
      .. code-block:: python

            import ansys.simai.core

            simai = ansys.simai.core_from_config()
            simai.workspaces.list()
    """

    _data_model = Workspace

    def list(self) -> List[Workspace]:
        """List all workspaces from the server."""
        return [self._model_from(workspace) for workspace in self._client._api.workspaces()]

    def get(self, id: Optional[str] = None, name: Optional[str] = None) -> Workspace:
        """Get a specific workspace object from the server by either ID or name.

        You can specify either the ID or the name, not both.

        Args:
            id: ID of the workspace.
            name: Name of the workspace.

        Returns:
            Workspace.

        Raises:
            NotFoundError: No geometry with the given ID exists.
        """
        if name and id:
            raise ValueError("'id' and 'name' cannot both be specified.")
        if name:
            return self._model_from(self._client._api.get_workspace_by_name(name))
        if id:
            return self._model_from(self._client._api.get_workspace(id))
        raise ValueError("Either 'id' or 'name' must be specified.")

    def create(self, name: str, model_id: str) -> Workspace:
        """Create a workspace.

        Args:
            name: Name to give the new workspace.
            model_id: ID of the model for the workspace to use.
        """
        return self._model_from(self._client._api.create_workspace(name, model_id))

    def delete(self, workspace: Identifiable[Workspace]) -> None:
        """Delete a workspace.

        Args:
            workspace: ID or :class:`model <Workspace>` of the workspace.
        """
        self._client._api.delete_workspace(get_id_from_identifiable(workspace))
