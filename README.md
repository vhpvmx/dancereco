# dancereco

You are not sure about your outfit for Saturday night, let's check your style!
Upload a picture to the app, it will recognize the dance style you are dressed for.

Categories: [Salsa, Lindy Hop, Hip Hop]

I developed a deep learning model to identify the kind of dance based on an image. I used around 450 images from Bing Search Api. It is possible to get good results with few images applying techniques like Data Augmentation and Transfer Learning.

I used the model resnet18 which was pre-trained on ImageNet (ImageNet contains over 1.3 million images of various sizes around 500 pixels across, in 1,000 categories)

As a result the new model can identify different dance styles in the same picture.

The deployment was done using Flask, Docker and Heroku.

Instructions for deployment:

1. Clone this repo
2. Build the docker image: sudo docker build -t dancereco:latest .
3. Execute the app inside the docker container: docker run --detach --publish 5000:5000 dancereco
4. Verify it works, go to the url: localhost:5000
Upload to Heroku:
5. Register in Heroku
6. In your terminal heroku login
7. heroku create nombre_app
8. heroku container:push web
9. heroku container:release web
10. heroku open
