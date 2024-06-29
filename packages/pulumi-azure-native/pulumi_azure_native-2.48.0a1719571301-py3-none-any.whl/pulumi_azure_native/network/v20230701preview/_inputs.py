# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'ARecordArgs',
    'AaaaRecordArgs',
    'CaaRecordArgs',
    'CnameRecordArgs',
    'DigestArgs',
    'DsRecordArgs',
    'MxRecordArgs',
    'NaptrRecordArgs',
    'NsRecordArgs',
    'PtrRecordArgs',
    'SoaRecordArgs',
    'SrvRecordArgs',
    'SubResource',
    'SubResourceArgs',
    'SubscriptionIdArgs',
    'TlsaRecordArgs',
    'TxtRecordArgs',
]

@pulumi.input_type
class ARecordArgs:
    def __init__(__self__, *,
                 ipv4_address: Optional[pulumi.Input[str]] = None):
        """
        An A record.
        :param pulumi.Input[str] ipv4_address: The IPv4 address of this A record.
        """
        if ipv4_address is not None:
            pulumi.set(__self__, "ipv4_address", ipv4_address)

    @property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 address of this A record.
        """
        return pulumi.get(self, "ipv4_address")

    @ipv4_address.setter
    def ipv4_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv4_address", value)


@pulumi.input_type
class AaaaRecordArgs:
    def __init__(__self__, *,
                 ipv6_address: Optional[pulumi.Input[str]] = None):
        """
        An AAAA record.
        :param pulumi.Input[str] ipv6_address: The IPv6 address of this AAAA record.
        """
        if ipv6_address is not None:
            pulumi.set(__self__, "ipv6_address", ipv6_address)

    @property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv6 address of this AAAA record.
        """
        return pulumi.get(self, "ipv6_address")

    @ipv6_address.setter
    def ipv6_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv6_address", value)


