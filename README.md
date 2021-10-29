
# Yobber job-planning application

Simple app to manage non-recurring jobs.

## Authors

Miikka Hakulinen | made as a demo for Code Bootcamp 2021
- [@walumo](https://www.github.com/walumo)


## Deployment

Prepared for deployment to Heroku, remember to update config vars on the Heroku Settings page.

## Installation


```bash
git clone https://github.com/walumo/demo.git
cd demo
pipenv install
```

You need to make .env file and include you environment variables there, see the section below for more information.

You can run the app directly from VSCode or from the shell using:

```bash
pipenv shell
flask run
```

With your browser, enter: localhost:5000


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY` = 'your Google Maps API key'

`DATABASE_URL` = 'your database url'


## License

[MIT](https://choosealicense.com/licenses/mit/)

