[Source](https://dev.to/acro5piano/specifying-user-and-group-in-docker-i2e)


```
Solution 1: Dockerfile

We can set owner and group in Dockerfile.
The official document says we can do it by USER postgres, but we can also set group with :.

# Dockerfile

USER 1000:1000

However, this way specifies owner and group id.
I found more flexisible solutions.
Solution 2: command argument

docker run -u 1000:1000 debian bash

In this way, we can set user and group with shell variables like $UID.
Or getent group staff | cut -d: -f3.
Solution 3: specify in docker-compose.yml

I was looking for this.

The principle is the same as solution 2, so the following config works well:

# docker-compose.yml

web:
  image: ruby:2.4
  user: "${UID}:${GID}"

Then run

UID=${UID} GID=${GID} docker-compose up

Or, export these variables as environment variables, ignoreing bash: UID: readonly variable

export UID=${UID}
export GID=${GID}
docker-compose up

Environment

    Arch Linux
    Docker 1.12.3 linux/amd64
```
