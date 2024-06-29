# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'LiveEventEncodingType',
    'LiveEventInputProtocol',
    'StreamOptionsFlag',
    'StretchMode',
]


class LiveEventEncodingType(str, Enum):
    """
    Live event type. When encodingType is set to PassthroughBasic or PassthroughStandard, the service simply passes through the incoming video and audio layer(s) to the output. When encodingType is set to Standard or Premium1080p, a live encoder transcodes the incoming stream into multiple bitrates or layers. See https://go.microsoft.com/fwlink/?linkid=2095101 for more information. This property cannot be modified after the live event is created.
    """
    NONE = "None"
    """
    This is the same as PassthroughStandard, please see description below. This enumeration value is being deprecated.
    """
    STANDARD = "Standard"
    """
    A contribution live encoder sends a single bitrate stream to the live event and Media Services creates multiple bitrate streams. The output cannot exceed 720p in resolution.
    """
    PREMIUM1080P = "Premium1080p"
    """
    A contribution live encoder sends a single bitrate stream to the live event and Media Services creates multiple bitrate streams. The output cannot exceed 1080p in resolution.
    """
    PASSTHROUGH_BASIC = "PassthroughBasic"
    """
    The ingested stream passes through the live event from the contribution encoder without any further processing. In the PassthroughBasic mode, ingestion is limited to up to 5Mbps and only 1 concurrent live output is allowed. Live transcription is not available.
    """
    PASSTHROUGH_STANDARD = "PassthroughStandard"
    """
    The ingested stream passes through the live event from the contribution encoder without any further processing. Live transcription is available. Ingestion bitrate limits are much higher and up to 3 concurrent live outputs are allowed.
    """


class LiveEventInputProtocol(str, Enum):
    """
    The input protocol for the live event. This is specified at creation time and cannot be updated.
    """
    FRAGMENTED_MP4 = "FragmentedMP4"
    """
    Smooth Streaming input will be sent by the contribution encoder to the live event.
    """
    RTMP = "RTMP"
    """
    RTMP input will be sent by the contribution encoder to the live event.
    """


class StreamOptionsFlag(str, Enum):
    DEFAULT = "Default"
    """
    Live streaming with no special latency optimizations.
    """
    LOW_LATENCY = "LowLatency"
    """
    The live event provides lower end to end latency by reducing its internal buffers.
    """
    LOW_LATENCY_V2 = "LowLatencyV2"
    """
    The live event is optimized for end to end latency. This option is only available for encoding live events with RTMP input. The outputs can be streamed using HLS or DASH formats. The outputs' archive or DVR rewind length is limited to 6 hours. Use "LowLatency" stream option for all other scenarios.
    """


class StretchMode(str, Enum):
    """
    Specifies how the input video will be resized to fit the desired output resolution(s). Default is None
    """
    NONE = "None"
    """
    Strictly respects the output resolution specified in the encoding preset without considering the pixel aspect ratio or display aspect ratio of the input video.
    """
    AUTO_SIZE = "AutoSize"
    """
    Override the output resolution, and change it to match the display aspect ratio of the input, without padding. For example, if the input is 1920x1080 and the encoding preset asks for 1280x1280, then the value in the preset is overridden, and the output will be at 1280x720, which maintains the input aspect ratio of 16:9.
    """
    AUTO_FIT = "AutoFit"
    """
    Pad the output (with either letterbox or pillar box) to honor the output resolution, while ensuring that the active video region in the output has the same aspect ratio as the input. For example, if the input is 1920x1080 and the encoding preset asks for 1280x1280, then the output will be at 1280x1280, which contains an inner rectangle of 1280x720 at aspect ratio of 16:9, and pillar box regions 280 pixels wide at the left and right.
    """
