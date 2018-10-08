# Marmiton Integration Service for Mattermost
This integrations service is used to enable an external search engine ([Marmiton](https://en.wikipedia.org/wiki/Marmiton)) to be queried based on commands issued in a Mattermost channel using Mattermost [outgoing webhooks](https://github.com/mattermost/platform/blob/master/doc/integrations/webhooks/Outgoing-Webhooks.md). 

Once installed, users can type `/marmiton: keyword` to send a query to the Marmiton search engine and return with a post containing one non-deterministic search result from the Marmiton database of recipes matching `keyword`. The recipe will appear below in the posted message. 

Powered by [Marmiton](http://www.marmiton.org/).

## Requirements
To run this integration you need:

1. A **web server** supporting Python 3.5 or compatible versions.
2. A **[Mattermost account](http://www.mattermost.org/)** [where outgoing webhooks are enabled](https://github.com/mattermost/platform/blob/master/doc/integrations/webhooks/Outgoing-Webhooks.md#enabling-outgoing-webhooks)

Many web server options will work, below we provide instructions for [**Heroku**](HEROKU.md) and a general [**Linux/Ubuntu**](LINUX.md) server.

### Docker install
[**Here**](DOCKER.md)
