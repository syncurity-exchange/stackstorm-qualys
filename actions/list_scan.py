from lib.base import QualysBaseAction

from qualysapi.api_objects import Scan

from datetime import datetime
import datetime
from lxml import objectify

__all__ = [
    'ListScanAction'
]


class ListScanAction(QualysBaseAction):
    def run(self, scan_ref, launched_after="", target="", state="",
            scan_type="", user_login=""):

        payload = {
            'scan_ref': scan_ref,
            'launched_after': launched_after,
            'state': state,
            'type': scan_type,
            'target': target,
            'user_login': user_login
        }

        scan = self.list_scan(**payload)

        output = self.resultsets.formatter(scan)
        if isinstance(output['launch_datetime'], datetime.date):
            output['launch_datetime'] = output['launch_datetime'].isoformat()

        return True, output

    def list_scan(self, scan_ref, launched_after="", state="", type="", target="", user_login=""):
        """"# 'scan_ref' the scan to return info for
        # 'launched_after' parameter accepts a date in the format: YYYY-MM-DD
        # 'state' parameter accepts "Running", "Paused", "Canceled", "Finished", "Error",
        # "Queued", and "Loading".
        # 'title' parameter accepts a string
        # 'type' parameter accepts "On-Demand", and "Scheduled".
        # 'user_login' parameter accepts a user name (string)"""
        call = '/api/2.0/fo/scan/'
        parameters = {'action': 'list', 'scan_ref': scan_ref, 'show_ags': 1, 'show_op': 1,
                      'show_status': 1}
        if launched_after != "":
            parameters['launched_after_datetime'] = launched_after

        if state != "":
            parameters['state'] = state

        if target != "":
            parameters['target'] = target

        if type != "":
            parameters['type'] = type

        if user_login != "":
            parameters['user_login'] = user_login

        scanlist = objectify.fromstring(self.connection.request(call, parameters).encode('utf-8'))
        scanArray = []
        for scan in scanlist.RESPONSE.SCAN_LIST.SCAN:
            try:
                agList = []
                for ag in scan.ASSET_GROUP_TITLE_LIST.ASSET_GROUP_TITLE:
                    agList.append(ag)
            except AttributeError:
                agList = []

            scanArray.append(Scan(agList,
                                  scan.find('DURATION'),
                                  scan.find('LAUNCH_DATETIME'),
                                  scan.find('OPTION_PROFILE.TITLE'),
                                  scan.find('PROCESSED'),
                                  scan.find('REF'),
                                  scan.find('STATUS'),
                                  scan.find('TARGET'),
                                  scan.find('TITLE'),
                                  scan.find('TYPE'),
                                  scan.find('USER_LOGIN')
                                  )
                             )

        return scanArray
