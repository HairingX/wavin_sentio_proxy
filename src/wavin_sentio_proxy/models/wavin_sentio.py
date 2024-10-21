from .basemodel import ( WavinModelBase, WavinProxyDatapointKey, WavinProxyDatapoint, WavinProxySetpointKey, WavinProxySetpoint )


class WavinSentio(WavinModelBase):
    def __init__(self, device_number:int, slave_device_number:int, slave_device_model:int):
        super().__init__()

        self._attr_manufacturer="Wavin"
        self._attr_model_name="Sentio"

        self.datapoints = {
            WavinProxyDatapointKey.MODBUS_MODE: WavinProxyDatapoint(read_address=5, divider=1, signed=True),
        }

        self.setpoints = {
            WavinProxySetpointKey.MODBUS_PASSWORD: WavinProxySetpoint(read_address=0, write_address=6, divider=1, min=1, max=65535, signed=True),
        }

        self.set_default_configs()
        
        #place config modifiers here