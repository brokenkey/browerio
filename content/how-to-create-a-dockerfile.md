Title: How to write a Dockerfile
Date: Sat 27 Mar 2021 09:27:19 AM CDT
Category: Tutorials
Tags: docker, programming
Status: published

# What is a Dockerfile?

A Dockerfile is a text file containing all the instructions necessary to set up a containerized server for running some kind of software.

### Why do you need a Dockerfile?

Are you trying to run a webserver or some other type of server software? Then it's a good idea to standardize how you will install and configure your software in a Dockerfile so that you can easily deploy a container image the same way every time.

### Getting started

You want to start by picking an image to base yours off of. I like Ubuntu because that's what I've used for a very long time and their apt repos contain a wide variety of stable software. A lot of people prefer to minimize the size of their containers by using distributions like Alpine. Pick whatever works for you.

You can generally pick any image accorting to your needs, and many are available on repos like [dockerhub](https://hub.docker.com/search?q=&type=image). 

The `FROM` instruction in a Dockerfile tells Docker what to base your image off of. 

```
:::Dockerfile
FROM ubuntu:20.04
```

After this command has executed, we now have a container image that is running a fresh install of Ubuntu 20.04.

We'll often need to install dependencies or update our container when we build it. For this we can use the `RUN` instruction:

```
:::Dockerfile
RUN apt-get update \
    && apt-get upgrade -y \
    && apt install python3-pip \
    && pip3 install requests
```

`RUN` will run the given program when we build our Dockerfile. This is great for installer scripts or configuring our image prior to runtime. 

So far we've installed python3-pip and used it to download the [requests](https://2.python-requests.org/en/master/) module.

We'll use this to make our python program:

```
:::python
import requests

response = requests.get('https://cat-fact.herokuapp.com/facts/random')

print(response.json()['text'])
```

From there, we can `COPY` our nice python program into the image:

```
:::Dockerfile
COPY my-program.py my-program.py
```

To define the main program to launch when we run our container, we use the `CMD` instruction.

```
:::Dockerfile
CMD python3 my-program.py
```

That's it, we have our first Dockerfile!

```
:::Dockerfile
FROM ubuntu:20.04

RUN apt-get update \
    && apt-get upgrade -y \
    && apt install -y python3-pip \
    && pip3 install requests

COPY my-program.py my-program.py

CMD python3 my-program.py
```

Now we build and tag our docker image:
```
:::bash
docker build -t my-first-docker-image .
```

Now we have an image of a Linux computer all set up and ready to run our program. We can upload this to a different server for deployment, share it with others, or use this image to build a child image.

We can run the image with `docker start`.

```
:::bash
docker start my-first-docker-image:latest

An estimated 50% of today's cat owners never take their cats to a veterinarian for health care. Too, because cats tend to keep their problems to themselves, many owners think their cat is perfectly healthy when actually they may be suffering from a life-threatening disease. Therefore, cats, on an average, are much sicker than dogs by the time they are brought to your veterinarian for treatment.
```

There we go. We've learned the basics of writing a Dockerfile and we've learned something about cats.

Here are some more resources to learn more about Dockerfiles and Docker:

* [Install Docker](https://docs.docker.com/get-docker/)
* [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)
* [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

You can download the files from this tutorial on [GitHub](https://github.com/brokenkey/my-first-dockerfile).
