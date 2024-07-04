# Logging of test results is compliant with the Test Anything Protocal (TAP)
# https://testanything.org/tap-specification.html

import difflib

GlobalTestLog = {
    'idx'         : 0,
    'ok'          : list(),
    'ok_name'     : list(),
    'not_ok'      : list(),
    'not_ok_name' : list(),
}

def log_result(is_ok, test_name, test_log=None):
    # set log storage
    global GlobalTestLog
    if test_log is None:
        test_log = GlobalTestLog
    # increment test index
    test_log['idx'] += 1
    # print and add to log
    if is_ok:
        print('ok {} {}'.format(test_log['idx'], test_name))
        test_log['ok'].append(test_log['idx'])
        test_log['ok_name'].append(test_name)
    else:
        print('not ok {} {}'.format(test_log['idx'], test_name))
        test_log['not_ok'].append(test_log['idx'])
        test_log['not_ok_name'].append(test_name)

def log_diff(lines_ref, lines_chk, prefix='# '):
    d = difflib.Differ()
    diff = list(d.compare(lines_ref.splitlines(), lines_chk.splitlines()))
    print(prefix + 'diff lines_ref lines_chk')
    for line in diff:
        print(prefix + line.rstrip())

def log_summary(test_log=None):
    # set log storage
    global GlobalTestLog
    if test_log is None:
        test_log = GlobalTestLog
    # count results
    n_ok     = len(test_log['ok'])
    n_not_ok = len(test_log['not_ok'])
    n_total  = n_ok + n_not_ok
    # print results
    print('{}..{}'.format(0, test_log['idx']))
    if n_not_ok:
        print('# FAILED', ' '.join(str(i) for i in test_log['not_ok']))
        print('# failed {}/{} tests; {}% ok'.format(n_not_ok, n_total, 100.0*n_ok/n_total))
