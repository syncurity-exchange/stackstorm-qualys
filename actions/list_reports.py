from lib.base import QualysBaseAction

__all__ = [
    'ListReportsAction'
]


class ListReportsAction(QualysBaseAction):
    def run(self):
        reports = self.connection.listReports()
        return True, self.resultsets.formatter(reports)
