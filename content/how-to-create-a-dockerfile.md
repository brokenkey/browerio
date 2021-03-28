Title: How to write a Dockerfile
Date: Sat 27 Mar 2021 09:27:19 AM CDT
Category: Tutorials
Tags: docker, programming
Status: draft

# What is a Dockerfile?

A Dockerfile is a text file containing all the instructions necessary to set up a containerized server for running some kind of software.

### Why do you need a Dockerfile?

Are you trying to run a webserver or some other type of server software? Then it's a good idea to standardize how you will install and configure your software in a Dockerfile so that you can easily deploy a container image the same way every time.

### Getting started

You want to start by picking an image to base yours off of. I like Ubuntu because that's what I use. A lot of people prefer to minimize the size of their containers by using distributions like Alpine. Pick whatever you like or what your software works best on.

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

From there, we can `COPY` our nice python program into the image:

```
:::Dockerfile
COPY my-program.py /opt/my-program/.
```

To define the main program to launch when we run our container, we use the `CMD` instruction.

```
:::Dockerfile
CMD python3 /opt/my-program/my-program.py
```


