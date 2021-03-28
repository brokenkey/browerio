Title: Using Pelican to Create a Personal Blog or Static Content Management System
Date: Sun 28 Mar 2021 02:27:43 PM CDT
Category: Tutorials
Tags: pelican, python, gcs, github
Status: draft

Everyone needs their own personal space on the Web. Blogs and home pages are the perfect place to publish your content for the world to see. Or perhaps you have a business or organization that needs an easy way to manage content.

Whether you just want to share action shots of your pet tortoise, your poetry about your favorite coffee mug, or videos of your vacation, a blog lets you organize and share content that is important to you and your audience.

But is it too much effort to learn a new piece of software and how to deploy it when social media websites like Medium or webhosts like squarespace can do all the hard work for you? Perhaps, but they can also take away the control you have as an artist, and reduce your options down to a set of binary-choice control panel toggles. Don't like the font choice or background color? Tough luck. Don't want pop-up ads and sign-up begging all over your important work? Too bad.

Hosting your own content does take some time and effort to set up, but by using a modern static site generator and cloud hosting, anyone can create a low-cost, professional looking blog without becoming a full-stack web developer at Twitter.

### Pelican 

Pelican is a static site generator written in Python. It's designed to get your content up and running quickly with minimal tweaking of the settings until you're ready for that.

Your articles and pages can be written in a convenient format like Markdown and automatically get converted to beautiful, clean HTML pages, ready for upload to any webhost you prefer. In this article, I'll explain how to upload your site to Google Cloud Storage, but services like Linode or Digital Ocean can also provide inexpensive hosting for your awesome new homepage.

### Getting Started

To install Pelican from pip, you would type the following into your terminal:

```
:::Bash
pip3 install pelican[markdown]
```
You should now create a directory for your project and `cd` into it.
```
:::Bash
mkdir my-homepage
cd my-homepage
```
Now we can create our project very quickly by using the `pelican-quickstart` command.

```
:::Bash
pelican-quickstart
Welcome to pelican-quickstart v4.6.0.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.

    
    > Where do you want to create your new web site? [.] 
    > What will be the title of this web site? my-homepage
    > Who will be the author of this web site? me
    > What will be the default language of this web site? [en] en
    > Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) n
    > Do you want to enable article pagination? (Y/n) y
    > How many articles per page do you want? [10] 
    > What is your time zone? [Europe/Paris] Etc/UTC
    > Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) Y
    > Do you want to upload your website using FTP? (y/N) N
    > Do you want to upload your website using SSH? (y/N) N
    > Do you want to upload your website using Dropbox? (y/N) N
    > Do you want to upload your website using S3? (y/N) N
    > Do you want to upload your website using Rackspace Cloud Files? (y/N) N
    > Do you want to upload your website using GitHub Pages? (y/N) N
    Done. Your new project is available at /home/cameron/my-homepage

```
You will be asked some basic questions about your site, fill those in or accept the defaults.

And... We're done! Congratulations on creating your own blog with Pelican. Sure, we still need to put it somewhere and write all those pesky blog posts and pages, but other than that, we're done. 😉

Your project should now look something like this:

```
:::Bash
total 24K
drwxrwxr-x 2 cameron cameron 4.0K Mar 28 14:37 content
-rw-rw-r-- 1 cameron cameron 2.5K Mar 28 14:37 Makefile
drwxrwxr-x 2 cameron cameron 4.0K Mar 28 14:37 output
-rw-rw-r-- 1 cameron cameron  825 Mar 28 14:37 pelicanconf.py
-rw-rw-r-- 1 cameron cameron  549 Mar 28 14:37 publishconf.py
-rw-rw-r-- 1 cameron cameron 3.5K Mar 28 14:37 tasks.py
```

### Creating a Post

Now we're ready to create our first blog post. I assume you're familiar with markdown format, but if not, you can learn a bit about it here: (Markdown Cheatsheet)[http://mdcheatsheet.com/]

Open your favorite text editor and create a file in the content directory, my-first-post.md:

```
:::Markdown
Title: My first blog post
Date: Sun 28 Mar 2021 03:23:41 PM CDT
Category: Blog

This is my first blog post.
This is a [link](https://brower.io/)
```


