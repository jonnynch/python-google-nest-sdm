"""Traits belonging to doorbell devices."""

from .event import DoorbellChimeEvent, EventTrait
from .traits import TRAIT_MAP, Command


@TRAIT_MAP.register()
class DoorbellChimeTrait(EventTrait):
    """For any device that supports a doorbell chime and related press events."""

    NAME = "sdm.devices.traits.DoorbellChime"
    EVENT_NAME = DoorbellChimeEvent.NAME

    def __init__(self, data: dict, cmd: Command):
        """Initialize DoorbellChime."""
        super().__init__()
        self._data = data
        self._cmd = cmd
