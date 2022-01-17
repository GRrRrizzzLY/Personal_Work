import datetime as dt
import os

import zulip
from dateutil.relativedelta import relativedelta

import conftest


def build_ended_message(build_name=os.environ['JOB_NAME'], build_number=os.environ['BUILD_NUMBER'],
                        build_url=os.environ['BUILD_URL'], commit_number=os.environ['GIT_COMMIT']):
    f = open('success', 'r')
    count_success = int(f.read())
    f.close()

    f = open('failure', 'r')
    count_failure = int(f.read())
    f.close()

    f = open('skipped', 'r')
    count_skipped = int(f.read())
    f.close()

    count_all = count_failure + count_success + count_skipped
    str_count_all = str(count_all)
    count_passed_percent = (100 / count_all) * count_success
    str_count_passed_percent = "%.2f" % count_passed_percent
    count_failure_percent = (100 / count_all) * count_failure
    str_count_failure_percent = "%.2f" % count_failure_percent
    count_skipped_percent = (100 / count_all) * count_skipped
    str_count_skipped_percent = "%.2f" % count_skipped_percent

    commit_name = 'COMMIT_NAME_GOES_HERE' + commit_number
    results_page = 'BUILD_GOES_HERE' + build_number + '/allure/'

    f = open('timer', 'r')
    timer = f.read()
    f.close()
    start_timer = dt.datetime(int(timer.split(',')[0]), int(timer.split(',')[1]), int(timer.split(',')[2]),
                              int(timer.split(',')[3]), int(timer.split(',')[4]), int(timer.split(',')[5]))
    stop_timer = dt.datetime.now()
    raw_timer = relativedelta(start_timer, stop_timer)

    time_message = 'Duration: '
    if raw_timer.hours != 0:
        time_message += str(abs(raw_timer.hours)) + ' hours '
    if raw_timer.minutes != 0:
        time_message += str(abs(raw_timer.minutes)) + ' minutes '
    if raw_timer.seconds != 0:
        time_message += str(abs(raw_timer.seconds)) + ' seconds '

    client = zulip.Client(config_file=conftest.ZULIPRC)

    request = {
        "type": "stream",
        "to": "QA Automation",
        "topic": "Notifications",
        "content": {}}

    part_1 = '**Autotests for: **`'\
             + build_name + '` **Branch: **[develop]('\
             + commit_name + ')** | Build: **[#'\
             + build_number + ']('\
             + build_url + ') **| COMPLETED '\
             + str_count_all + ' TESTS!**'

    part_2 = '**PASSED: **'\
             + str_count_passed_percent +\
             '**% (' + str(count_success) + ') | SKIPPED: **'\
             + str_count_skipped_percent +\
             '**% (' + str(count_skipped) + ') | FAILED: **'\
             + str_count_failure_percent +\
             '**% (' + str(count_failure) + ') | [RESULTS]('\
             + results_page + ')**'

    if count_passed_percent == 0:
        request['content'] = '🔴 ' + part_1 +\
                             '\n\n🔴 ' + part_2 +\
                             '\n\n🔴 ' + '**' + time_message + '**' +\
                             '\n\n🔴 @**Ilya Knyazev**'

    elif 0 < count_passed_percent < 51:
        request['content'] = '🟠 ' + part_1 + \
                             '\n\n🟠 ' + part_2 + \
                             '\n\n🟠 ' + '**' + time_message + '**' +\
                             '\n\n🟠 @**Ilya Knyazev**'

    elif 50 < count_passed_percent < 100:
        request['content'] = '🟡 ' + part_1 + \
                             '\n\n🟡 ' + part_2 + \
                             '\n\n🟡 ' + '**' + time_message + '**' +\
                             '\n\n🟡 @**Ilya Knyazev**'

    else:
        request['content'] = '🟢 ' + part_1 + \
                             '\n\n🟢 ' + part_2 + \
                             '\n\n🟢 ' + '**' + time_message + '**'

    result = client.send_message(request)

    os.remove('success')
    os.remove('failure')
    os.remove('skipped')
    os.remove('timer')
