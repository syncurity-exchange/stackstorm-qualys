from lib.base import QualysBaseAction

from datetime import datetime
import datetime

__all__ = [
    'ListScansAction'
]


class ListScansAction(QualysBaseAction):
    def run(self, launched_after="", state="", target="",
            scan_type="", user_login=""):
        scans = self.connection.listScans(launched_after, state,
                                          target, scan_type, user_login)
        output = self.resultsets.formatter(scans)
        if isinstance(output['launch_datetime'], datetime.date):
            output['launch_datetime'] = output['launch_datetime'].isoformat()

        return True, output
