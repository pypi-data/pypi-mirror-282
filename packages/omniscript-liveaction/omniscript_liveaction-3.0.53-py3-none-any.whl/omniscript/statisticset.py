"""Statistic Set class.
"""
# Copyright (c) LiveAction, Inc. 2024. All rights reserved.

import six

from .applicationstatistic import ApplicationStatistic
from .callstatistic import CallStatistic
from .countrystatistic import CountryStatistic
from .nodestatistic import NodeStatistic
from .omniid import OmniId
from .protocolstatistic import ProtocolStatistic
from .summarystatistic import SummaryStatistic


class OmniEngine(object):
    pass


def get_id(props: dict, name: str) -> OmniId:
    id = props.get(name)
    if id:
        return OmniId(id)
    return None


class StatisticSet(object):
    """Statistic Set base class."""
    _statset_prop_dict = {
        'duration': 'duration',
        'totalBytes': 'total_bytes',
        'totalPackets': 'total_packets'
    }

    _engine = None
    """OmniEngine that generated the Statistic Set."""

    duration = 0
    """Duration of the Statistic Set."""

    total_bytes = 0
    """Number of bytes in all the packets."""

    total_packets = 0
    """Number of packets."""

    def __init__(self, engine: OmniEngine, props: dict = None):
        self._engine = engine
        self.duration = StatisticSet.duration
        self.total_bytes = StatisticSet.total_bytes
        self.total_packets = StatisticSet.total_packets
        self._load_set(props)

    def _load_set(self, props: dict):
        """Set attributes from a dictionary."""
        if isinstance(props, dict):
            for k, v in props.items():
                a = StatisticSet._statset_prop_dict.get(k)
                if a is None or not hasattr(self, a):
                    continue
                if isinstance(getattr(self, a), six.string_types):
                    setattr(self, a, v if v else '')
                elif isinstance(getattr(self, a), int):
                    setattr(self, a, int(v) if v else 0)
                else:
                    self.logger.error(f'Unparsed property: {k}: {v}')


class ApplicationStatisticSet(StatisticSet):
    """ApplicationStatisticSet
    """
    _appset_prop_dict = {
        'applications': 'application_stats',
        'resetCount': 'reset_count',
        'timeLimitReached': 'time_limit_reached'
    }

    application_stats = []
    """A list ApplicationStatsitc."""

    reset_count = 0
    """Nuber of times the Statistic Set has been reset."""

    time_limit_reached = False
    """Was the time limit reached."""

    def __init__(self, engine: OmniEngine, props: dict = None):
        StatisticSet.__init__(self, engine, props)
        self.application_stats = []
        self.reset_count = ApplicationStatisticSet.reset_count
        self.time_limit_reached = ApplicationStatisticSet.time_limit_reached
        self._load(props)

    def _load(self, props: dict):
        if isinstance(props, dict):
            for k, v in props.items():
                a = ApplicationStatisticSet._appset_prop_dict.get(k)
                if a is None or not hasattr(self, a):
                    continue
                if isinstance(getattr(self, a), int):
                    setattr(self, a, int(v) if v else 0)
                elif isinstance(getattr(self, a), six.string_types):
                    setattr(self, a, v if v else '')
                elif isinstance(getattr(self, a), list):
                    self.application_stats.clear()
                    for stat in v:
                        if isinstance(stat, dict):
                            self.application_stats.append(ApplicationStatistic(self._engine, stat))
                else:
                    self.logger.error(f'Unparsed property: {k}: {v}')


class CountryStatisticSet(StatisticSet):
    """CountryStatisticSet
    """
    _countryset_prop_dict = {
        'countries': 'country_stats'
    }

    country_stats = []
    """A list CountryStatsitc."""

    def __init__(self, engine: OmniEngine, props: dict = None):
        StatisticSet.__init__(self, engine, props)
        self.country_stats = []
        self._load(props)

    def _load(self, props: dict):
        if isinstance(props, dict):
            countries = props.get('countries')
            if isinstance(countries, list):
                self.country_stats.clear()
                for stat in countries:
                    if isinstance(stat, dict):
                        self.country_stats.append(CountryStatistic(self._engine, stat))


