import os

name = os.getenv('ZAB')
print(f"Hello, ZAB env variable defined in ../../../docker-compose.yml: {name}!")

print("hello from reflexive service land...")

# Create and save a file hello.txt with content "asdf"
with open("hello.txt", "w") as file:
    file.write("asdf")

print("file write did not crash out at least ...")

# Print out the equivalent of an "ls ./" command
print("Contents of current directory:")
for item in os.listdir("."):
    print(item)

# Check if the file hello.txt exists and print its contents
if os.path.isfile("hello.txt"):
    print("hello.txt exists")
    with open("hello.txt", "r") as file:
        content = file.read()
        print(f"Contents of hello.txt: {content}")
else:
    print("hello.txt does not exist")

# possible top to bottom conceptual redeau https://github.com/jpetazzo/dind
#If you want to run Docker-in-Docker today, all you need to do is:

#docker run --privileged -d docker:dind



#Begin tests

# docker network ls, foreach network, docker network inspect <network_name> | grep "Containers" | wc -l
# docker network inspect <network_name>

# Networks can be configured with static IP addresses by setting the ipv4_address and/or ipv6_address for each attached network.
# todo, leverage for aws...probably never if deploy starts at github.

# docker network create --subnet
# why .... maybe...lol...this stablilizes and 2 forked projects off of this stabilize and are managed in one of these.

# brute force port scan on all containers in network

# For available scopes and descriptions see https://docs.pytest.org/en/6.2.x/fixture.html#fixture-scopes

# docker_ip
# Determine the IP address for TCP connections to Docker containers.

# docker_compose_file
# Get an absolute path to the docker-compose.yml file. Override this fixture in your tests if you need a custom location.

# docker_compose_project_name
# Generate a project name using the current process PID. Override this fixture in your tests if you need a particular project name.

# docker_services
# Start all services from the docker compose file (docker-compose up). After test are finished, shutdown all services (docker-compose down).

# docker_compose_command
# Docker Compose command to use to execute Dockers. Default is to use Docker Compose V2 (command is docker compose). If you want to use Docker Compose V1, change this fixture to return docker-compose.

# docker_setup
# Get the list of docker_compose commands to be executed for test spawn actions. Override this fixture in your tests if you need to change spawn actions. Returning anything that would evaluate to False will skip this command.

# docker_cleanup
# Get the list of docker_compose commands to be executed for test clean-up actions. Override this fixture in your tests if you need to change clean-up actions. Returning anything that would evaluate to False will skip this command.

# finally kick off "normal, non reflexive testing" in pytest, across golden-internal-network/ and/or golden-external-network/