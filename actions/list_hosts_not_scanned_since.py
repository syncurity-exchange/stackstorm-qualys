from lib.base import QualysBaseAction

__all__ = [
    'ListHostsNotScannedSinceAction'
]


class ListHostsNotScannedSinceAction(QualysBaseAction):
    def run(self, days):
        hosts = self.connection.notScannedSince(days)
        return True, self.resultsets.formatter(hosts)
