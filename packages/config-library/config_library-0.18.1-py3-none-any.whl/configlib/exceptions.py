# -*- coding=utf-8 -*-
r"""

"""


class ConfigLibError(Exception):
    r"""
    any exception coming from configlib
    """
    pass


class ConfigNotFoundError(ConfigLibError, FileNotFoundError):
    r"""
    A configuration file could not be found
    """
    pass


class NotSupportedError(ConfigLibError, NotImplementedError):
    r"""
    a configuration file could not be parsed
    """
    pass


class ValidationError(ConfigLibError):
    r"""
    a configuration could not be validated
    """
    def pretty(self) -> str:
        lines = []
        for error in self.args[0]:
            lines.append(f"- {error['type']}: {error['msg']} ({'->'.join(error['loc'])})")

        return ''.join(lines)
