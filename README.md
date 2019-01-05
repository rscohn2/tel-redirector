# tel-redirector
Redirects to a tel URL

Deploy as a google cloud function

If your cloud function URL is

https://my-gcp-projet.cloudfunctions.net/TelephoneRedirect?tel=555-555-1234

It will redirect to tel:555-555-1234

This is useful for google sheets, which allows http URLs, but does not allow tel:
