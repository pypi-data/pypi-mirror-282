"""Base class for config object for the application."""

from termcolor import cprint
import colorama

from .constants import (ERROR_COLOUR, CORRUPT_FILE_MSG, MISSING_ATTR_MSG,
                        STATUS_OK, FIELD, NOT_IN_DICT)

colorama.init()

MODULE_COLOUR = 'red'


class Config():
    """
    The class takes a path to a json file and if valid, returns a config dict.

    Attributes
    ----------

    path: str
        The path to the config file

    attrs: dict[str, list[type]
        The dict keys are the fields that are expected in the config json
        The dict item holds a list of allowed types for each files

        If there are attrs, then the config is validated.

    create: bool
        Whether or not the config should be created if missing.
        Defaults to False.
        (The individual sub-classes implement the function.)
    """

    def __init__(
            self,
            path: str,
            defaults: dict[str, str] = {}
            ):
        self.STATUS_OK = STATUS_OK
        self.path = path
        self.defaults = defaults
        self.config = self._get_config()
        for key, item in self.config.items():
            self.__dict__[key] = item

    def __repr__(self):
        output = ['Config:']
        for key, item in self.__dict__.items():
            output .append(f'{key}: {item}')
        return '\n'.join(output)

    def _get_config(self) -> dict[str, object]:
        # Return config, if contents are valid.
        config = self._read_config()

        if config:
            return config

        if self.defaults:
            return self.defaults
        return {}

    def update(self, field: str, value: object, force: bool = False) -> None:
        """Update the value of an attribute in config."""
        if not force and field not in self.__dict__['config']:
            cprint(f'{FIELD} {field} {NOT_IN_DICT}', ERROR_COLOUR)
            return

        self.__dict__['config'][field] = value
