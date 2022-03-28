# gmail_api

## requirements

* [Python 3.9](https://www.python.org/downloads/)

## setup
To run the application several settings must be set. 
* create a Google Cloud Platform project
* enable Gmail API for the project
* create OAuth 2.0 Client ID credentials
* enable OAuth consent screen, add **gmail.readonly** and **gmail.send** scopes
* download credentials json-file and save them as 
  **src/settings/credentials.json**
* create ".env" file with SENDER and RECEIVER variables, or set them manually.
  Sender is email address you gave permission for application.
  Receiver is destination email address.


## launch application

To run the application use terminal or command prompt and scripts in directory.
For macOS and Linux users check the `_nix` one
and for Windows take a look at the `windows` one.

### linux or macOS
```commandline
sh ./scripts/_nix/start.sh
```
### windows
```commandline
./scripts/windows/start.cmd
  ```

## run application

When the application launched the first time, you will be provided with the 
authorization granting page. It will be opened automatically.
* give the application permission for the account you choose
* press continue
* choose both scopes (view emails and settings, and send emails)

This will create **src/settings/token.json**, which would be used later
when the application launched again.

