import os

name = os.getenv('ZAB')
print(f"Hello, ZAB env variable defined in ../../../docker-compose.yml: {name}!")

print("hello from pytest service land...nothing doing here for a minute...")
