import os

HOST = "brickd"

SHORT_IDENT = os.environ['AUGMENT00_UUID'][:8]

SCHEMA_POST_URL = os.environ['SCHEMA_POST_URL']

INFLUX_AUTH = {
    "host": os.environ['INFLUX_HOST'],
    "port": os.environ['INFLUX_PORT'],
    "user": os.environ['INFLUX_USERNAME'],
    "pass": os.environ['INFLUX_PASSWORD'],
    "db": os.environ['INFLUX_DBNAME'],
    "ssl": os.environ['INFLUX_SSL'] == "True"
}

FIREBASE_AUTH = {
    "google_api_key":  os.environ['GOOGLE_API_KEY'],
    "custom_token_url":  os.environ['FIREBASE_CUSTOM_TOKEN_URL'],
    "auth_domain":  os.environ['FIREBASE_AUTH_DOMAIN'],
    "db_url":  os.environ['FIREBASE_DB_URL'],
    "credentials_path":  os.environ['CREDENTIALS_PATH'],
}

MODULES = [
    ("MenuModule", "navigation", "Navigation"),
    ("InputModule", "inputs", "Inputs"),
    ("SleepModule", "sleep", "Sleep"),
    ("RFIDModule", "rfid", "RFID"),
    ("InfluxModule", "influx", "InfluxDB"),
    ("HttpPushModule", "httppush", "HTTPpush"),
    ("KilnModule", "kiln", "Kiln")
]