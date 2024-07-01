"""Assign hotkeys to run commands"""
import json
import logging
from requests import post, get
from lnxlink.modules.scripts.helpers import import_install_package, syscommand


logger = logging.getLogger("lnxlink")


class Addon:
    """Addon module"""

    def __init__(self, lnxlink):
        """Setup addon"""
        self.name = "Keyboard Hotkeys"
        self.lnxlink = lnxlink
        self.started = False
        self.lib = {}
        self.hass_url = self.lnxlink.config["hass_url"]
        hass_api = self.lnxlink.config["hass_api"]
        self.hass_headers = {
            "Authorization": f"Bearer {hass_api}",
            "content-type": "application/json",
        }
        if hass_api is None or self.hass_url is None:
            raise SystemError(
                "Configuration option 'hass_api' or 'hass_url' is not set"
            )
        if not self._test_connection():
            raise SystemError("Can't connect to Home Assistant")
        self._requirements()

    def _requirements(self):
        self.lib = {
            "xlib_hotkeys": import_install_package(
                "xlib-hotkeys", ">=2024.3.0", "xlib_hotkeys"
            ),
        }

    def get_info(self):
        """Gather information from the system"""
        if not self.started and self.lnxlink.display is not None:
            hm = self.lib["xlib_hotkeys"].HotKeysManager(self.lnxlink.display)
            actions = self.lnxlink.config["settings"]["hotkeys"]
            for action in actions:
                action_key = action.pop("key")
                hm.hotkeys[action_key] = lambda action=action: self._activate(action)
            hm.start()
            self.started = True

    def _activate(self, act):
        response = ""
        action = act.copy()
        action_type = action.pop("type")
        if action_type == "action":
            url_action = action.pop("service").replace(".", "/")
            url = f"{self.hass_url}/api/services/{url_action}"
            post(url, headers=self.hass_headers, data=json.dumps(action))
        elif action_type == "state":
            url = f"{self.hass_url}/api/states/light.myroom"
            response = get(url, headers=self.hass_headers).json()["state"]
        elif action_type in ["conversation", "popup"]:
            url = f"{self.hass_url}/api/conversation/process"
            if action_type == "conversation":
                response = post(url, headers=self.hass_headers, data=json.dumps(action))
            elif action_type == "popup":
                stdout, _, _ = syscommand(
                    f"timeout 15s zenity --display='{self.lnxlink.display}' "
                    + "--entry --title='Home Assistant' --text='Sentence:'",
                    timeout=15,
                )
                if stdout == "":
                    return
                action = {"text": stdout}
                response = post(url, headers=self.hass_headers, data=json.dumps(action))
            speech = response.json()["response"]["speech"]
            if "plain" in speech:
                response = speech["plain"]["speech"]
            elif "ssml" in speech:
                response = speech["ssml"]["speech"]
        if response != "":
            logger.info("Home Assistant response: %s", response)
            syscommand(
                f'zenity --display="{self.lnxlink.display}" --notification --text="{response}"'
            )

    def _test_connection(self):
        try:
            response = get(f"{self.hass_url}/api/", headers=self.hass_headers)
            if response.ok:
                return True
        except Exception:
            return False
        return False
