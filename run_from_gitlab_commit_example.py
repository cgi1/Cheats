"""
Sometimes you just need a quick way to continously scanning for new commits in a dedicated repo and than fullfill some tasks
That is the reason behind this script.
@author: Christoph Giese cgi
"""

import subprocess
import sys, os, py
import datetime
import time
import git
from git import Git, Repo


import traceback

SLEEP_SECONDS = 60 # Between the checks for a new commit in gitlab repo


REPO_REMOTE = 'git@gitlab.com:cgi1/my_gitlab_repo.git'
MASTER_BRANCH = 'origin/master'
REPO_NAME = 'my_gitlab_repo'
BASE_DIR = '/home/cgi/BUILDER/repo/'
REPO_DIR = os.path.join(BASE_DIR, '%s/') % REPO_NAME

# Enabling SSH auth from the OS password manager - nice
global_git = Git()
global_git.update_environment(
    **{k: os.environ[k] for k in os.environ if k.startswith('SSH')}
)

def trigger_new_commit(args, print_response_of_started_program=True):
    print('%s trigger_new_commit %s' % (datetime.datetime.now(), args))

    try:
        # A hard cut here - Running the code of the manipulated repo
        import subprocess

        cmd =  'python3 %s/db_timescale/jobs_continously/YOUR_DIR/YOUR_FILE.py ' % REPO_DIR
        # Your arugments for the program
        now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        cmd += ' > /var/log/ktp_%s_%s_%s.log' % (args.get('gitlab_branch','UNKWN').replace('/','_'),
                                                                 now, args.get('gitlab_commit','UNKWN'))

        print("Start process %s. This typically takes a lot of time.." % cmd)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate()

        if print_response_of_started_program:
            if isinstance(out,str):
                result = out.split('\n')
                for lin in result:
                    if not lin.startswith('#'):
                        print(lin)

    except:
        print("Error>Failed to execute trade_ktp_test.py (%s)"
              % traceback.format_exc())

    print('%s Finished trigger_new_commit' % datetime.datetime.now())

def exec_cli(command, v=True):
    import subprocess
    try:
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate()

        if v:
            if isinstance(out, str):
                result = out.split('\n')
                for lin in result:
                    if not lin.startswith('#'):
                        print(lin)
            else:
                print("exec_cli resp out=%s err=%s" % (out, err))
        return out,err
    except:
        print("Error>Failed to exec %s with error %s" % (command, traceback.format_exc()))

if __name__ == '__main__':


    import argparse

    parser = argparse.ArgumentParser(description='Gets fresh code from Gitlab repo and runs backtests afterwards. '
                                                 'If used with debug_remote, it will directly run the code from the remote deployment dir of the IDE')
    parser.add_argument('-pp', '--parallel-processes', help='Parallel processes to use', required=False, default=1) # 12
    parser.add_argument('-f', '--enforce-run', help='Enforces a backtest run, even if there is no updated commit there.', required=False, default=0) # 1=Yes
    parser.add_argument('-runs', '--runs', help='-1 is endless loop.', required=False, default=-1) # 1=Yes

    parser.add_argument('-sha', '--gitlab-commit', help='Will checkout a dedicated gitlab commit and runs from it.', required=False, default='HEAD')
    parser.add_argument('-branch', '--gitlab-branch', help='Will checkout a dedicated gitlab branch and runs from it.', required=False, default='debug_remote')

    args = vars(parser.parse_args())
    args['runs'] = int(args['runs'])
    args['enforce_run'] = int(args['enforce_run'])
    print("Starting with args>%s" % args)
    commit_to_test = args['gitlab_commit']
    branch_to_test = args.get('gitlab_branch', 'origin/master')


    def clone_repo_if_not_exists():
        if not os.path.exists(REPO_DIR):
            try:
                cmd_checkout = "cd %s && git clone %s " % (BASE_DIR, REPO_REMOTE)
                exec_cli(command=cmd_checkout, v=True)
                print("%s FIN CLONE %s  to %s." % (datetime.datetime.now(), REPO_REMOTE, BASE_DIR))
            except:
                print("Error>Failed to checkout repo (%s)(%s)"
                      % (REPO_REMOTE, traceback.format_exc()))
        else: print("Repo (%s) already exists." % REPO_DIR)
    clone_repo_if_not_exists()

    repo = git.Repo(REPO_DIR)
    print("Loaded repo (%s)" % repo)
    o = repo.remotes.origin
    print("Selected origin (%s)" % o)

    try:
        # Checkout the master branch and pull first
        # (pull after checking out another branch makes git to belive to pull the origin/master branch)
        # So only pull if we want to get the master branch

        cmd_checkout = "cd %s && git fetch && git checkout %s && git pull origin master" % (REPO_DIR, MASTER_BRANCH)
        out, err = exec_cli(command=cmd_checkout, v=True)
        print("%s FIN update to %s@HEAD." % (datetime.datetime.now(), MASTER_BRANCH))

    except:
        print("Failed to checkout (%s)(%s)(%s)" % (REPO_DIR, MASTER_BRANCH, traceback.format_exc()))


    if args['runs'] < 0: print("Start in endless loop with args=%s" % (args))

    run = 0
    while 1:
        run += 1
        if args['runs'] > 0 and run > args['runs']:
            print("Quit because args['runs']=%s is now reached" % (args['runs']))
            break

        try:
            # Checkout the given branch
            cmd_checkout = "cd %s && git checkout %s " % (REPO_DIR, branch_to_test)
            out, err = exec_cli(command=cmd_checkout, v=True)
            print("%s FIN CHECKOUT %s"
                  % (datetime.datetime.now(), branch_to_test))

        except:
            print("Failed to checkout (%s)(%s)" % (REPO_DIR, branch_to_test))

        try:
            commit_before_pull = repo.head.commit
            commit_after_pull = commit_to_test

            if branch_to_test.lower() not in ['debug_remote']:

                if branch_to_test.lower() not in ['origin/master']:

                    cmd_checkout = "cd %s && git reset --hard %s" % (REPO_DIR, commit_after_pull)

                    out, err = exec_cli(command=cmd_checkout, v=True)
                    commit_after_pull = repo.head.commit
                    print("%s FIN PULL. commit_after_pull=%s"
                          % (datetime.datetime.now(), commit_after_pull))
                else:
                    commit_after_pull = repo.head.commit
                    # Do a git reset --hard to discard all changes
                    # which happened between the last branch push and the master HEA
                    cmd_checkout = "cd %s && git reset --hard %s" % (REPO_DIR, commit_after_pull)
                    out, err = exec_cli(command=cmd_checkout, v=True)
                    print("%s FIN RESET HARD %s@%s"
                          % (datetime.datetime.now(), branch_to_test, commit_after_pull))

        except:
            print("Error> QUIT! Failed to get data for branch/commit: %s %s ERROR: %s"
                  % (branch_to_test, commit_to_test, traceback.format_exc()))
            sys.exit(-1)

        if (not commit_after_pull == commit_before_pull) or int(args['enfore_run'])==1:
            msg = 'Catched a new commit (%s)! (or enforce_run=1 (is set to=%s)' % (commit_after_pull, args['enfore_run'])
            args['gitlab_commit'] = str(commit_after_pull)
            trigger_new_commit(args=args)
        else:
            msg = '%s Nothing new. (Last commit=%s' % (datetime.datetime.now(), commit_after_pull)

        print("%s Now sleep for (%s seconds)" % (datetime.datetime.now(), SLEEP_SECONDS))

        time.sleep(SLEEP_SECONDS)
    else:
        trigger_new_commit(args=args)
