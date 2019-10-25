from lib.base import QualysBaseAction

from datetime import datetime
import datetime

__all__ = [
    'ListScanAction'
]


class ListScanAction(QualysBaseAction):
    def run(self, scan_ref, launched_after="", state="",
            scan_type="", user_login=""):

        payload = {
            'action': 'list',
            'scan_ref': scan_ref,
            'launched_after': launched_after,
            'state': state,
            'scan_type': scan_type,
            'user_login': user_login
        }

        scan = self.connection.request(
            api_call='api/2.0/fo/scan',
            data=payload,
            api_version=2,
            http_method='GET'
        )

        output = self.resultsets.formatter(scan)
        if isinstance(output['launch_datetime'], datetime.date):
            output['launch_datetime'] = output['launch_datetime'].isoformat()

        return True, output
