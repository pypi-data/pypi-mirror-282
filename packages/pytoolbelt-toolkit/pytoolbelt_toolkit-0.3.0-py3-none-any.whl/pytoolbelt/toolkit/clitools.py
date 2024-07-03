import inspect
from argparse import ArgumentParser, Namespace
from types import ModuleType
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar

CommandType = TypeVar("CommandType", bound="Command")
CommandModulesType = TypeVar(name="CommandModulesType", bound="CommandModules")
T = TypeVar("T", bound=Callable[..., Any])
CommandData = Dict[str, Any]
CommandDict = Dict[str, CommandData]
FlagDict = Dict[str, Any]


class _CommandMeta(type):
    def __new__(mcs, name, bases, attrs):
        # Merging 'args' dictionaries of parent classes and the new class
        new_args = {}
        for base in reversed(bases):
            if hasattr(base, "args"):
                new_args.update(base.args)
        if "args" in attrs:
            new_args.update(attrs["args"])
        attrs["args"] = new_args

        return super().__new__(mcs, name, bases, attrs)


class PyToolBeltCommand(metaclass=_CommandMeta):
    args = {}
    help = ""

    def __init__(self, cliargs: Namespace) -> None:
        self.cliargs = cliargs

    @classmethod
    def method(cls) -> str:
        return cls.__name__.lower()

    def __call__(self) -> None:
        raise NotImplementedError

    @staticmethod
    def discover_commands(module: ModuleType) -> List[Type["PyToolBeltCommand"]]:
        commands = []
        for i, _class in inspect.getmembers(module, inspect.isclass):
            if _class != PyToolBeltCommand:
                if issubclass(_class, PyToolBeltCommand) and not _class.__name__.startswith("Base"):
                    commands.append(_class)
        return commands

    @staticmethod
    def parse(version: str, *modules: ModuleType) -> Namespace:
        parser = ArgumentParser()
        sub_parser = parser.add_subparsers(dest="command")
        sub_parser.required = True
        parser.add_argument("--version", action="version", version=version)

        for module in modules:
            for command in PyToolBeltCommand.discover_commands(module):
                p = sub_parser.add_parser(command.method(), help=command.help)
                for args, kwargs in command.args.items():
                    p.add_argument(*args, **kwargs)
                p.set_defaults(command=command)
        return parser.parse_args()


class entrypoint:
    _commands: CommandDict = {}
    _global_flags: List[FlagDict] = []

    def __init__(
        self, *, command: Optional[str] = None, flags: Optional[List[FlagDict]] = None, help_msg: Optional[str] = None
    ) -> None:
        self.command_data: CommandData = {"func": None, "flags": flags or [], "help_msg": help_msg}
        self.command_name: str = command or "default"

    def __call__(self, func: T) -> T:
        self.command_data["func"] = func
        self._commands[self.command_name] = self.command_data
        return func

    @classmethod
    def build_parser(cls, version: str, tool_description: str) -> ArgumentParser:
        parser = ArgumentParser(description=tool_description)
        parser.add_argument("--version", action="version", version=version)

        for arg_data in cls._global_flags:
            parser.add_argument(arg_data.pop("name"), **arg_data)

        subparsers = parser.add_subparsers(title="commands", dest="command")
        for cmd, data in cls._commands.items():
            if cmd == "default":  # Skip default for sub-commands
                continue
            command_parser = subparsers.add_parser(cmd, help=data.get("help_msg"))
            for arg_data in data.get("flags", []):
                command_parser.add_argument(arg_data.pop("name"), **arg_data)

        return parser

    @classmethod
    def run(cls, args: Namespace) -> int:
        func = cls._commands.get(args.command or "default", {}).get("func")
        if func:
            return func(cliargs=args)
        return 1  # Return an error code if no suitable command or default is found

    @classmethod
    def set_global_flags(cls, flags: List[FlagDict]) -> None:
        cls._global_flags.extend(flags)

    @staticmethod
    def execute(
        version: Optional[str] = "0.0.0", tool_description: Optional[str] = "A tool built with pytoolbelt toolkit."
    ) -> None:
        parser = entrypoint.build_parser(version=version, tool_description=tool_description)
        args = parser.parse_args()
        exit_code = entrypoint.run(args)
        exit(exit_code)
