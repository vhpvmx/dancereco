# dancereco

You are not sure about your outfit for Saturday night, let's check your style!
Upload a picture to the app, it will recognize the dance style you are dressed for.

Categories: [Salsa, Lindy Hop, Hip Hop]

I developed a deep learning model to identify the kind of dance based on an image. I used around 450 images from Bing Search Api. It is possible to get good results with few images applying techniques like Data Augmentation and Transfer Learning.

I used the model resnet18 which was pre-trained on ImageNet (ImageNet contains over 1.3 million images of various sizes around 500 pixels across, in 1,000 categories)

As a result the new model can identify different dance styles in the same picture.

Prepare the environment:
Git, follow this instructions to install git: https://docs.docker.com/engine/install/ubuntu/
Docker, you can install docker following these instructions: https://docs.docker.com/engine/install/ubuntu/
Heroku CLI, here you have the instructions to install heroku cli: https://devcenter.heroku.com/articles/heroku-cli


The deployment was done using Flask, Docker and Heroku.

Instructions for deployment:

1. Clone this repo
2. Build the docker image: $sudo docker build -t dancereco:latest .
3. To verify it works correctly before we deploy on heroku we execute the app locally using the docker container: $docker run --detach --publish 5000:5000 dancereco
4. Open a web browser and go to the url localhost:5000
5. Once you register at heroku.com and it is installed in your machine, type in your terminal: $heroku login
6. Create the app in heroku with this command: $heroku create nombre_app
8. Upload the container: $heroku container:push web
9. Release the container: $heroku container:release web
10. Open the app in your browser:  $heroku open

*I use $ as a prompt indicator


References:
https://runnable.com/docker/python/dockerize-your-flask-application
