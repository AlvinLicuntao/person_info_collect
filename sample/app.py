from model import PersonModel
from alvin.page.Index import Index
from configure import config
import logging, time, os


def main():
    # 日志配置
    log_file = os.getcwd() + r'\resources\log\{}.log'.format(time.strftime("%Y-%m-%d", time.localtime()))
    format_str = '%(asctime)s %(levelname)s %(module)s %(filename)s[line:%(lineno)d]: %(message)s'
    logging.basicConfig(filename=log_file, level=config.get('logging', 'level'), format=format_str)
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(logging.Formatter(format_str))
    logging.getLogger('').addHandler(console)
    logging.info('Application start!')
    # 启动程序
    Index(config)


if __name__ == '__main__':
    main()
