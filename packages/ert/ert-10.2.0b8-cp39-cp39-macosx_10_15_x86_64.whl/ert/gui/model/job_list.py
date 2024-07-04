from typing import Any, List, Optional, overload

from qtpy.QtCore import (
    QAbstractItemModel,
    QAbstractProxyModel,
    QModelIndex,
    QObject,
    Qt,
    QVariant,
    Slot,
)
from typing_extensions import override

from ert.ensemble_evaluator import identifiers as ids
from ert.gui.model.node import NodeType
from ert.gui.model.snapshot import (
    COLUMNS,
    IsEnsembleRole,
    IsJobRole,
    IsRealizationRole,
    NodeRole,
)


class JobListProxyModel(QAbstractProxyModel):
    """This proxy model presents two-dimensional views (row-column) of
    forward model data for a specific realization in a specific iteration."""

    def __init__(
        self,
        parent: Optional[QObject],
        iter_: int,
        real: int,
    ) -> None:
        super().__init__(parent=parent)
        self._iter = iter_
        self._real = real

    @Slot(int, int)
    def set_real(self, iter_: int, real: int) -> None:
        """Called when the user clicks a specific realization in the run_dialog window."""
        self._disconnect()
        self.modelAboutToBeReset.emit()
        self._iter = iter_
        self._real = real
        self.modelReset.emit()
        self._connect()

    def _disconnect(self) -> None:
        source_model = self.sourceModel()
        if source_model is None:
            return
        source_model.dataChanged.disconnect(self._source_data_changed)
        source_model.modelAboutToBeReset.disconnect(self.modelAboutToBeReset)
        source_model.modelReset.disconnect(self.modelReset)

    def _connect(self) -> None:
        source_model = self.sourceModel()
        if source_model is None:
            return
        source_model.dataChanged.connect(self._source_data_changed)
        source_model.modelAboutToBeReset.connect(self.modelAboutToBeReset)
        source_model.modelReset.connect(self.modelReset)

    def _get_source_parent_index(self) -> QModelIndex:
        start = self.index(0, 0, QModelIndex())
        if not start.isValid():
            return QModelIndex()
        if start.internalPointer() is None:
            return QModelIndex()
        source_parent = self.mapToSource(start).parent()
        return source_parent

    @override
    def setSourceModel(self, sourceModel: Optional[QAbstractItemModel]) -> None:
        if not sourceModel:
            raise ValueError("need source model")
        self.beginResetModel()
        self._disconnect()
        super().setSourceModel(sourceModel)
        self._connect()
        self.endResetModel()

    @override
    def headerData(
        self,
        section: int,
        orientation: Qt.Orientation,
        role: int = Qt.ItemDataRole.DisplayRole,
    ) -> Any:
        if role != Qt.ItemDataRole.DisplayRole:
            return QVariant()
        if orientation == Qt.Orientation.Horizontal:
            header = COLUMNS[NodeType.REAL][section]
            if header in [ids.STDOUT, ids.STDERR]:
                return header.upper()
            if header in [ids.CURRENT_MEMORY_USAGE, ids.MAX_MEMORY_USAGE]:
                header = header.replace("_", " ")
            return header.capitalize()
        if orientation == Qt.Orientation.Vertical:
            return section
        return QVariant()

    @override
    def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
        return len(COLUMNS[NodeType.REAL])

    def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
        if parent is None:
            parent = QModelIndex()
        if parent.isValid():
            return 0
        source_index = self._get_source_parent_index()
        if not source_index.isValid():
            return 0
        source_model = self.sourceModel()
        assert source_model is not None
        return source_model.rowCount(source_index)

    @overload
    def parent(self, child: QModelIndex) -> QModelIndex: ...
    @overload
    def parent(self) -> Optional[QObject]: ...
    @override
    def parent(self, child: Optional[QModelIndex] = None) -> Optional[QObject]:
        return QModelIndex()

    @override
    def index(
        self, row: int, column: int, parent: Optional[QModelIndex] = None
    ) -> QModelIndex:
        if parent is None:
            parent = QModelIndex()
        if parent.isValid():
            return QModelIndex()
        job_index = self.mapToSource(self.createIndex(row, column, parent))
        return self.createIndex(row, column, job_index.data(NodeRole))

    def mapToSource(self, proxyIndex: QModelIndex) -> QModelIndex:
        if not proxyIndex.isValid():
            return QModelIndex()
        source_model = self.sourceModel()
        assert source_model is not None
        iter_index = source_model.index(self._iter, 0, QModelIndex())
        if not iter_index.isValid() or not source_model.hasChildren(iter_index):
            return QModelIndex()
        real_index = source_model.index(self._real, 0, iter_index)
        if not real_index.isValid() or not source_model.hasChildren(real_index):
            return QModelIndex()
        job_index = source_model.index(
            proxyIndex.row(), proxyIndex.column(), real_index
        )
        return job_index

    def mapFromSource(self, sourceIndex: QModelIndex) -> QModelIndex:
        if not sourceIndex.isValid():
            return QModelIndex()
        if not self._accept_index(sourceIndex):
            return QModelIndex()
        return self.index(sourceIndex.row(), sourceIndex.column(), QModelIndex())

    def _source_data_changed(
        self, top_left: QModelIndex, bottom_right: QModelIndex, roles: List[int]
    ) -> None:
        if not self._accept_index(top_left):
            return
        proxy_top_left = self.mapFromSource(top_left)
        proxy_bottom_right = self.mapFromSource(bottom_right)
        if not proxy_top_left.isValid() or not proxy_bottom_right.isValid():
            return
        self.dataChanged.emit(proxy_top_left, proxy_bottom_right, roles)

    def _accept_index(self, index: QModelIndex) -> bool:
        if index.internalPointer() is None:
            return False

        # This model should only consist of job indices, so anything else mean
        # the index is not on "our branch" of the state graph.
        if not index.data(IsJobRole):
            return False

        # traverse upwards and check real and iter against parents of
        # this index.
        while index.isValid() and index.internalPointer() is not None:
            if (index.data(IsRealizationRole) and (index.row() != self._real)) or (
                index.data(IsEnsembleRole) and (index.row() != self._iter)
            ):
                return False
            index = index.parent()
        return True

    def get_iter(self) -> int:
        return self._iter

    def get_real(self) -> int:
        return self._real
