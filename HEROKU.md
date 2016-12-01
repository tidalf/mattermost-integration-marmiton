## How to
To install this project using Heroku, you will need: 

1. A Heroku account, available for free from [Heroku.com](http://heroku.com)
1. A Heroku CLI, available for free from [Heroku.com](https://devcenter.heroku.com/articles/heroku-cli)
2. A GitHub account, available for free from [GitHub.com](http://github.com)

Here's how to start:

1. **Create a copy of this project to manipulate**
  1. Log in to your GitHub account. Go to the [Github repository of this project](https://github.com/numberly/mattermost-integration-giphy/) click **Fork** in the top-right corner to create a copy of this project that you can control and manipulate

2. **Deploy your project copy to Heroku**
```bash
    $ heroku login

    $ heroku create

    $ git push heroku master
```

3. **Connect your project to your Mattermost account for slash commands**
 1. Log in to your Mattermost account. Click the three dot menu at the top of the left-hand side and go to **Integrations** > **Slash Commands**
 2. Under *Add a new command*, enter `gif` into **Command Trigger Word**
 3. Paste your Heroku domain into *Callback URLs* to the beginning and `/new_post` to the end so it looks similar to `http://<your-heroku-domain>/new_post`
 4. Select `POST` method
 5. (optional) Choose a username and icon url (more details [here](https://docs.mattermost.com/developer/slash-commands.html#set-up-a-custom-command))
 6. (optional) Check the autocomplete checkbox, add `[KEYWORD]` as the hint, `Returns a GIF from Giphy based on the keyword` as the description and `Get a GIF from Giphy` as the descriptive label
 7. Copy the *Token* from your newly created slash command that appears under the *Existing commands* section

4. **Configure your heroku app with the new token**
```bash
   $ heroku config:set MATTERMOST_GIPHY_TOKEN=xxxxx
```

That's it! Waiting a few minutes for the Heroku process to restart you should be able to type `gif: hello` or `/gif hello` into any channel and see a GIF from Giphy's translate service.


## Production setup:
If you'd like to use this integration in a production envrionment, it is strongly recommended that you get a production Giphy API key from [here](http://api.giphy.com/submit). Once you have that you can configure the integration to use it:

1. Go to your [Heroku Dashboard](https://dashboard.heroku.com/apps) and click on your app
2. Click the **Settings** tab. Under the *Config Variables* section, click **Reveal Config Vars**
3. For *KEY* type in `GIPHY_API_KEY` and for *VALUE* paste in your Giphy API key, then click **Add**
4. Wait a minute for the Heroku process to restart
