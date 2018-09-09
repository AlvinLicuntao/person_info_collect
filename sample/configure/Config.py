import configparser, os

config = configparser.ConfigParser()
path = os.path.join(os.path.dirname(__file__), r'..\resources\configure.conf')
print('read config from path {}'.format(path))
config.read(path)