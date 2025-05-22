from configparser import ConfigParser

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)

FAST_API_RELOAD = config.getboolean('server', 'reload', fallback=False)
FAST_API_PORT = config.getint('server', 'port')
