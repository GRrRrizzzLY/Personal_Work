import datetime as dt
import os

import zulip

import conftest


def build_start_message(build_name=os.environ['JOB_NAME'], build_number=os.environ['BUILD_NUMBER'],
                        build_url=os.environ['BUILD_URL'], commit_number=os.environ['GIT_COMMIT'],
                        build_started_by=os.environ['BUILD_USER']):
    date = dt.datetime.now()

    f = open('timer', 'w')
    f.write(str(date.year) + ',' + str(date.month) + ',' + str(date.day) + ',' + str(date.hour) + ',' + str(
        date.minute) + ',' + str(date.second) + ',' + str(date.microsecond))
    f.close()

    client = zulip.Client(config_file=conftest.ZULIPRC)

    commit_name = 'COMMIT_NAME_GOES_HERE' + commit_number

    request = {
        "type": "stream",
        "to": "QA Automation",
        "topic": "Notifications",
        "content": ':play: **Autotests for: **`' + build_name + '` **Branch:** [develop]('
                   + commit_name + ') **| Build:** [#'
                   + build_number + '](' + build_url + ') **| STARTED!**\n\n:play: Build started by: **'
                   + build_started_by + '**'}

    result = client.send_message(request)
