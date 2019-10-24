from lib.base import QualysBaseAction

from datetime import datetime
import datetime
import json

__all__ = [
    'LaunchScanAction'
]


class LaunchScanAction(QualysBaseAction):
    def run(self, title, option_title, iscanner_name,
            asset_groups=None, ip=None):
        scan = self.connection.launchScan(title, option_title,
                                          iscanner_name, asset_groups, ip)
        output = self.resultsets.formatter(scan)
        if isinstance(output['launch_datetime'], datetime.date):
            output['launch_datetime'] = output['launch_datetime'].isoformat()
        return True, output
