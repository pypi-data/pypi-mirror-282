"""Module responsible for configuration."""
import numbers
import typing

import voluptuous as vol
from zigpy.config import (CONF_DEVICE, CONF_DEVICE_PATH,  # noqa: F401
                          CONF_NWK, CONF_NWK_CHANNEL, CONF_NWK_CHANNELS,
                          CONF_NWK_EXTENDED_PAN_ID, CONF_NWK_KEY,
                          CONF_NWK_KEY_SEQ, CONF_NWK_PAN_ID,
                          CONF_NWK_TC_ADDRESS, CONF_NWK_TC_LINK_KEY,
                          CONF_NWK_UPDATE_ID, CONFIG_SCHEMA, SCHEMA_DEVICE,
                          cv_boolean)

LOG_FILE_NAME = "zigpy-zboss.log"
SERIAL_LOG_FILE_NAME = "serial-zigpy-zboss.log"

ConfigType = typing.Dict[str, typing.Any]

VolPositiveNumber = vol.All(numbers.Real, vol.Range(min=0))

CONF_DEVICE_BAUDRATE = "baudrate"
CONF_DEVICE_FLOW_CONTROL = "flow_control"
CONF_DEVICE_BAUDRATE_DEFAULT = 115_200
CONF_DEVICE_FLOW_CONTROL_DEFAULT = None

SCHEMA_DEVICE = SCHEMA_DEVICE.extend(
    {
        vol.Optional(
            CONF_DEVICE_BAUDRATE, default=CONF_DEVICE_BAUDRATE_DEFAULT): int,
        vol.Optional(
            CONF_DEVICE_FLOW_CONTROL,
            default=CONF_DEVICE_FLOW_CONTROL_DEFAULT): vol.In(
            ("hardware", "software", None)
        ),
    }
)


def keys_have_same_length(*keys):
    """Raise an error if values don't have the same length."""
    def validator(config):
        lengths = [len(config[k]) for k in keys]

        if len(set(lengths)) != 1:
            raise vol.Invalid(
                f"Values for {keys} must all have the same length: {lengths}"
            )

        return config

    return validator


CONF_ZBOSS_CONFIG = "zboss_config"
CONF_TX_POWER = "tx_power"
CONF_LED_MODE = "led_mode"
CONF_SKIP_BOOTLOADER = "skip_bootloader"
CONF_REQ_TIMEOUT = "request_timeout"
CONF_AUTO_RECONNECT_RETRY_DELAY = "auto_reconnect_retry_delay"
CONF_MAX_CONCURRENT_REQUESTS = "max_concurrent_requests"
CONF_CONNECT_RTS_STATES = "connect_rts_pin_states"
CONF_CONNECT_DTR_STATES = "connect_dtr_pin_states"

CONFIG_SCHEMA = CONFIG_SCHEMA.extend(
    {
        vol.Required(CONF_DEVICE): SCHEMA_DEVICE,
        vol.Optional(CONF_ZBOSS_CONFIG, default={}): vol.Schema(
            vol.All(
                {
                    vol.Optional(CONF_TX_POWER, default=None): vol.Any(
                        None, vol.All(int, vol.Range(min=-22, max=22))
                    ),
                    vol.Optional(
                        CONF_REQ_TIMEOUT, default=15): VolPositiveNumber,
                    vol.Optional(
                        CONF_AUTO_RECONNECT_RETRY_DELAY, default=5
                    ): VolPositiveNumber,
                    vol.Optional(
                        CONF_SKIP_BOOTLOADER, default=True): cv_boolean,
                    vol.Optional(CONF_LED_MODE, default=None): vol.Any(None),
                    vol.Optional(
                        CONF_MAX_CONCURRENT_REQUESTS, default="auto"): vol.Any(
                        "auto", VolPositiveNumber
                    ),
                    vol.Optional(
                        CONF_CONNECT_RTS_STATES, default=[False, True, False]
                    ): vol.Schema([cv_boolean]),
                    vol.Optional(
                        CONF_CONNECT_DTR_STATES, default=[False, False, False]
                    ): vol.Schema([cv_boolean]),
                },
                keys_have_same_length(
                    CONF_CONNECT_RTS_STATES, CONF_CONNECT_DTR_STATES),
            )
        ),
    }
)
