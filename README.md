Slack.io status plugin for Buildbot
===================================

This Buildbot plugin sends messages to a Slack.io channel when each build finishes with a handy link to the build results.

This plugin is based on the buildbot-status-hipchat plugin created by the dev team at http://www.pricingassistant.com/ ; Contributions are welcome!

Install
=======

Create a new Incomming Webhook in your slack account.

Copy slack.py next to your master.cfg file

Then in your master.cfg, add the following:

```
import slack
c['status'].append(slack.SlackStatusPush("YOUR_SLACK_SUBDOMAIN", "YOUR_SLACK_TOKEN", "SLACK_CHANNEL_NAME"))
```

If you Buildbot web frontend doesn't know its public address it will use "localhost" in its links. You can change this:

```
import slack
c['status'].append(slack.SlackStatusPush("YOUR_SLACK_SUBDOMAIN", "YOUR_SLACK_TOKEN", "SLACK_CHANNEL_NAME", "buildbot.mycompany.com"))
```

If you want to specify a builder name you can add it to the master.cfg like this:

```
import slack
c['status'].append(slack.SlackStatusPush("YOUR_SLACK_SUBDOMAIN", "YOUR_SLACK_TOKEN", "SLACK_CHANNEL_NAME", "buildbot.mycompany.com", "builder name"))
```

You need to define two new emoticons in your Slack Account:

```
:buildbot_success:
:buildbot_failure:
```

and add some fancy icons or gifs ;)

## Example

For a Slack Team named ```Empire``` i would have the subdomain ```empire``` and a Project named ```Death Star 2``` so my slack channel would be somthing like ```#death-star-2```.  
Of course my generated Slack Token would be somthing like ```KILLALLTHEREBELS``` ;)  
My Buildbot would run under ```ci.empire.com``` and the Builder would be called ```Vader```.

So with this Example Data my master.cfg would look like this:

```
import slack
c['status'].append(slack.SlackStatusPush("empire", "KILLALLTHEREBELS", "#death-star-2", "ci.empire.com", "Vader"))
```


Enjoy!
