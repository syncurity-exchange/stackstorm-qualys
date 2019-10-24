from lib.base import QualysBaseAction

__all__ = [
    'GetScanResults'
]


class LaunchScanAction(QualysBaseAction):
    def run(self, scan_ref=None):
        payload = {
            'scan_ref': scan_ref,
            'action': 'fetch',
            'output_format': 'json'
        }
        scan_results = None
        try:
            scan_results = self.connection.request(
                api_call='api/2.0/fo/scan',
                data=payload,
                api_version=2,
                http_method='GET'
            )
            return True, scan_results.json()
        except ConnectionError as e:
            return False, e

