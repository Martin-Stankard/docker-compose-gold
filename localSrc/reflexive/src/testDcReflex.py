#pytest
import os

name = os.getenv('PROFILE')
print(f"Hello, {name}!")



print("hello from reflexive land")

#run docker compose up from /app....

#maybe a check on containers up and running test every five seconds until ALL UP

#Begin tests

# docker network ls, foreach network, docker network inspect <network_name> | grep "Containers" | wc -l
# docker network inspect <network_name>

# Networks can be configured with static IP addresses by setting the ipv4_address and/or ipv6_address for each attached network.
# todo, leverage for aws...probably never if deploy starts at github.

# docker network create --subnet
# why .... maybe...lol...this stablilizes and 2 forked projects off of this stabilize and are managed in one of these.


# brute force port scan on all containers in network




# finally kick off "normal, non reflexive testing" in pytest, across golden-internal-network/ and/or golden-external-network/