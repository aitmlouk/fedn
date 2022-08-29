from fedn.network.combiner.interfaces import CombinerUnavailableError
from fedn.network.loadbalancer.loadbalancerbase import LoadBalancerBase


class LeastPacked(LoadBalancerBase):

    def __init__(self, network):
        super().__init__(network)

    def find_combiner(self):
        """ Find the first available combiner. """

        for combiner in self.network.get_combiners():
            if combiner.allowing_clients():
                return combiner
        return None
