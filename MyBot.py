# stdlib
import sys
import datetime
# local
import protocol
import decider


def genlogger(fn):
    LOG = open(fn, mode='wb')
    sys.stderr = LOG
    def f(s, noprefix=False):
        if noprefix:
            LOG.write('{}\n'.format(s))
        else:
            LOG.write('{} {}\n'.format(datetime.datetime.now(), s))
        LOG.flush()
    return f


def listen():
    return sys.stdin.readline().strip()


def tell(s):
    sys.stdout.write(s)
    sys.stdout.write('\n')
    sys.stdout.flush()


def main(deciderprgm=None):
    DECOPT = '--decider'
    LOGOPT = '--log'
    #
    # decider option
    if DECOPT in sys.argv:
        i = sys.argv.index(DECOPT)
        sys.argv.pop(i)
        try:
            decname = sys.argv.pop(i)
        except IndexError:
            raise ValueError('{} option requires an argument'.format(DECOPT))
        try:
            decclass = decider.DECIDERS[decname]
        except KeyError:
            raise ValueError('{} invalid argument "{}"'.format(DECOPT, decname))
    else:
        decname, decclass = decider.DEFAULT
    #
    # decider argument (overrides command-line option)
    if deciderprgm is not None:
        decname, decclass = deciderprgm, decider.DECIDERS[deciderprgm]
    #
    # logger option
    if LOGOPT in sys.argv:
        sys.argv.remove(LOGOPT)
        logger = genlogger('log-'+decname+'.log')
    else:
        logger = None
    #
    # initialize bot
    bot = protocol.Bot(decclass(logger), logger)
    #
    # main loop
    while True:
        heard = listen()
        replies = bot.handle(heard)
        if replies:
            tell('\n'.join(replies))


if __name__ == '__main__':
    main()
