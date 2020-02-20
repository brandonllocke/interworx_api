# InterWorx API Library

This library is designed to make it much easier to interact with the Interworx XMLRPC API outlined here: [http://docs.interworx.com/interworx/api/index.php](http://docs.interworx.com/interworx/api/index.php)

This is still very much in alpha. As of now, the only completed component is the /nodeworx/users and /siteworx/users calls.

## Usage:

    # Connect to server:
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
