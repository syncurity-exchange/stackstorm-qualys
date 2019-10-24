from lib.base import QualysBaseAction

__all__ = [
    'GetReportAction'
]


class GetReportAction(QualysBaseAction):
    def run(self, id):
        reports = self.connection.listReports(id)
        return True, self.resultsets.formatter(reports[0])
