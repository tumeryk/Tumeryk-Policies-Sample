
import os
import pathlib
current = pathlib.Path(__file__).parent.resolve()
credential_path = f"{current}/google-creds.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
      