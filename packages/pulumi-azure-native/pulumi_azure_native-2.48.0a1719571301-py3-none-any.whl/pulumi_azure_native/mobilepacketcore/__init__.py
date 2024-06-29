# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .amf_deployment import *
from .cluster_service import *
from .get_amf_deployment import *
from .get_cluster_service import *
from .get_network_function import *
from .get_nrf_deployment import *
from .get_nssf_deployment import *
from .get_observability_service import *
from .get_smf_deployment import *
from .get_upf_deployment import *
from .network_function import *
from .nrf_deployment import *
from .nssf_deployment import *
from .observability_service import *
from .smf_deployment import *
from .upf_deployment import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.mobilepacketcore.v20230515preview as __v20230515preview
    v20230515preview = __v20230515preview
    import pulumi_azure_native.mobilepacketcore.v20231015preview as __v20231015preview
    v20231015preview = __v20231015preview
else:
    v20230515preview = _utilities.lazy_import('pulumi_azure_native.mobilepacketcore.v20230515preview')
    v20231015preview = _utilities.lazy_import('pulumi_azure_native.mobilepacketcore.v20231015preview')