@pulumi.input_type
class CaaRecordArgs:
    def __init__(__self__, *,
                 flags: Optional[pulumi.Input[int]] = None,
                 tag: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        A CAA record.
        :param pulumi.Input[int] flags: The flags for this CAA record as an integer between 0 and 255.
        :param pulumi.Input[str] tag: The tag for this CAA record.
        :param pulumi.Input[str] value: The value for this CAA record.
        """
        if flags is not None:
            pulumi.set(__self__, "flags", flags)
        if tag is not None:
            pulumi.set(__self__, "tag", tag)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def flags(self) -> Optional[pulumi.Input[int]]:
        """
        The flags for this CAA record as an integer between 0 and 255.
        """
        return pulumi.get(self, "flags")

    @flags.setter
    def flags(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "flags", value)

    @property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[str]]:
        """
        The tag for this CAA record.
        """
        return pulumi.get(self, "tag")

    @tag.setter
    def tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tag", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The value for this CAA record.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class CnameRecordArgs:
    def __init__(__self__, *,
                 cname: Optional[pulumi.Input[str]] = None):
        """
        A CNAME record.
        :param pulumi.Input[str] cname: The canonical name for this CNAME record.
        """
        if cname is not None:
            pulumi.set(__self__, "cname", cname)

    @property
    @pulumi.getter
    def cname(self) -> Optional[pulumi.Input[str]]:
        """
        The canonical name for this CNAME record.
        """
        return pulumi.get(self, "cname")

    @cname.setter
    def cname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cname", value)


@pulumi.input_type
class DigestArgs:
    def __init__(__self__, *,
                 algorithm_type: Optional[pulumi.Input[int]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        A digest.
        :param pulumi.Input[int] algorithm_type: The digest algorithm type represents the standard digest algorithm number used to construct the digest. See: https://www.iana.org/assignments/ds-rr-types/ds-rr-types.xhtml
        :param pulumi.Input[str] value: The digest value is a cryptographic hash value of the referenced DNSKEY Resource Record.
        """
        if algorithm_type is not None:
            pulumi.set(__self__, "algorithm_type", algorithm_type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="algorithmType")
    def algorithm_type(self) -> Optional[pulumi.Input[int]]:
        """
        The digest algorithm type represents the standard digest algorithm number used to construct the digest. See: https://www.iana.org/assignments/ds-rr-types/ds-rr-types.xhtml
        """
        return pulumi.get(self, "algorithm_type")

    @algorithm_type.setter
    def algorithm_type(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "algorithm_type", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The digest value is a cryptographic hash value of the referenced DNSKEY Resource Record.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class DsRecordArgs:
    def __init__(__self__, *,
                 algorithm: Optional[pulumi.Input[int]] = None,
                 digest: Optional[pulumi.Input['DigestArgs']] = None,
                 key_tag: Optional[pulumi.Input[int]] = None):
        """
        A DS record. For more information about the DS record format, see RFC 4034: https://www.rfc-editor.org/rfc/rfc4034
        :param pulumi.Input[int] algorithm: The security algorithm type represents the standard security algorithm number of the DNSKEY Resource Record. See: https://www.iana.org/assignments/dns-sec-alg-numbers/dns-sec-alg-numbers.xhtml
        :param pulumi.Input['DigestArgs'] digest: The digest entity.
        :param pulumi.Input[int] key_tag: The key tag value is used to determine which DNSKEY Resource Record is used for signature verification.
        """
        if algorithm is not None:
            pulumi.set(__self__, "algorithm", algorithm)
        if digest is not None:
            pulumi.set(__self__, "digest", digest)
        if key_tag is not None:
            pulumi.set(__self__, "key_tag", key_tag)

    @property
    @pulumi.getter
    def algorithm(self) -> Optional[pulumi.Input[int]]:
        """
        The security algorithm type represents the standard security algorithm number of the DNSKEY Resource Record. See: https://www.iana.org/assignments/dns-sec-alg-numbers/dns-sec-alg-numbers.xhtml
        """
        return pulumi.get(self, "algorithm")

    @algorithm.setter
    def algorithm(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "algorithm", value)

    @property
    @pulumi.getter
    def digest(self) -> Optional[pulumi.Input['DigestArgs']]:
        """
        The digest entity.
        """
        return pulumi.get(self, "digest")

    @digest.setter
    def digest(self, value: Optional[pulumi.Input['DigestArgs']]):
        pulumi.set(self, "digest", value)

    @property
    @pulumi.getter(name="keyTag")
    def key_tag(self) -> Optional[pulumi.Input[int]]:
        """
        The key tag value is used to determine which DNSKEY Resource Record is used for signature verification.
        """
        return pulumi.get(self, "key_tag")

    @key_tag.setter
    def key_tag(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "key_tag", value)


@pulumi.input_type
class MxRecordArgs:
    def __init__(__self__, *,
                 exchange: Optional[pulumi.Input[str]] = None,
                 preference: Optional[pulumi.Input[int]] = None):
        """
        An MX record.
        :param pulumi.Input[str] exchange: The domain name of the mail host for this MX record.
        :param pulumi.Input[int] preference: The preference value for this MX record.
        """
        if exchange is not None:
            pulumi.set(__self__, "exchange", exchange)
        if preference is not None:
            pulumi.set(__self__, "preference", preference)

    @property
    @pulumi.getter
    def exchange(self) -> Optional[pulumi.Input[str]]:
        """
        The domain name of the mail host for this MX record.
        """
        return pulumi.get(self, "exchange")

    @exchange.setter
    def exchange(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "exchange", value)

    @property
    @pulumi.getter
    def preference(self) -> Optional[pulumi.Input[int]]:
        """
        The preference value for this MX record.
        """
        return pulumi.get(self, "preference")

    @preference.setter
    def preference(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "preference", value)


@pulumi.input_type
class NaptrRecordArgs:
    def __init__(__self__, *,
                 flags: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 preference: Optional[pulumi.Input[int]] = None,
                 regexp: Optional[pulumi.Input[str]] = None,
                 replacement: Optional[pulumi.Input[str]] = None,
                 services: Optional[pulumi.Input[str]] = None):
        """
        A NAPTR record. For more information about the NAPTR record format, see RFC 3403: https://www.rfc-editor.org/rfc/rfc3403
        :param pulumi.Input[str] flags: The flags specific to DDDS applications. Values currently defined in RFC 3404 are uppercase and lowercase letters "A", "P", "S", and "U", and the empty string, "". Enclose Flags in quotation marks.
        :param pulumi.Input[int] order: The order in which the NAPTR records MUST be processed in order to accurately represent the ordered list of rules. The ordering is from lowest to highest. Valid values: 0-65535.
        :param pulumi.Input[int] preference: The preference specifies the order in which NAPTR records with equal 'order' values should be processed, low numbers being processed before high numbers. Valid values: 0-65535.
        :param pulumi.Input[str] regexp: The regular expression that the DDDS application uses to convert an input value into an output value. For example: an IP phone system might use a regular expression to convert a phone number that is entered by a user into a SIP URI. Enclose the regular expression in quotation marks. Specify either a value for 'regexp' or a value for 'replacement'.
        :param pulumi.Input[str] replacement: The replacement is a fully qualified domain name (FQDN) of the next domain name that you want the DDDS application to submit a DNS query for. The DDDS application replaces the input value with the value specified for replacement. Specify either a value for 'regexp' or a value for 'replacement'. If you specify a value for 'regexp', specify a dot (.) for 'replacement'.
        :param pulumi.Input[str] services: The services specific to DDDS applications. Enclose Services in quotation marks.
        """
        if flags is not None:
            pulumi.set(__self__, "flags", flags)
        if order is not None:
            pulumi.set(__self__, "order", order)
        if preference is not None:
            pulumi.set(__self__, "preference", preference)
        if regexp is not None:
            pulumi.set(__self__, "regexp", regexp)
        if replacement is not None:
            pulumi.set(__self__, "replacement", replacement)
        if services is not None:
            pulumi.set(__self__, "services", services)

    @property
    @pulumi.getter
    def flags(self) -> Optional[pulumi.Input[str]]:
        """
        The flags specific to DDDS applications. Values currently defined in RFC 3404 are uppercase and lowercase letters "A", "P", "S", and "U", and the empty string, "". Enclose Flags in quotation marks.
        """
        return pulumi.get(self, "flags")

    @flags.setter
    def flags(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "flags", value)

    @property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[int]]:
        """
        The order in which the NAPTR records MUST be processed in order to accurately represent the ordered list of rules. The ordering is from lowest to highest. Valid values: 0-65535.
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "order", value)

    @property
    @pulumi.getter
    def preference(self) -> Optional[pulumi.Input[int]]:
        """
        The preference specifies the order in which NAPTR records with equal 'order' values should be processed, low numbers being processed before high numbers. Valid values: 0-65535.
        """
        return pulumi.get(self, "preference")

    @preference.setter
    def preference(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "preference", value)

    @property
    @pulumi.getter
    def regexp(self) -> Optional[pulumi.Input[str]]:
        """
        The regular expression that the DDDS application uses to convert an input value into an output value. For example: an IP phone system might use a regular expression to convert a phone number that is entered by a user into a SIP URI. Enclose the regular expression in quotation marks. Specify either a value for 'regexp' or a value for 'replacement'.
        """
        return pulumi.get(self, "regexp")

    @regexp.setter
    def regexp(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "regexp", value)

    @property
    @pulumi.getter
    def replacement(self) -> Optional[pulumi.Input[str]]:
        """
        The replacement is a fully qualified domain name (FQDN) of the next domain name that you want the DDDS application to submit a DNS query for. The DDDS application replaces the input value with the value specified for replacement. Specify either a value for 'regexp' or a value for 'replacement'. If you specify a value for 'regexp', specify a dot (.) for 'replacement'.
        """
        return pulumi.get(self, "replacement")

    @replacement.setter
    def replacement(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "replacement", value)

    @property
    @pulumi.getter
    def services(self) -> Optional[pulumi.Input[str]]:
        """
        The services specific to DDDS applications. Enclose Services in quotation marks.
        """
        return pulumi.get(self, "services")

    @services.setter
    def services(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "services", value)


@pulumi.input_type
class NsRecordArgs:
    def __init__(__self__, *,
                 nsdname: Optional[pulumi.Input[str]] = None):
        """
        An NS record.
        :param pulumi.Input[str] nsdname: The name server name for this NS record.
        """
        if nsdname is not None:
            pulumi.set(__self__, "nsdname", nsdname)

    @property
    @pulumi.getter
    def nsdname(self) -> Optional[pulumi.Input[str]]:
        """
        The name server name for this NS record.
        """
        return pulumi.get(self, "nsdname")

    @nsdname.setter
    def nsdname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "nsdname", value)


@pulumi.input_type
class PtrRecordArgs:
    def __init__(__self__, *,
                 ptrdname: Optional[pulumi.Input[str]] = None):
        """
        A PTR record.
        :param pulumi.Input[str] ptrdname: The PTR target domain name for this PTR record.
        """
        if ptrdname is not None:
            pulumi.set(__self__, "ptrdname", ptrdname)

    @property
    @pulumi.getter
    def ptrdname(self) -> Optional[pulumi.Input[str]]:
        """
        The PTR target domain name for this PTR record.
        """
        return pulumi.get(self, "ptrdname")

    @ptrdname.setter
    def ptrdname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ptrdname", value)


@pulumi.input_type
class SoaRecordArgs:
    def __init__(__self__, *,
                 email: Optional[pulumi.Input[str]] = None,
                 expire_time: Optional[pulumi.Input[float]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 minimum_ttl: Optional[pulumi.Input[float]] = None,
                 refresh_time: Optional[pulumi.Input[float]] = None,
                 retry_time: Optional[pulumi.Input[float]] = None,
                 serial_number: Optional[pulumi.Input[float]] = None):
        """
        An SOA record.
        :param pulumi.Input[str] email: The email contact for this SOA record.
        :param pulumi.Input[float] expire_time: The expire time for this SOA record.
        :param pulumi.Input[str] host: The domain name of the authoritative name server for this SOA record.
        :param pulumi.Input[float] minimum_ttl: The minimum value for this SOA record. By convention this is used to determine the negative caching duration.
        :param pulumi.Input[float] refresh_time: The refresh value for this SOA record.
        :param pulumi.Input[float] retry_time: The retry time for this SOA record.
        :param pulumi.Input[float] serial_number: The serial number for this SOA record.
        """
        if email is not None:
            pulumi.set(__self__, "email", email)
        if expire_time is not None:
            pulumi.set(__self__, "expire_time", expire_time)
        if host is not None:
            pulumi.set(__self__, "host", host)
        if minimum_ttl is not None:
            pulumi.set(__self__, "minimum_ttl", minimum_ttl)
        if refresh_time is not None:
            pulumi.set(__self__, "refresh_time", refresh_time)
        if retry_time is not None:
            pulumi.set(__self__, "retry_time", retry_time)
        if serial_number is not None:
            pulumi.set(__self__, "serial_number", serial_number)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        The email contact for this SOA record.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[float]]:
        """
        The expire time for this SOA record.
        """
        return pulumi.get(self, "expire_time")

    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "expire_time", value)

    @property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[str]]:
        """
        The domain name of the authoritative name server for this SOA record.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter(name="minimumTtl")
    def minimum_ttl(self) -> Optional[pulumi.Input[float]]:
        """
        The minimum value for this SOA record. By convention this is used to determine the negative caching duration.
        """
        return pulumi.get(self, "minimum_ttl")

    @minimum_ttl.setter
    def minimum_ttl(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "minimum_ttl", value)

    @property
    @pulumi.getter(name="refreshTime")
    def refresh_time(self) -> Optional[pulumi.Input[float]]:
        """
        The refresh value for this SOA record.
        """
        return pulumi.get(self, "refresh_time")

    @refresh_time.setter
    def refresh_time(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "refresh_time", value)

    @property
    @pulumi.getter(name="retryTime")
    def retry_time(self) -> Optional[pulumi.Input[float]]:
        """
        The retry time for this SOA record.
        """
        return pulumi.get(self, "retry_time")

    @retry_time.setter
    def retry_time(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "retry_time", value)

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[pulumi.Input[float]]:
        """
        The serial number for this SOA record.
        """
        return pulumi.get(self, "serial_number")

    @serial_number.setter
    def serial_number(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "serial_number", value)


@pulumi.input_type
class SrvRecordArgs:
    def __init__(__self__, *,
                 port: Optional[pulumi.Input[int]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None):
        """
        An SRV record.
        :param pulumi.Input[int] port: The port value for this SRV record.
        :param pulumi.Input[int] priority: The priority value for this SRV record.
        :param pulumi.Input[str] target: The target domain name for this SRV record.
        :param pulumi.Input[int] weight: The weight value for this SRV record.
        """
        if port is not None:
            pulumi.set(__self__, "port", port)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if target is not None:
            pulumi.set(__self__, "target", target)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        The port value for this SRV record.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        The priority value for this SRV record.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[str]]:
        """
        The target domain name for this SRV record.
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[int]]:
        """
        The weight value for this SRV record.
        """
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weight", value)


@pulumi.input_type
class SubResource:
    def __init__(__self__, *,
                 id: Optional[str] = None):
        """
        A reference to a another resource
        :param str id: Sub-resource ID. Both absolute resource ID and a relative resource ID are accepted.
               An absolute ID starts with /subscriptions/ and contains the entire ID of the parent resource and the ID of the sub-resource in the end.
               A relative ID replaces the ID of the parent resource with a token '$self', followed by the sub-resource ID itself.
               Example of a relative ID: $self/frontEndConfigurations/my-frontend.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Sub-resource ID. Both absolute resource ID and a relative resource ID are accepted.
        An absolute ID starts with /subscriptions/ and contains the entire ID of the parent resource and the ID of the sub-resource in the end.
        A relative ID replaces the ID of the parent resource with a token '$self', followed by the sub-resource ID itself.
        Example of a relative ID: $self/frontEndConfigurations/my-frontend.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[str]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class SubResourceArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        A reference to a another resource
        :param pulumi.Input[str] id: Sub-resource ID. Both absolute resource ID and a relative resource ID are accepted.
               An absolute ID starts with /subscriptions/ and contains the entire ID of the parent resource and the ID of the sub-resource in the end.
               A relative ID replaces the ID of the parent resource with a token '$self', followed by the sub-resource ID itself.
               Example of a relative ID: $self/frontEndConfigurations/my-frontend.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Sub-resource ID. Both absolute resource ID and a relative resource ID are accepted.
        An absolute ID starts with /subscriptions/ and contains the entire ID of the parent resource and the ID of the sub-resource in the end.
        A relative ID replaces the ID of the parent resource with a token '$self', followed by the sub-resource ID itself.
        Example of a relative ID: $self/frontEndConfigurations/my-frontend.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class SubscriptionIdArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] id: Subscription id in the ARM id format.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Subscription id in the ARM id format.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class TlsaRecordArgs:
    def __init__(__self__, *,
                 cert_association_data: Optional[pulumi.Input[str]] = None,
                 matching_type: Optional[pulumi.Input[int]] = None,
                 selector: Optional[pulumi.Input[int]] = None,
                 usage: Optional[pulumi.Input[int]] = None):
        """
        A TLSA record. For more information about the TLSA record format, see RFC 6698: https://www.rfc-editor.org/rfc/rfc6698
        :param pulumi.Input[str] cert_association_data: This specifies the certificate association data to be matched.
        :param pulumi.Input[int] matching_type: The matching type specifies how the certificate association is presented.
        :param pulumi.Input[int] selector: The selector specifies which part of the TLS certificate presented by the server will be matched against the association data.
        :param pulumi.Input[int] usage: The usage specifies the provided association that will be used to match the certificate presented in the TLS handshake.
        """
        if cert_association_data is not None:
            pulumi.set(__self__, "cert_association_data", cert_association_data)
        if matching_type is not None:
            pulumi.set(__self__, "matching_type", matching_type)
        if selector is not None:
            pulumi.set(__self__, "selector", selector)
        if usage is not None:
            pulumi.set(__self__, "usage", usage)

    @property
    @pulumi.getter(name="certAssociationData")
    def cert_association_data(self) -> Optional[pulumi.Input[str]]:
        """
        This specifies the certificate association data to be matched.
        """
        return pulumi.get(self, "cert_association_data")

    @cert_association_data.setter
    def cert_association_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert_association_data", value)

    @property
    @pulumi.getter(name="matchingType")
    def matching_type(self) -> Optional[pulumi.Input[int]]:
        """
        The matching type specifies how the certificate association is presented.
        """
        return pulumi.get(self, "matching_type")

    @matching_type.setter
    def matching_type(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "matching_type", value)

    @property
    @pulumi.getter
    def selector(self) -> Optional[pulumi.Input[int]]:
        """
        The selector specifies which part of the TLS certificate presented by the server will be matched against the association data.
        """
        return pulumi.get(self, "selector")

    @selector.setter
    def selector(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "selector", value)

    @property
    @pulumi.getter
    def usage(self) -> Optional[pulumi.Input[int]]:
        """
        The usage specifies the provided association that will be used to match the certificate presented in the TLS handshake.
        """
        return pulumi.get(self, "usage")

    @usage.setter
    def usage(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "usage", value)


@pulumi.input_type
class TxtRecordArgs:
    def __init__(__self__, *,
                 value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        A TXT record.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] value: The text value of this TXT record.
        """
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The text value of this TXT record.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "value", value)


