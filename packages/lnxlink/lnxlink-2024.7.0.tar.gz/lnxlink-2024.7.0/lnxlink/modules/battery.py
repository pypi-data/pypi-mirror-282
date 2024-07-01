"""Gets the battery information of connected devices"""
from shutil import which
import jc
from lnxlink.modules.scripts.helpers import syscommand


class Addon:
    """Addon module"""

    def __init__(self, lnxlink):
        """Setup addon"""
        self.name = "Battery"
        self.lnxlink = lnxlink
        if which("upower") is None:
            raise SystemError("System command 'upower' not found")
        self.devices = self._get_devices()

    def exposed_controls(self):
        """Exposes to home assistant"""
        discovery_info = {}
        for device in self.devices:
            att_temp = f"{{{{ value_json.get('{device}', {{}}).get('attributes', {{}}) | tojson }}}}"
            discovery_info[f"Battery {device}"] = {
                "type": "sensor",
                "unit": "%",
                "device_class": "battery",
                "value_template": f"{{{{ value_json.get('{device}', {{}}).get('percent') }}}}",
                "attributes_template": att_temp,
                "enabled": True,
            }
        return discovery_info

    def get_info(self):
        """Gather information from the system"""
        devices = self._get_devices()
        new_devices = set(devices) - set(self.devices)
        disconnected_devices = set(self.devices) - set(devices)
        for device_name in disconnected_devices:
            devices[device_name] = self.devices[device_name]
            self.devices[device_name]["percent"] = None
        self.devices = devices
        if len(new_devices) > 0:
            self.lnxlink.setup_discovery()

        return devices

    def _get_devices(self):
        stdout, _, _ = syscommand("upower --dump")
        upower_json = jc.parse("upower", stdout)

        devices = {}
        for device in upower_json:
            if "detail" in device:
                if "percentage" in device["detail"]:
                    native_path = device.get("native_path", "").split("/")[-1]
                    name = " ".join(
                        [
                            device.get("vendor", ""),
                            device.get("model", ""),
                            device.get("serial", "").replace(":", ""),
                        ]
                    ).strip()
                    if name == "":
                        name = native_path
                    if name != "":
                        devices[name] = {
                            "percent": device["detail"]["percentage"],
                            "attributes": {
                                "vendor": device.get("vendor", ""),
                                "model": device.get("model", ""),
                                "serial": device.get("serial", ""),
                                "native_path": native_path,
                                "rechargeable": device["detail"].get(
                                    "rechargeable", ""
                                ),
                            },
                        }
        return devices
