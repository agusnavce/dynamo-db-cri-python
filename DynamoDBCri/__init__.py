from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution('Dynamo DB CRI Python').version
except DistributionNotFound:
    __version__ = '(local)'
