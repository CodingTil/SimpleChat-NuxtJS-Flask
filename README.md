# SimpleChat

**SimpleChat** is a very simple full stack chat application.

It is created using [Nuxt.js](https://nuxtjs.org) for the frontend and [Flask](https://flask.palletsprojects.com/en/1.1.x/) for the backend.
On the frontend I am using the [Vuetify Material Design Framework](https://vuetifyjs.com/en/) to easily create a visually appealing application. The backend uses [sqlite](https://docs.python.org/3/library/sqlite3.html) to store the messages in a file.

I created this application as an exercise to get into the world of web-development. Therefore, **I did not concern myself with security standards and risks. &rarr; DO NOT USE THIS APPLICATION IN A REAL ENVIRONMENT!**

## TODO:
 - Efficient Fetch of messages. Currently, each few seconds *all* messages are fetched from the server, not just the latest.
 - Common startup script for production and dev, and common configuration file