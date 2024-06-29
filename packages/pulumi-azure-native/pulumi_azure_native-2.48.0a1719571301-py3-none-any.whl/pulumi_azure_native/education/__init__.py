# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .get_lab import *
from .get_student import *
from .lab import *
from .student import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.education.v20211201preview as __v20211201preview
    v20211201preview = __v20211201preview
else:
    v20211201preview = _utilities.lazy_import('pulumi_azure_native.education.v20211201preview')

