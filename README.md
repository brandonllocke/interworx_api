# InterWorx API Wrapper

This API Wrapper is designed to make it much easier to interact with the
Interworx XMLRPC API outlined here:
[http://docs.interworx.com/interworx/api/index.php](http://docs.interworx.com/interworx/api/index.php)

As of now, _none_ of the clustering options are tested. I simply
don't have a way to test against a cluster with my current setup.

## Usage:

Follow the InterWorx API documentation as closely as possible. This wrapper
does no error checking before sending commands to the InterWorx server.

A basic usage is found below:

    Iworx_Object.request(controller, action, params)

`controller` is equal to the controllers defined in the API documentation.
Examples include: `/nodeworx/cron`, `/nodeworx/dns`, and may occasionally be
nested further like `/nodeworx/dns/record`.

`action` is equal to one of the actions defined on that specific controller's
page. Examples for `/nodeworx/overview` include: `editProfile`,
`listHostname`, `listIsClusterable`, `listLicenseKey`, `listLoadAverage`,
`listServiceStatus`, etc.

`params` are input parameters defined below the action on the specific
controller's documentation page. To continue using `/nodeworx/overview` as an
example, using the `editProfile` action can take some additional parameters,
such as: `theme`, `language`, `menu_style`, `password`, and
`confirm_password`. Some actions take no input parameters, so none need to be
defined. Be sure to check the note on `siteworx_domain` below for a special
case.

As a real world example, let's be a bit verbose while we edit the theme our
account uses to 'blue_steel'.

    controller = '/nodeworx/overview'
    action = 'editProfile'
    Iworx_Object.request(controller, action, theme='blue_steel')

### `siteworx_domain`

While using any of the controllers beginning with `/siteworx`, you must
define an additional parameter called `siteworx_domain`. This should be set
to the domain of the account you wish to interact with. This lets the API
know which account to complete the action on.

## Basic Examples:

    # Connect to server:
    URL = 'myserver.domain.com'
    KEY = '<api key from NodeWorx>'
    iworx = Iworx(URL, KEY)

    # Get all NodeWorx users:
    iworx.request('/nodeworx/users', 'listUsers')

    # Get all SiteWorx users for domain.com:
    iworx.request('/siteworx/users', 'listUsers', siteworx_domain='domain.com')

    # Create a NodeWorx user:
    iworx.request('/nodeworx/users',
        'add',
        nickname='newuser', 
        email='existingemail@user.com',
        password='supersecurepassword11!',
        confirm_password='supersecurepassword11!')

    # Create a SiteWorx user:
    iworx.request('/siteworx/users', 
        'add',
        siteworx_domain='domain.com',
        nickname='newuser',
        email='existingemail@user.com',
        password='supersecurepassword!!1',
        confirm_password='supersecurepassword!!1')

## Advanced Examples:

    # Delete all Siteworx accounts:
    for account in iworx.request('/nodeworx/siteworx', 'listAccounts'):
        iworx.request('/nodeworx/siteworx', 'delete', domain=account['domain'])

    # Delete all secondary Siteworx users (but not the master user):
    for account in iworx.request('/nodeworx/siteworx', 'listAccounts'):
        for deluser in iworx.request('/siteworx/users', 'listDeletable', siteworx_domain=account['domain']):
            iworx.request('/siteworx/users', 'delete', siteworx_domain=account['domain'], user=deluser[0])

## Errors:

This library relies on the API response to tell the user when things are
incorrectly formed. When the server returns a non-`0` response, the output
will simply show the server message the server returned. For example:

    Server responded with an exit code of: 11.
    The server's response was: There was a problem validating the form. Please see details below.
    options: This input is required
    Usage: 
    type
    location
    email_address 
    options web|mail|dbs
    exclude_extensions (One per Line).