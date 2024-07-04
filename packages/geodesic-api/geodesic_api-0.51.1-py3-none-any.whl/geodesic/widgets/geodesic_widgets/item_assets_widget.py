#!/usr/bin/env python
# coding: utf-8

# Copyright (c) seerai.
# Distributed under the terms of the Modified BSD License.

"""
UI widget for displaying ItemAssets
"""

from ._frontend import module_version
import ipywidgets
import traitlets


class ItemAssetsWidget(ipywidgets.DOMWidget):
    """
    Binds the model & view for the widget and attaches it to the geodesic_widgets module
    """

    _model_name = traitlets.Unicode("ItemAssetsModel").tag(sync=True)
    _model_module = traitlets.Unicode("geodesic_widgets").tag(sync=True)
    _view_name = traitlets.Unicode("ItemAssetsView").tag(sync=True)
    _view_module = traitlets.Unicode("geodesic_widgets").tag(sync=True)
    _model_module_version = traitlets.Unicode(module_version).tag(sync=True)
    _view_module_version = traitlets.Unicode(module_version).tag(sync=True)
    object_value = traitlets.Dict().tag(sync=True)

    def __init__(self, obj={}, **kwargs):
        super().__init__(**kwargs)
        self.object_value = dict(obj)

    def _repr_mimebundle_(self, **kwargs):
        try:
            return super()._repr_mimebundle_(**kwargs)
        except AttributeError:
            return {
                "text/plain": repr(self),
                "application/vnd.jupyter.widget-view+json": {
                    "version_major": 2,
                    "version_minor": 0,
                    "model_id": self.model_id,
                },
            }
