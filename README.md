# Cozy Corner

Cozy Corner is locally owned mom & pop flower boutique shop located in Ashburn VA.

It specializes in wedding arrangements and is experiencing a recent growth in traffic. So I decided to create a basic webpage for the business to help keep the flow.

# Tech Stack

- PostgreSQL for backend
- Created with Django, a python framework
- Deployed to Heroku at : https://calm-gorge-13996.herokuapp.com/

I decided to use PostgreSQL and Django because I wanted to learn more about the this techstack. We've had great exposure to JavaScript and JS frameworks, but I wanted to diversify my knowledge and dig a little deeper into this stack.

## Local Environment

Please Git clone the repo:

```bash
$ pip3 install virtualenv
$ virtualenv .env -p python3
$ source .env/bin/activate
```

Once the envrionment is activated:

```bash
cd cozycorner
pip install -r requirements.txt
code .
```

\*\* Please note code . is the command to open VisualCode, if you have another text editor you prefer, please go ahead and use the preferred text editor.

To start local envrionment:

```bash
$ python manage.py runserver
```

and enjoy the magic at localhost:8000

# Goals

### Primary Goal

Through out the course, I was never able to successfully incorporate user authentication and authorization.

For this project, I would like to get use authentication and authorization up and running.

### Secondary Goal

Once authorized, I would like the User to be able to either:

1. Click the existing bouquet to add to his/her user page
2. Create his/her own custom bouquet and add to his/her user page
3. Send us an email with the form information
