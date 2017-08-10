import os

HOST = "brickd"

SHORT_IDENT = os.environ['AUGMENT00_UUID'][:8]

INFLUX_AUTH = {
    "host": os.environ['INFLUX_HOST'],
    "port": os.environ['INFLUX_PORT'],
    "user": os.environ['INFLUX_USERNAME'],
    "pass": os.environ['INFLUX_PASSWORD'],
    "db": os.environ['INFLUX_DBNAME'],
}
