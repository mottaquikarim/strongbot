[![Build Status](https://travis-ci.org/mottaquikarim/strongbot.svg?branch=fix-travis)](https://travis-ci.org/mottaquikarim/strongbot) [![Coverage Status](https://coveralls.io/repos/github/mottaquikarim/strongbot/badge.svg?branch=master&cachebust=1)](https://coveralls.io/github/mottaquikarim/strongbot?master)

# 💪 💪 StrongBot 👊 👊

*Chatbot exercise companion*

Serverless bot that acts as a workout companion. Meant to be a lightweight, platform agnostic alternative to workout apps. Performs two primary functions:

1. Keeps track of workout schedule (ie: rest days vs. exercise days, etc)
2. Keeps track of progress (ie: automagically remembers PRs and tracks performance stats)

Designed specifically to make management of workout routine simpler - just update Airtable spreadsheet with regiment, which the bot uses as source of truth.

Currently under active development.

## Getting Started

Bot implementation is deployed to AWS Lambda via the Serverless Framework. User data is stored in DynamoDb and workout info is stored in Airtable. Twilio is leveraged for actual SMS communication. 

NPM/NPM scripts is used as task runner and devel environment. The actual app is written in python but building/testing/etc can be achieved entirely with npm scripts.

## Set up
Before beginning, key services must be configured.

### Configure Serverless Framework/AWS account
**TODO**.

### Configure DynamoDb on AWS
**TODO**.

### Configure Twilio
**TODO**.


## Scripts
Here are a list of the available scripts for use re: deployment, testing, development.

```
Lifecycle scripts included in strongbot:
  test
    python -m pytest --cov=. --cov-report html --cov-report term

available via `npm run-script`:
  _dev
    python dev_app.py &
  _kill_python
    ps -ef | grep python | grep -v grep | awk '{print $2}' | xargs kill
  _kill_localtunnel
    ps -ef | grep lt | grep -v grep | awk '{print $2}' | xargs kill
  _localtunnel
    $(npm bin)/lt --port 5000 &
  deploy
    $(npm bin)/serverless deploy
  local-dev
    npm run _dev && sleep 5 && npm run _localtunnel
  local-kill
    npm run _kill_python && npm run _kill_localtunnel
  write-coveralls
    rm -f .coveralls.yml && echo "repo_token: $COVERAGE_TOKEN" >> .coveralls.yml
```

## Common Usecases

Here are some common coding usecases that will leverage npm scripts.

### Initial Set up
To get started with coding,
```
cd [into_project]
virtualenv -p python3 .venv
pip install -r requirements.txt
pip install -r requirements-test.txt
pip install -r requirements-dev.txt
```
The reason `requirements` files are broken up is to minimize size of serverless artifact. In truth the test depenedencies and dev dependencies are not needed to lambda function, so we don't want to bundle during deploy step.

### Develop locally

This only has to be done once at the start of devel.

**START**
```
npm run local-dev
```
Take the localtunnel URL printed in console and update your appropriate number in **[twilio](https://www.twilio.com/console/phone-numbers/incoming)**.

**CLEAN UP**

Once local devel is completed or you are ready to push, run:

```
npm run local-kill
```

### Run Tests
Before pushing, it is a good idea to run tests.

```
npm run test
```

### Deploy
To deploy to AWS lambda,
```
npm run deploy
```
