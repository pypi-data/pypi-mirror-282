#!/usr/bin/env python
# coding: utf-8

# Copyright (c) seerai.
# Distributed under the terms of the Modified BSD License.

"""
UI widget for displaying a Dataset or DatasetList
"""
from typing import List
from ._frontend import module_name, module_version
import ipywidgets
import traitlets


class ObjectWidget(ipywidgets.DOMWidget):
    """
    Binds the model & view for the widget and attaches it to the geodesic_widgets module
    """

    _model_name = traitlets.Unicode("ObjectModel").tag(sync=True)
    _model_module = traitlets.Unicode(module_name).tag(sync=True)
    _model_module_version = traitlets.Unicode(module_version).tag(sync=True)
    _view_name = traitlets.Unicode("ObjectView").tag(sync=True)
    _view_module = traitlets.Unicode(module_name).tag(sync=True)
    _view_module_version = traitlets.Unicode(module_version).tag(sync=True)
    object_value = traitlets.List().tag(sync=True)

    def __init__(self, obj={}, **kwargs):
        super().__init__(**kwargs)
        self.object_value = parse_dataset_list(obj)

    def _repr_mimebundle_(self, **kwargs):
        try:
            return super()._repr_mimebundle_(**kwargs)
        except AttributeError as e:
            return {
                "text/plain": repr(self),
                "application/vnd.jupyter.widget-view+json": {
                    "version_major": 2,
                    "version_minor": 0,
                    "model_id": self.model_id,
                },
            }


def parse_dataset_list(raw_dataset_list) -> List[dict]:
    """
    Helper function for parsing out only the fields needed for the dataset list widget,
    and converting them from a nested dict to a list of dicts
    """
    parsed_list = []
    for ds in raw_dataset_list:
        raw_dataset = raw_dataset_list[ds]
        parsed_dataset = {}
        parsed_dataset["alias"] = raw_dataset["item"]["alias"]
        parsed_dataset["name"] = raw_dataset["item"]["name"]
        parsed_dataset["project"] = raw_dataset["project"]
        parsed_dataset["version"] = raw_dataset["item"].get("version", "")
        parsed_dataset["description"] = raw_dataset["item"]["description"]
        parsed_dataset["providers"] = raw_dataset["item"].get("providers", [])
        for provider in parsed_dataset["providers"]:
            if "roles" not in provider:
                provider["roles"] = []
        parsed_dataset["created"] = raw_dataset["item"].get("created", "")
        parsed_dataset["updated"] = raw_dataset["item"].get("updated", "")
        parsed_dataset["item_type"] = raw_dataset["item"].get("item_type", "")
        parsed_dataset["domain"] = raw_dataset["domain"]
        parsed_dataset["category"] = raw_dataset["category"]
        parsed_dataset["type"] = raw_dataset["type"]
        parsed_list.append(parsed_dataset)
    return parsed_list
