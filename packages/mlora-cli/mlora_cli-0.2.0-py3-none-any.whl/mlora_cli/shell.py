import cmd

from .dispatcher import help_dispatcher, do_dispatcher
from .dataset import help_dataset, do_dataset
from .file import help_file, do_file
from .adapter import help_adapter, do_adapter
from .task import help_task, do_task


def help_quit(_):
    print("Quit the cli")


def do_quit(*_):
    exit(0)


class mLoRAShell(cmd.Cmd):
    intro = "Welcome to the mLoRA CLI. Type help or ? to list commands.\n"
    prompt = "(mLoRA) "

    help_quit = help_quit
    do_quit = do_quit

    help_dispatcher = help_dispatcher
    do_dispatcher = do_dispatcher

    help_file = help_file
    do_file = do_file

    help_dataset = help_dataset
    do_dataset = do_dataset

    help_adapter = help_adapter
    do_adapter = do_adapter

    help_task = help_task
    do_task = do_task


def cmd_loop():
    mLoRAShell().cmdloop()
