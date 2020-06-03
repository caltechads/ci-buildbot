# ci-buildbot

`ci-buildbot` is a command line tool to do slack messaging from CodePipelines.

To install:

```
pyenv virtualenv 3.6.5 ci-buildbot
pyenv local ci-buildbot
pip install -r requirements.txt
pip install -e .
```

Now set up the environment:

```
cp etc/environment.text .env
```

You'll need to know two things: `SLACK_API_TOKEN`.

Now you can run the main command, `buildbot`:

```
buildbot --help
```
