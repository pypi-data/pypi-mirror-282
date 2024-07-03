from datetime import date, datetime
from enum import Enum
from typing import Union
from .tariff_information import TariffInformation
from .channel import ChannelType


class SpikeStatus(Enum):
    NO_SPIKE = "none"
    POTENTIAL = "potential"
    SPIKE = "spike"

    def from_str(s: Union[str, None]):
        possible = list(filter(lambda t: t.value == s, SpikeStatus))
        if len(possible) > 0:
            return possible[0]


class Descriptor(Enum):
    NEGATIVE = "negative"
    EXTREMELY_LOW = "extremelyLow"
    VERY_LOW = "veryLow"
    LOW = "low"
    NEUTRAL = "neutral"
    HIGH = "high"
    SPIKE = "spike"

    def from_str(s: Union[str, None]):
        possible = list(filter(lambda t: t.value == s, Descriptor))
        if len(possible) > 0:
            return possible[0]


class Interval(object):
    """Length of the interval in minutes."""
    duration: str
    """NEM spot price. This is the price generators get paid to generate electricity, and what drives the variable component of your perKwh price"""
    spot_per_kwh: float
    """Number of cents you will pay per kilowatt-hour (c/kWh)"""
    per_kwh: float
    """Date the interval belongs to. This may be different to the date component of nemTime, as the last interval of the day ends at 12:30 the following day. Formatted as a ISO 8601 date"""
    date: date
    """The interval's NEM time. This represents the time at the end of the interval UTC+10. Formatted as a ISO 8601 time"""
    nem_time: datetime
    """Start time of the interval in UTC. Formatted as a ISO 8601 time"""
    start_time: datetime
    """End time of the interval in UTC. Formatted as a ISO 8601 time"""
    end_time: datetime
    """Percentage of renewables in the grid"""
    renewables: float
    """Meter channel type"""
    channel_type: ChannelType
    """Indicates whether this interval will potentially spike, or is currently in a spike state"""
    spike_status: SpikeStatus
    """Describes the current price. Gives you an indication of how cheap the price is in relation to the average VMO and DMO. Note: Negative is no longer used. It has been replaced with extremelyLow."""
    descriptor: Descriptor

    tariff_information: TariffInformation

    def __init__(
        self,
        duration: float,
        spot_per_kwh: float,
        per_kwh: float,
        date: date,
        nem_time: datetime,
        start_time: datetime,
        end_time: datetime,
        renewables: float,
        channel_type: str,
        spike_status: str,
        descriptor: str,
        **kwargs
    ):
        self.duration = duration
        self.spot_per_kwh = spot_per_kwh
        self.per_kwh = per_kwh
        self.date = date
        self.nem_time = nem_time
        self.start_time = start_time
        self.end_time = end_time
        self.renewables = renewables
        self.channel_type = ChannelType.from_str(channel_type)
        self.spike_status = SpikeStatus.from_str(spike_status)
        self.descriptor = Descriptor.from_str(descriptor)
        self.tariff_information = kwargs.get('tariff_information')

    def to_dict(self) -> dict:
        return {
            "duration": self.duration,
            "spot_per_kwh": self.spot_per_kwh,
            "per_kwh": self.per_kwh,
            "date": self.date,
            "nem_time": self.nem_time,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "renewables": self.renewables,
            "channel_type": self.channel_type,
            "spike_status": self.spike_status,
            "descriptor": self.descriptor
        }

    def __repr__(self) -> str:
        return self.to_str()

    def to_str(self):
        return str(self.to_dict())
