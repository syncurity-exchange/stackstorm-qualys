from lib.base import QualysBaseAction

__all__ = [
    'GetHostAction'
]


class GetHostAction(QualysBaseAction):
    def run(self, host):
        host = self.connection.getHost(host)  # pylint: disable=too-many-function-args
        return True, self.resultsets.formatter(host)
