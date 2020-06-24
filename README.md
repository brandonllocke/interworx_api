# InterWorx API Library

This library is designed to make it much easier to interact with the
Interworx XMLRPC API outlined here:
[http://docs.interworx.com/interworx/api/index.php](http://docs.interworx.com/interworx/api/index.php)

This is still very much in alpha. As of now, the only completed controllers
are:
* /nodeworx/apikey
* /nodeworx/backup
* /nodeworx/cron
* /nodeworx/firewall
* /nodeworx/ftp
* /nodeworx/help
* /nodeworx/http
* /nodeworx/index
* /nodeworx/ip
* /nodeworx/ip/sites
* /nodeworx/siteworx
* /nodeworx/users
* /siteworx/backup
* /siteworx/users
* /siteworx/ftp

As of now, _**none**_ of the clustering options are tested. I simply
don't have a way to test against a cluster with my current setup.

## Usage:

The general principle is to follow the InterWorx documentation as closely as
possible while making the library operate in a more pythonic manner. For
instance, actions are defined in the API using camelCase, but since snake
case is more "pythonic" all the calls have been rewritten in snake case. i.e.
`listUsers` becomes `list_users`.

Commands are formed as
`<instance>.<nodeworx/siteworx>.<controller>.<action>`.
For instance, if I wanted to use the FTP controller to add an account to siteworx account, the format would be `server.siteworx.ftp.add(params)`.

### Basic Examples:

    # Connect to server:
    URL = 'myserver.domain.com'
    KEY = '<api key from NodeWorx>'
    server = Server(URL, KEY)

    # Get all NodeWorx users:
    server.nodeworx.users.list_users()

    # Get all SiteWorx users for domain.com:
    server.siteworx.users.list_users(wd='domain.com')

    # Create a NodeWorx user:
    server.nodeworx.users.add(
        nickname='newuser', 
        email='existingemail@user.com',
        password='supersecurepassword11!',
        confirm_password='supersecurepassword11!')

    # Create a SiteWorx user:
    server.siteworx.users.add(
        wd='domain.com',
        nickname='newuser',
        email='existingemail@user.com',
        password='supersecurepassword!!1',
        confirm_password='supersecurepassword!!1')

### Advanced Examples:

    # Delete all Siteworx accounts:
    for account in server.nodeworx.siteworx.list_accounts():
        server.nodeworx.siteworx.delete(domain=account['domain'])

    # Delete all secondary Siteworx users (but not the master user):
    for account in server.nodeworx.siteworx.list_accounts():
        for deluser in server.siteworx.users.list_deletable(wd=account['domain']):
            server.siteworx.users.delete(wd=account['domain'], user=deluser)

### Errors:

This library does very little input checking and instead relies on the API
response to tell the user when things are incorrectly formed. When the server
returns a non-`0` response, the output will simply show whatever message the
server returned.