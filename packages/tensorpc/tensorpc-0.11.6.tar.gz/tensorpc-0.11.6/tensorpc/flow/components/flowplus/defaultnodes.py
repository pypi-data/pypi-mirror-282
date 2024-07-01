import inspect
import json
from pathlib import Path
import traceback
from typing import Any, Dict, Optional, Type, TypedDict

from tensorpc.flow.components.plus.objinspect.tree import BasicObjectTree
from .compute import ComputeNode,  ReservedNodeTypes, register_compute_node

from tensorpc.flow.components import flowui, mui


@register_compute_node(key=ReservedNodeTypes.JsonInput, name="Json Input", icon_cfg=mui.IconProps(icon=mui.IconType.DataObject))
class JsonInputNode(ComputeNode):
    class OutputDict(TypedDict):
        json: Any

    def init_node(self):
        self._editor = mui.SimpleCodeEditor("0", "json")
        self._editor.event_change.on(self._on_change)
        self._saved_value = None

    async def _on_change(self, value: str):
        self._saved_value = value

    def get_node_layout(self) -> mui.FlexBox | None:
        return mui.VBox([
            self._editor.prop(editorPadding=5)
        ]).prop(width="200px", maxHeight="300px", overflow="auto")

    async def compute(self) -> OutputDict:
        data = json.loads(self._editor.props.value)
        self._saved_value = self._editor.props.value
        return {
            'json': data
        }

    def state_dict(self) -> Dict[str, Any]:
        res = super().state_dict()
        if self._saved_value is not None:
            res["value"] = self._saved_value
        return res

    @classmethod
    async def from_state_dict(cls, data: Dict[str, Any]):
        res = ComputeNode.from_state_dict_default(data, cls)
        if "value" in data:
            res._editor.props.value = data["value"]
            res._saved_value = data["value"]
        return res

@register_compute_node(key=ReservedNodeTypes.ObjectTreeViewer, name="Object Viewer", icon_cfg=mui.IconProps(icon=mui.IconType.Visibility))
class ObjectTreeViewerNode(ComputeNode):
    def init_node(self):
        self.item_tree = BasicObjectTree(
            use_init_as_root=True,
            default_expand_level=1000,
            use_fast_tree=False)

    def get_node_layout(self) -> mui.FlexBox | None:
        res = mui.VBox([
            self.item_tree.prop(width="100%", height="100%", flex=1)
        ]).prop(flex=1, minWidth="250px", minHeight="300px")
        # if we use virtual tree, we need to set height
        if isinstance(self.item_tree.tree, mui.TanstackJsonLikeTree):
            res.prop(minHeight="300px", height="300px", overflow="hidden")
        else:
            res.prop(minHeight="100px", maxHeight="300px", overflow="hidden")
        return res

    def _expand_validator(self, node: Any):
        if isinstance(node, (dict, )):
            return len(node) < 30
        if isinstance(node, (list, tuple, set)):
            return len(node) < 10
        return False

    async def compute(self, obj: Any) -> None:
        await self.item_tree.set_object(obj, key="obj", expand_level=1000, validator=self._expand_validator)
        await self.item_tree.expand_all()

@register_compute_node(key=ReservedNodeTypes.Expr, name="Eval Expr")
class ExprEvaluatorNode(ComputeNode):
    class OutputDict(TypedDict):
        evaled: Any

    def init_node(self):
        self._editor = mui.SimpleCodeEditor("x", "python")
        self._editor.event_change.on(self._on_change)
        self._saved_value = None

    async def _on_change(self, value: str):
        self._saved_value = value

    def get_node_layout(self) -> mui.FlexBox | None:
        return mui.HBox([
            self._editor.prop(width="100%", height="100%", editorPadding=5)
        ]).prop(flex=1, minWidth="60px", maxWidth="300px")

    async def compute(self, obj: Any) -> OutputDict:
        expr = self._editor.props.value
        expr_obj = compile(expr, '<string>', 'eval')
        evaled = eval(expr_obj, {
            "x": obj
        })
        # save when eval success
        self._saved_value = self._editor.props.value
        return {
            'evaled': evaled
        }

    def state_dict(self) -> Dict[str, Any]:
        res = super().state_dict()
        if self._saved_value is not None:
            res["value"] = self._saved_value
        return res

    @classmethod
    async def from_state_dict(cls, data: Dict[str, Any]):
        res = ComputeNode.from_state_dict_default(data, cls)
        if "value" in data:
            res._editor.props.value = data["value"]
            res._saved_value = data["value"]
        return res
