# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .get_shared_private_link_resource import *
from .get_target import *
from .get_watcher import *
from .shared_private_link_resource import *
from .target import *
from .watcher import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.databasewatcher.v20230901preview as __v20230901preview
    v20230901preview = __v20230901preview
else:
    v20230901preview = _utilities.lazy_import('pulumi_azure_native.databasewatcher.v20230901preview')

