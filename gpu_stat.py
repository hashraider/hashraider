#!/usr/bin/env python

import subprocess
import logging
import datetime
logging.basicConfig(format='%(asctime)s %(message)s')
logging.Formatter.formatTime = (
    lambda self, record, datefmt=None: 
    datetime.datetime.fromtimestamp (record.created, datetime.timezone.utc)
        .astimezone()
        .isoformat(sep="T",timespec="milliseconds")
)



class GPUStats:
    '''
    Simple class designed to pull the common mining stats from the GPU.
    '''

    def __init__(self):
        pass

    def __str__(self):
        return "TODO: Call stat fuction and build summary"

    def __repr__(self):
        return "GPUStats(TODO=Value)"

    def _run(self, cmd, shell=True, quit_on_failure=True):
        '''
        Runs a system command and can return the failure or exit the program.
        
        Parameters
        ----------
        cmd : string
            shell command string to be ran
        shell : bool, optional
            If shell is True, the specified command will be executed through
            the shell. (Default is True)
        quit_on_failure : bool, optional
            If we get a bad return code and we want to kill the current
            running python process.
        
        Returns
        ------- 
        string
            Output of the command that ran
        
        Raises
        ------
        CalledProcessError
            Exception raised when a process run by check_call() or 
            check_output() returns a non-zero exit status.
        '''

        try:
            result = subprocess.check_output(
                cmd,
                shell=shell,
                stderr=subprocess.STDOUT
                )

            return result.rstrip()

        except subprocess.CalledProcessError as e:
            logging.critical(
                "Failed to run command:\"{}\" CODE:\"{}\" OUTPUT={}"
                    .format(e.cmd, e.returncode, e.output)
            )
            if quit_on_failure:
                # If we dont want to trust the data if the command fails and think
                # its better to exit than report in any data we will quit.
                
                quit(1)
            else:
                # raise the error so that the upstream can process the failure.
                raise

if __name__ == "__main__":
    gs = GPUStats()
    print(gs._run("ls"))