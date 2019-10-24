from lib.base import QualysBaseAction

from datetime import datetime
import datetime

__all__ = [
    'ListReportsAction'
]


class ListReportsAction(QualysBaseAction):
    def run(self):
        reports = self.connection.listReports()
        output = self.resultsets.formatter(reports)
        if isinstance(output['launch_datetime'], datetime.date):
            output['launch_datetime'] = output['launch_datetime'].isoformat()
        return True, self.resultsets.formatter(reports)
