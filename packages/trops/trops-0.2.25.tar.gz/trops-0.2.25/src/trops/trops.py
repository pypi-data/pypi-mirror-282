import logging
import os
import subprocess

from configparser import ConfigParser
from getpass import getuser
from pathlib import Path
from socket import gethostname
from textwrap import dedent
from typing import Any, List

from .utils import absolute_path, strtobool


class Trops:
    """Trops Class"""

    def __init__(self, args: Any, other_args: List[str]) -> None:
        """Initialize the Trops class"""

        # Make args sharable among functions
        self.args = args
        self.other_args = other_args
        # Set username and hostname
        self.username = getuser()
        self.hostname = gethostname().split('.')[0]
        # Set trops_dir
        self.trops_dir = absolute_path(os.getenv('TROPS_DIR'))

        # Create the log directory
        self.trops_log_dir = os.path.join(self.trops_dir, 'log')
        self.trops_logfile = os.path.join(self.trops_log_dir, 'trops.log')
        os.makedirs(self.trops_log_dir, exist_ok=True)

        # Set trops_env
        self.trops_env = args.env if hasattr(args, 'env') and args.env else os.getenv('TROPS_ENV', False)

        # Set trops_sid
        self.trops_sid = os.getenv('TROPS_SID', False)

        self.config = ConfigParser()
        self.conf_file = os.path.join(self.trops_dir, 'trops.cfg')
        if os.path.isfile(self.conf_file):
            self.config.read(self.conf_file)

            if self.config.has_section(self.trops_env):
                self.git_dir = absolute_path(self.get_config_value('git_dir'))
                self.work_tree = absolute_path(self.get_config_value('work_tree'))
                self.git_cmd = ['git', f'--git-dir={self.git_dir}', f'--work-tree={self.work_tree}']

                self.sudo = strtobool(self.get_config_value('sudo', default='False'))
                if self.sudo:
                    self.git_cmd = ['sudo'] + self.git_cmd

                self.trops_logfile = absolute_path(self.get_config_value('logfile', default=self.trops_logfile))

                self.disable_header = strtobool(self.get_config_value('disable_header', default='False'))

                self.ignore_cmds = self.get_config_value('ignore_cmds', default='').split(',')

                self.git_remote = self.get_config_value('git_remote', default=False)
                if self.git_remote:
                    self.glab_cmd = ['glab', '-R', self.git_remote]

                self.trops_tags = os.getenv('TROPS_TAGS', self.get_config_value('tags', default=False))
                if self.trops_tags:
                    self.trops_tags = self.trops_tags.replace(' ', '')


        if self.trops_logfile:
            self.setup_logging()

    def setup_logging(self) -> None:
        logging.basicConfig(format=f'%(asctime)s { self.username }@{ self.hostname } %(levelname)s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            filename=self.trops_logfile,
                            level=logging.DEBUG)
        self.logger = logging.getLogger()

    def get_config_value(self, key: str, default: str = None) -> str:
        """Get a value from the configuration file."""
        try:
            return self.config[self.trops_env][key]
        except KeyError:
            if default is not None:
                return default
            print(f'{key} does not exist in your configuration file')
            exit(1)
        
    def add_and_commit_file(self, file_path) -> None:

        cmd = self.git_cmd + ['ls-files', file_path]
        result = subprocess.run(cmd, capture_output=True)
        if result.stdout.decode("utf-8"):
            git_msg = f"Update { file_path }"
            log_note = 'UPDATE'
        else:
            git_msg = f"Add { file_path }"
            log_note = 'ADD'
        if self.trops_tags:
            git_msg = f"{ git_msg } ({ self.trops_tags })"
        cmd = self.git_cmd + ['add', file_path]
        subprocess.call(cmd)
        cmd = self.git_cmd + ['commit', '-m',
                              git_msg, file_path]
        # Commit the change if needed
        result = subprocess.run(cmd, capture_output=True)
        # If there's an update, log it in the log file
        if result.returncode == 0:
            msg = result.stdout.decode('utf-8').splitlines()[0]
            print(msg)
            cmd = self.git_cmd + \
                ['log', '--oneline', '-1', file_path]
            output = subprocess.check_output(
                cmd).decode("utf-8").split()
            if file_path in output:
                mode = oct(os.stat(file_path).st_mode)[-4:]
                owner = Path(file_path).owner()
                group = Path(file_path).group()
                message = f"FL trops show -e { self.trops_env } { output[0] }:{ absolute_path(file_path).lstrip(self.work_tree)}  #> { log_note } O={ owner },G={ group },M={ mode }"
                if self.trops_sid:
                    message = f"{ message } TROPS_SID={ self.trops_sid }"
                message = f"{ message } TROPS_ENV={ self.trops_env }"
                if self.trops_tags:
                    message = message + f" TROPS_TAGS={self.trops_tags}"

                self.logger.info(message)
        else:
            print('No update')


