# Copyright (c) 2017-2018. The SimGrid Team. All rights reserved.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the license (GNU LGPL) which comes with this package.

import simgrid, sys

# This example does not much: It just spans over-polite actor that yield a large amount
# of time before ending.
#
# This serves as an example for the simgrid.yield() function, with which an actor can request
# to be rescheduled after the other actor that are ready at the current timestamp.
#
# It can also be used to benchmark our context-switching mechanism.

# Main function of the Yielder process
class Yielder:
    number_of_yields = 0
    def __init__(self, *args):
        self.number_of_yields = int(args[0])
    def __call__(self):
        for i in range(self.number_of_yields):
            simgrid.yield_()
        simgrid.info("I yielded {:d} times. Goodbye now!".format(self.number_of_yields))

if __name__ == '__main__':
    e = simgrid.Engine(sys.argv)

    e.load_platform(sys.argv[1])             # Load the platform description
    e.register_actor("yielder", Yielder)  # Register the class representing the actors

    e.load_deployment(sys.argv[2])

    e.run() # - Run the simulation