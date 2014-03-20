from buildbot.status.base import StatusReceiverMultiService
from buildbot.status.builder import Results, SUCCESS
import os, urllib


class SlackStatusPush(StatusReceiverMultiService):

  def __init__(self, subdomain, api_token, channel_name, localhost_replace=False, builder_name=False, **kwargs):
      StatusReceiverMultiService.__init__(self)

      self.subdomain = subdomain
      self.api_token = api_token
      self.channel_name = channel_name
      self.localhost_replace = localhost_replace
      self.builder_name = builder_name

  def setServiceParent(self, parent):
    StatusReceiverMultiService.setServiceParent(self, parent)
    self.master_status = self.parent
    self.master_status.subscribe(self)
    self.master = self.master_status.master

  def disownServiceParent(self):
    self.master_status.unsubscribe(self)
    self.master_status = None
    for w in self.watched:
      w.unsubscribe(self)
    return StatusReceiverMultiService.disownServiceParent(self)

  def builderAdded(self, name, builder):
    return self  # subscribe to this builder

  def buildFinished(self, builder_name, build, result):
    url = self.master_status.getURLForThing(build)
    if self.localhost_replace:
      url = url.replace("//localhost", "//%s" % self.localhost_replace)
    if self.builder_name:
      builder_name = self.builder_name

    if result == SUCCESS:
      icon = ":buildbot_success:"
    else:
      icon = ":buildbot_failure:"
    message = ("%s %s on <%s|%s>" % (icon, Results[result].upper(), url, builder_name))


    data = ('payload={"channel": "%s", "text": "%s"}' % (self.channel_name, message))
    # Yes, we are in Twisted and shouldn't do os.system :)
    os.system("curl -X POST -d '%s' https://%s.slack.com/services/hooks/incoming-webhook?token=%s" % (data, self.subdomain, self.api_token))