class TropsMain(Trops):
    """TropsMain Class"""

    def __init__(self, args: Any, other_args: List[str]) -> None:
        """Initialize the TropsMain class"""
        super().__init__(args, other_args)

    def git(self) -> None:
        """Git wrapper command"""
        cmd = self.git_cmd + self.other_args
        subprocess.run(cmd, check=True)

    def glab(self) -> None:
        """Glab wrapper command"""

        if self.other_args == ['auth', 'login']:
            hostname = input(
                'Your GitLab hostname(default: gitlab.com): ') or 'gitlab.com'
            cmd = ['glab', 'auth', 'login', '--hostname', hostname]
        else:
            cmd = self.glab_cmd + self.other_args
        subprocess.call(cmd)

    def check(self) -> None:
        """Git status wrapper command"""

        cmd = self.git_cmd + ['status']
        subprocess.call(cmd)

    def ll(self) -> None:
        """Shows the list of git-tracked files"""

        if os.getenv('TROPS_ENV') == None:
            raise SystemExit("You're not under any trops environment")

        dirs = self.args.dirs
        for dir in dirs:
            if os.path.isdir(dir):
                os.chdir(dir)
                cmd = self.git_cmd + ['ls-files']
                output = subprocess.check_output(cmd)
                for f in output.decode("utf-8").splitlines():
                    cmd = ['ls', '-al', f]
                    subprocess.call(cmd)

    def show(self) -> None:
        """trops show hash[:path]"""

        cmd = self.git_cmd + ['show', self.args.commit]
        subprocess.call(cmd)

    def branch(self) -> None:
        """trops branch"""

        cmd = self.git_cmd + ['branch', '-a']
        subprocess.call(cmd)

    def fetch(self) -> None:
        """trops fetch"""

        cmd = self.git_cmd + ['fetch', '-a']
        subprocess.call(cmd)

    def touch(self) -> None:

        for file_path in self.args.paths:

            self._touch_file(file_path)

    def _touch_file(self, file_path) -> None:
        """Add a file or directory in the git repo"""

        file_path = absolute_path(file_path)

        # Check if the path exists
        if not os.path.exists(file_path):
            print(f"{ file_path } doesn't exists")
            exit(1)
        # TODO: Allow touch directory later
        if not os.path.isfile(file_path):
            message = f"""\
                Error: { file_path } is not a file
                Only file is allowed to be touched"""
            print(dedent(message))
            exit(1)

        # Check if the path is in the git repo
        cmd = self.git_cmd + ['ls-files', file_path]
        result = subprocess.run(cmd, capture_output=True)
        if result.returncode != 0:
            print(result.stderr.decode('utf-8'))
            exit(result.returncode)
        output = result.stdout.decode('utf-8')
        # Set the message based on the output
        if output:
            git_msg = f"Update { file_path }"
            log_note = "UPDATE"
        else:
            git_msg = f"Add { file_path }"
            log_note = "ADD"
        if self.trops_tags:
            git_msg = f"{ git_msg } ({ self.trops_tags })"
        # Add and commit
        cmd = self.git_cmd + ['add', file_path]
        subprocess.call(cmd)
        cmd = self.git_cmd + ['commit', '-m', git_msg, file_path]
        subprocess.call(cmd)
        cmd = self.git_cmd + ['log', '--oneline', '-1', file_path]
        output = subprocess.check_output(
            cmd).decode("utf-8").split()
        if file_path in output:
            env = self.trops_env
            commit = output[0]
            path = absolute_path(file_path).lstrip(self.work_tree)
            mode = oct(os.stat(file_path).st_mode)[-4:]
            owner = Path(file_path).owner()
            group = Path(file_path).group()
            message = f"FL trops show -e { env } { commit }:{ path }  #> { log_note } O={ owner },G={ group },M={ mode }"
            if self.trops_sid:
                message = message + f" TROPS_SID={ self.trops_sid }"
            message = message + f" TROPS_ENV={ env }"
            if self.trops_tags:
                message = message + f" TROPS_TAGS={self.trops_tags}"
            self.logger.info(message)

    def drop(self) -> None:

        for file_path in self.args.paths:

            self._drop_file(file_path)

    def _drop_file(self, file_path) -> None:
        """Remove a file from the git repo"""

        file_path = absolute_path(file_path)

        # Check if the path exists
        if not os.path.exists(file_path):
            print(f"{ file_path } doesn't exists")
            exit(1)
        # TODO: Allow touch directory later
        if not os.path.isfile(file_path):
            message = f"""\
                Error: { file_path } is not a file.
                A directory is not allowed to say goodbye"""
            print(dedent(message))
            exit(1)

        # Check if the path is in the git repo
        cmd = self.git_cmd + ['ls-files', file_path]
        output = subprocess.check_output(cmd).decode("utf-8")
        # Set the message based on the output
        if output:
            cmd = self.git_cmd + ['rm', '--cached', file_path]
            subprocess.call(cmd)
            git_msg = f"Goodbye { file_path }"
            if self.trops_tags:
                git_msg = f"{ git_msg } ({ self.trops_tags })"
            cmd = self.git_cmd + ['commit', '-m', git_msg]
            subprocess.call(cmd)
        else:
            message = f"{ file_path } is not in the git repo"
            exit(1)
        cmd = self.git_cmd + ['log', '--oneline', '-1', file_path]
        output = subprocess.check_output(
            cmd).decode("utf-8").split()
        message = f"FL trops show -e { self.trops_env } { output[0] }:{ absolute_path(file_path).lstrip('/')}  #> BYE BYE"
        if self.trops_sid:
            message = message + f" TROPS_SID={ self.trops_sid }"
        message = message + f" TROPS_ENV={ self.trops_env }"
        if self.trops_tags:
            message = message + f" TROPS_TAGS={self.trops_tags}"
        self.logger.info(message)
