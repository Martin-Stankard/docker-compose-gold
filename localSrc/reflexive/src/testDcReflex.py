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
