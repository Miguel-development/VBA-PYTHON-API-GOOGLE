from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from apiclient import errors
from apiclient.http import MediaFileUpload

import  tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()




def getCLIENT__SECRET_FILE_BASE(CLIENT_PATH):
    return CLIENT_PATH

def getTOKEN_FILE_BASE(TOKEN_PATH):
    return TOKEN_PATH

def getUploadFile():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    API_SERVICE_NAME = "drive"
    CLIENT_SECRET_FILE = r"\\credentials.json"
    # CLIENT_SECRET_FILE = getCLIENT__SECRET_FILE_BASE()
    CLIENT_SECRET_FILE = filedialog.askopenfilename()
    API_VERSION = "v3"
    SCOPES = ['https://www.googleapis.com/auth/drive']
    TOKEN_PATH = r"\\token.json"
    # TOKEN_PATH = getTOKEN_FILE_BASE()
    TOKEN_PATH = filedialog.askopenfilename()

    #WE HAVE CREDENTIALS TOKEN FILE, WHERE IT WILL STORE THE AUTHORIZATION SCOPES
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=creds)

        path_File = filedialog.askopenfilename()
        
        #Send file to Google Drive
        file_metadata = {'name': str(path_File.split("/")[-1])}
        media = MediaFileUpload(path_File,
                                mimetype='application/octet-stream')
        file = service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
        print ('File ID: %s' % file.get('id'))


        """
        # Call the Drive v3 API
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
        """
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')









