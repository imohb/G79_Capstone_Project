# Project Karty

#### A web implementation of [ChatterBot](https://github.com/gunthercox/ChatterBot) using Flask.

## Local Setup:
 1. Ensure that Python, Flask, SQLAlchemy, and ChatterBot are installed (either manually, or run `pip install -r requirements.txt`).
 2. Run *app.py* with `python app.py`.
 3. The demo will be live at [http://localhost:5000/](http://localhost:5000/)

## How do I deploy this to a web server?
If you do not have a dedicated server, I highly recommend using  [AWS](https://aws.amazon.com/getting-started/projects/deploy-python-application/)  to host your application.

### Deploying on AWS

`bot = ChatBot("Karty", storage_adapter="chatterbot.storage.SQLStorageAdapter")`

## License
This source is free to use, but ChatterBot does have a license which still applies and can be found on the [LICENSE](https://github.com/gunthercox/ChatterBot/blob/master/LICENSE) page.
