# Snake

[![Docker Image CI](https://github.com/aramirol/snake/actions/workflows/docker-image.yml/badge.svg)](https://github.com/aramirol/snake/actions/workflows/docker-image.yml)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=aramirol_snake&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=aramirol_snake)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=aramirol_snake&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=aramirol_snake)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=aramirol_snake&metric=bugs)](https://sonarcloud.io/summary/new_code?id=aramirol_snake)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=aramirol_snake&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=aramirol_snake)

***Snake*** is a classic arcade game where the player controls a snake that moves around the screen. The objective of the game is to eat food items that appear randomly while avoiding collisions with the snake's own body or the game boundaries.

As the snake eats food, it grows in length, making it more challenging to navigate without running into itself. The game ends if the snake collides with its own body or hits the boundaries of the game window.

The player controls the snake's movement using arrow keys or other designated keys. The snake can move in four directions: up, down, left, and right. The goal is to eat as much food as possible and achieve the highest score.

This game was develeped using **[ChatGPT](https://openai.com/chatgpt)**.

<img src="https://aramirol.github.io/custom-resources/images/snake.png" width="49%" />

## How to

Use the `Dockerfile` to quickly deploy the game. The image used is python:3.9, exposing the port 8000.

```sh
$ sudo docker run -d -p 8000:8000 aramirol/snake:latest
```

If you prefer, you can use the `deployment.yaml` file to deploy the game to Kubernetes. This file creates all the necessary components (remember to change the values to fit your environment)

```sh
$ kubectl apply -f deployment.yaml
```

```yml
spec:
      containers:
        - name: tictactoe
          image: aramirol/snake:latest
          ports:
            - containerPort: 8000
```

## License

[![GitHub](https://img.shields.io/github/license/aramirol/snake)](https://github.com/aramirol/snake/blob/main/LICENSE)

See [LICENSE](https://github.com/aramirol/snake/blob/main/LICENSE) to see the full text.
