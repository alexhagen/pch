import sys
import argparse
from argparse import RawTextHelpFormatter
import logging
from process_watcher.process import *

class process_chainer(object):
    def __init__(self, pattern='*', pid='*', chain_command=None):
        # dict of all the process watching objects pid -> ProcessByPID
        # items removed when process ends
        watched_processes = {}

        process_matcher = ProcessMatcher()
        new_processes = ProcessIDs()

        process_matcher.add_command_wildcard('polimi')

        # Initial processes matching conditions
        for pid in process_matcher.matching(new_processes):
            if pid not in watched_processes:
                watched_processes[pid] = ProcessByPID(pid)

        if not watched_processes and not watch_new:
            logging.warning('No processes found to watch.')
            sys.exit()

        logging.info('Watching {} processes:'.format(len(watched_processes)))
        for pid, process in watched_processes.items():
            logging.info(process.info())
            print(process.info())

    def wait(self):
        try:
            to_delete = []
            while True:
                time.sleep(15)
                # Need to iterate copy since removing within loop.
                for pid, process in watched_processes.items():
                    try:
                        running = process.check()
                        if not running:
                            to_delete.append(pid)

                            logging.info('Process stopped\n%s', process.info())
                            '''
                            for comm, send_args in comms:
                                template = '{executable} process {pid} ended'
                                comm.send(process=process, subject_format=template, **send_args)
                            '''

                    except:
                        logging.exception('Exception encountered while checking or communicating about process {}'.format(pid))
                        if pid not in to_delete:
                            # Exception raised in check(), queue PID to be deleted
                            to_delete.append(pid)

                if to_delete:
                    for pid in to_delete:
                        del watched_processes[pid]

                    to_delete.clear()

                elif not watched_processes:
                    print("processes ended")
                    return
