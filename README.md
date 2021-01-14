# dancereco

You are not sure about your outfit for Saturday night, let's check your style!

Upload a picture to the app, it will recognize the dance style you are dressed for.

Categories: [Salsa, Lindy Hop, Hip Hop]

I developed a deep learning model to identify the kind of dance based on an image. I used around 450 images from Bing Search Api. It is possible to get good results with few images applying techniques like Data Augmentation and Transfer Learning.

I used the model resnet18 which was pre-trained on ImageNet (ImageNet contains over 1.3 million images of various sizes around 500 pixels across, in 1,000 categories)

As a result the new model can identify different dance styles in the same picture.

I use python, fastai, flask, javascript, docker and heroku to develop and deploy the app.

You can check how the app looks once deployed on heroku in this URL: https://dancereco.herokuapp.com/

To install and deploy it follow these instructions.

Prepare the environment:
- Git, follow this instructions to install git: https://docs.docker.com/engine/install/ubuntu/
- Docker, you can install docker following these instructions: https://docs.docker.com/engine/install/ubuntu/
- Heroku CLI, here you have the instructions to install heroku cli: https://devcenter.heroku.com/articles/heroku-cli


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

* I use $ as a terminal prompt indicator

I found errors while creating the docker image, you can find out the problem opening an interactive session:

$sudo docker run -it --entrypoint sh dancereco

Then you have a shell, you can list your files, check the content of them or execute the app with this command:

$python app.py

Here you can check the development of the DL model: https://github.com/vhpvmx/danceClassifier

Enjoy!

References:
> https://runnable.com/docker/python/dockerize-your-flask-application
> https://devcenter.heroku.com/articles/container-registry-and-runtime
