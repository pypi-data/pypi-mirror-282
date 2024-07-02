import os
import json

class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.CONFIG_DIR = os.path.expanduser('~/.sqnethelper')
        self.CONFIG_FILE = os.path.join(self.CONFIG_DIR, 'config.json')
        
        # Default values
        self.defaults = {
            'access_key': '',
            'access_secret': '',
            'region': 'ap-southeast-1',
            'instance_type': 'ecs.t6-c2m1.large',
            'image_id': 'ubuntu_22_04_x64_20G_alibase_20240530.vhd',
            'security_group_id': '',
            'vswitch_id': '',
            'internet_charge_type':'PayByTraffic',
        }

        self.config = self.defaults.copy()
        self.load_config()

    def load_config(self):
        if os.path.exists(self.CONFIG_FILE):
            with open(self.CONFIG_FILE, 'r') as f:
                file_config = json.load(f)
                # Update config with file values, keeping defaults for missing keys
                self.config.update(file_config)

    def save_config(self):
        os.makedirs(self.CONFIG_DIR, exist_ok=True)
        with open(self.CONFIG_FILE, 'w') as f:
            json.dump(self.config, f, indent=2)

    def set_config(self, **kwargs):
        self.config.update(kwargs)
        self.save_config()

    def get_config(self, key):
        return self.config.get(key, self.defaults.get(key))

    def is_configured(self):
        return bool(self.config['access_key'] and self.config['access_secret'])

    # Add property for each config item
    @property
    def access_key(self):
        return self.get_config('access_key')

    @property
    def access_secret(self):
        return self.get_config('access_secret')

    @property
    def region(self):
        return self.get_config('region')

    @property
    def instance_type(self):
        return self.get_config('instance_type')

    @property
    def image_id(self):
        return self.get_config('image_id')

    @property
    def security_group_id(self):
        return self.get_config('security_group_id')

    @property
    def vswitch_id(self):
        return self.get_config('vswitch_id')

    @property
    def internet_charge_type(self):
        return self.get_config('internet_charge_type')




