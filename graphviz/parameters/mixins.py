"""Mixin classes used to inherit parameter functionality."""

import typing

from . import engines
from . import formats
from . import renderers
from . import formatters

__all__ = ['Parameters']


class Parameters(engines.Engine, formats.Format,
                 renderers.Renderer, formatters.Formatter):
    """Parameters for calling ``graphviz.render()`` and ``graphviz.pipe()``."""

    def __init__(self, format=None, engine=None, **kwargs):
        super().__init__(format=format, engine=engine, **kwargs)

    def _get_parameters(self, *,
                        engine: typing.Optional[str] = None,
                        format: typing.Optional[str] = None,
                        renderer: typing.Optional[str] = None,
                        formatter: typing.Optional[str] = None,
                        verify: bool = False,
                        **kwargs):
        if engine is None:
            engine = self._engine
        elif verify:
            self._verify_engine(engine)

        if format is None:
            format = self._format
        elif verify:
            self._verify_format(format)

        if renderer is None:
            renderer = self._renderer
        elif verify:
            self._verify_renderer(renderer)

        if formatter is None:
            formatter = self._formatter
        elif verify:
            self._verify_formatter(formatter)

        kwargs.update(engine=engine, format=format,
                      renderer=renderer, formatter=formatter)
        return kwargs