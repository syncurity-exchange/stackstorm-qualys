from lib.base import QualysBaseAction

__all__ = [
    'GetHostRangeAction'
]


class GetHostRangeAction(QualysBaseAction):
    def run(self, host_start, host_end):
        host = self.connection.getHostRange(host_start, host_end)
        return True, self.resultsets.formatter(host)
