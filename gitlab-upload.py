#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import requests

from optparse import OptionParser


def upload_file(project_id, filename, gitlab_token):
    url = 'https://gitlab.com/api/v4/projects/{0}/uploads'.format(project_id)
    headers = {'PRIVATE-TOKEN': gitlab_token}
    files = {'file': open('{0}'.format(filename), 'rb')}
    r = requests.post(url, headers=headers, files=files)

    if r.status_code == 200 or r.status_code == 201:
        print('Uploading the file {0}....'.format(filename))
    else:
        print('File {0} was not uploaded'.format(filename))

    markdown = r.json()['markdown']
    return markdown


def create_new_issue(project_id, file, gitlab_token, title, markdown):
    url = 'https://gitlab.com/api/v4/projects/{0}/issues'.format(project_id)
    headers = {'PRIVATE-TOKEN': gitlab_token}
    params = {
        'title': title,
        'description': markdown
    }
    r = requests.post(url, headers=headers, params=params)

    if r.status_code == 200 or r.status_code == 201:
        print('Created a new Issue with file {}'.format(file))
    else:
        print('Did not created a new Issue')

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("--gitlab_token", dest="gitlab_token", help="Gitlab private token")
    parser.add_option("-f", "--file", dest="file", help="File to upload gitlab.com")
    parser.add_option("-p", "--project", dest="project_id", help="project id where will upload file")
    parser.add_option("-t", "--title", dest="title", help="Title for new issue")

    (options, args) = parser.parse_args()
    if not options.project_id or not options.gitlab_token:
        parser.print_help()
        sys.exit(0)

    status_message = upload_file(options.project_id, options.file, options.gitlab_token)
    print(create_new_issue(options.project_id, options.file, options.gitlab_token, options.title, status_message))
