# InterWorx API Library

This library is designed to make it much easier to interact with the
Interworx XMLRPC API outlined here:
[http://docs.interworx.com/interworx/api/index.php](http://docs.interworx.com/interworx/api/index.php)

This is still very much in alpha. As of now, the only completed controllers
are:
* /nodeworx/users
* /nodeworx/apikey
* /nodeworx/backup
* /siteworx/backup
* /siteworx/users calls.

I am currently working on these controllers:
* /nodeworx/firewall
* /nodeworx/ftp

As of now, _**none**_ of the clustering options are implemented. I simply
don't have a way to test against a cluster with my current setup.

## Usage:

The general principle is to follow the InterWorx documentation as closely as possible while making the library operate in a more pythonic manner. For instance, actions are defined in the API using camelCase, but since snake case is more "pythonic" all the calls have been rewritten in snake case. i.e. `listUsers` becomes `list_users`.

    # Connect to server:
    URL = 'myserver.domain.com'
    KEY = '<api key from NodeWorx>'
    server = Server(URL, KEY)

    # Get all NodeWorx users:
    server.nodeworx.users.list_users()

    # Get all SiteWorx users for domain.com:
    server.siteworx.users.list_users('domain.com')

    # Create a NodeWorx user:
    server.nodeworx.users.add(
        nickname='newuser', 
        email='existingemail@user.com',
        password='supersecurepassword11!',
        confirm_password='supersecurepassword11!')

    # Create a SiteWorx user:
    server.siteworx.users.add(
        'domain.com',
        nickname='newuser',
        email='existingemail@user.com',
        password='supersecurepassword!!1',
        confirm_password='supersecurepassword!!1')

### Errors:

This library does very little input checking and instead relies on the API response to tell the user when things are incorrectly formed. When the server returns a non-`0` response, the output will simply show whatever message the server returned.