class NodeStatisticSet(StatisticSet):
    """NodeStatisticSet
    """
    _nodeset_prop_dict = {
        'nodes': 'node_stats',
        'resetCount': 'reset_count',
        'timeLimitReached': 'time_limit_reached'
    }

    node_stats = []
    """A list NodeStatsitc."""

    reset_count = 0
    """Nuber of times the Statistic Set has been reset."""

    time_limit_reached = False
    """Was the time limit reached."""

    def __init__(self, engine: OmniEngine, props: dict = None):
        StatisticSet.__init__(self, engine, props)
        self.reset_count = NodeStatisticSet.reset_count
        self.time_limit_reached = NodeStatisticSet.time_limit_reached
        self.node_stats = []
        self._load(props)

    def _load(self, props: dict):
        if isinstance(props, dict):
            for k, v in props.items():
                a = NodeStatisticSet._nodeset_prop_dict.get(k)
                if a is None or not hasattr(self, a):
                    continue
                if isinstance(getattr(self, a), int):
                    setattr(self, a, int(v) if v else 0)
                elif isinstance(getattr(self, a), bool):
                    setattr(self, a, v if v else False)
                elif isinstance(getattr(self, a), list):
                    self.node_stats.clear()
                    for stat in v:
                        if isinstance(stat, dict):
                            self.node_stats.append(NodeStatistic(self._engine, stat))
                else:
                    self.logger.error(f'Unparsed property: {k}: {v}')


class ProtocolStatisticSet(StatisticSet):
    """ProtocolStatisticSet
    """
    _protocolset_prop_dict = {
        'protocols': 'protocol_stats',
        'resetCount': 'reset_count',
        'timeLimitReached': 'time_limit_reached'
    }

    protocol_stats = []
    """A list ProtocolStatsitc."""

    reset_count = 0
    """Nuber of times the Statistic Set has been reset."""

    time_limit_reached = False
    """Was the time limit reached."""

    def __init__(self, engine: OmniEngine, props: dict = None):
        StatisticSet.__init__(self, engine, props)
        self.reset_count = ProtocolStatisticSet.reset_count
        self.time_limit_reached = ProtocolStatisticSet.time_limit_reached
        self.protocol_stats = []
        self._load(props)

    def _load(self, props: dict):
        if isinstance(props, dict):
            for k, v in props.items():
                a = ProtocolStatisticSet._protocolset_prop_dict.get(k)
                if a is None or not hasattr(self, a):
                    continue
                if isinstance(getattr(self, a), int):
                    setattr(self, a, int(v) if v else 0)
                elif isinstance(getattr(self, a), bool):
                    setattr(self, a, v if v else False)
                elif isinstance(getattr(self, a), list):
                    self.protocol_stats.clear()
                    for stat in v:
                        if isinstance(stat, dict):
                            self.protocol_stats.append(ProtocolStatistic(self._engine, stat))
                else:
                    self.logger.error(f'Unparsed property: {k}: {v}')


class SummarySnapshot(object):
    """SummarySnapshot
    """

    _engine = None
    id = None
    name = []
    summary_stats = []

    def __init__(self, engine: OmniEngine, props: dict = None):
        self._engine = engine
        self.id = SummarySnapshot.id
        self.name = SummarySnapshot.name
        self.summary_stats = []
        self._load(props)

    def _load(self, props: dict):
        if isinstance(props, dict):
            self.id = get_id(props, 'id')
            self.name = props.get('name')
            stat_items = props.get('items')
            for stat in stat_items:
                if isinstance(stat, dict):
                    self.summary_stats.append(SummaryStatistic(self._engine, stat))


class SummaryStatisticSet(StatisticSet):
    """SummaryStatisticSet
    """

    current_id = None
    summary_snapshots = []

    def __init__(self, engine: OmniEngine, props: dict = None):
        StatisticSet.__init__(self, engine, props)
        self.current_id = SummaryStatisticSet.current_id
        self.summary_snapshots = []
        self._load(props)

    def _load(self, props: dict):
        if isinstance(props, dict):
            summary = props.get('summary')
            if isinstance(summary, dict):
                current_id = summary.get('currentSnapshotId')
                if current_id:
                    self.current_id = OmniId(current_id)
                snapshot_list = summary.get('snapshots')
                if isinstance(snapshot_list, list):
                    self.summary_snapshots.clear()
                    for snapshot in snapshot_list:
                        self.summary_snapshots.append(SummarySnapshot(self._engine, snapshot))


def create_statistic_set(engine: OmniEngine, props: dict = None) -> StatisticSet:
    from .omniscript import get_id_class_names
    if isinstance(props, dict):
        class_id = OmniId(props['clsid'])
        id_class_names = get_id_class_names()
        class_name = id_class_names[class_id]
        if class_name == 'ApplicationStats':
            return ApplicationStatisticSet(engine, props)
        if class_name == 'CallStats':
            if isinstance(props, dict):
                call = props.get('call')
                if isinstance(call, dict):
                    return CallStatistic(engine, call)
        if class_name == 'CountryStats':
            return CountryStatisticSet(engine, props)
        if class_name == 'NodeStats':
            return NodeStatisticSet(engine, props)
        if class_name == 'ProtocolStats':
            return ProtocolStatisticSet(engine, props)
        elif class_name == 'SummaryStats':
            return SummaryStatisticSet(engine, props)
        else:
            engine.logger.error(f'Unknown Statistic Set type: {class_name}')

    return None
