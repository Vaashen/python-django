># Django-Project

In this repo, you will find a folder called "myclub_website", this is my website that i recently created using django. It is a simple booking website, you can create a event and book a venue on the website.

<br><br>

>## Tools you will need

<p>There are a 2 things you will need to run the website:</p>

- Docker Desktop
- An editor (eg. VSC)

You can download Docker Desktop [here](https://www.docker.com/products/docker-desktop/)

You can download Visual Studio Code [here](https://code.visualstudio.com/download)

Once the downloads have been completed, open them one at a time and follow the instructions that follow to setting them up.

<br><br>

>## How to run the website

<p>Download the myclub_website folder from the repo.
Open VSC and in the top left hand corner, you will see a tab called "File", in it will be a "open folder", tap on it and find the myclub_website folder, select it and tap on 'open', it should now be in VSC.</p>

<p> Next open Docker Desktop, you should see that images adn containers are empyt, lets create the image first.<p>

<p>Back in VSC, on the top of the screen, click on the tab called "Terminal" and then "new terminal"<p>

Now to create the image, type in the cammand:<br>
`docker build -t python-django .`<br>
Make sure to include the dot at the end. It should take a few seconds to install everything. Once this is done, if you open the docker desktop, you will see under images that there is an image called 'python-django'.

Next is to run the image, in VSC, in the terminal, type in the command:<br>
`docker run --publish 8000:8000 python-django`<br>
if all goes well, the server should start up, and if you go back to docker desktop, in containers, the status should be 'running'. If this is the case, visit [localhost](http://127.0.0.1:8000/) and the website should be up.