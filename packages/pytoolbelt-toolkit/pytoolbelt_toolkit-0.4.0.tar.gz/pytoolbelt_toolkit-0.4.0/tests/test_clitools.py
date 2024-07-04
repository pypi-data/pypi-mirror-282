from argparse import Namespace
from unittest.mock import patch

import pytest

from pytoolbelt.toolkit.clitools import PyToolBeltCommand, entrypoint
from tests.stubs import stub_commands


def test_method():
    class MyCommand(PyToolBeltCommand):
        pass

    assert MyCommand.method() == "mycommand"


def test_call():
    class MyCommand(PyToolBeltCommand):
        pass

    command_instance = MyCommand(Namespace())

    with pytest.raises(NotImplementedError):
        command_instance()  # Call the command instance, it should raise NotImplementedError


def test_args():
    class MyCommand(PyToolBeltCommand):
        args = {"--foo": {"help": "Foo help"}}

    assert MyCommand.args == {"--foo": {"help": "Foo help"}}


def test_help():
    class MyCommand(PyToolBeltCommand):
        help = "Some help"

    assert MyCommand.help == "Some help"


def test_multiple_inheritance():
    class MyCommand(PyToolBeltCommand):
        args = {"--foo": {"help": "Foo help"}}

    class MyOtherCommand(MyCommand):
        args = {"--bar": {"help": "Bar help"}}

    assert MyOtherCommand.args == {"--foo": {"help": "Foo help"}, "--bar": {"help": "Bar help"}}


def test_cli():
    class MyCommand(PyToolBeltCommand):
        args = {"--foo": {"help": "Foo help"}}
        help = "Some help"

        def __call__(self) -> None:
            pass

    args = Namespace(command=MyCommand, foo="bar")
    assert MyCommand(args).cliargs == args


def test_get_commands():
    assert PyToolBeltCommand.discover_commands(stub_commands) == [stub_commands.StubCommand]


@pytest.fixture(autouse=True)
def cleanup_entrypoint():
    yield
    entrypoint._global_flags.clear()
    entrypoint._commands.clear()


def test_command_registration():
    @entrypoint(command="test_cmd", flags=[{"name": "--option", "type": str}], help_msg="Test command")
    def test_func(cliargs):
        return 0

    assert "test_cmd" in entrypoint._commands
    assert entrypoint._commands["test_cmd"]["help_msg"] == "Test command"
    assert entrypoint._commands["test_cmd"]["flags"] == [{"name": "--option", "type": str}]


def test_global_flags():
    flags = [{"name": "--global_option", "type": str}]
    entrypoint.set_global_flags(flags)

    assert flags[0] in entrypoint._global_flags


def test_parser_building():
    version = "1.0.0"
    tool_description = "Test tool description"
    parser = entrypoint.build_parser(version, tool_description)

    # Not a comprehensive test; just a simple check to see if the version and tool description are set correctly.
    assert parser.description == tool_description
    assert any(action for action in parser._actions if action.dest == "version" and action.version == version)


def test_execution():
    @entrypoint(command="execute_test")
    def foo_func(cliargs):
        return 0

    # Note: This isn't the best test because it doesn't actually run the execute() method, but it gives you an idea.
    # Ideally, you'd use a library like `unittest.mock` to mock out sys.argv and see if the command is executed correctly.
    args = Namespace(command="execute_test")
    exit_code = entrypoint.run(args)

    assert exit_code == 0


def test_default_command_registration():
    @entrypoint()
    def default_func(cliargs):
        return 0

    assert "default" in entrypoint._commands
    assert entrypoint._commands["default"]["func"] == default_func


def test_run_command_with_flags():
    flag_value = "sample_value"

    @entrypoint(command="flag_test_cmd", flags=[{"name": "--flag", "type": str}])
    def flag_test_func(cliargs):
        return 0 if cliargs.flag == flag_value else 1

    class MockArgs:
        command = "flag_test_cmd"
        flag = flag_value

    assert entrypoint.run(MockArgs()) == 0

    MockArgs.flag = "wrong_value"
    assert entrypoint.run(MockArgs()) == 1


def test_run_default_command():
    @entrypoint()
    def default_func(cliargs):
        return 0

    class MockArgs:
        command = None

    assert entrypoint.run(MockArgs()) == 0


def test_run_non_existent_command():
    class MockArgs:
        command = "i_dont_exist"

    assert entrypoint.run(MockArgs()) == 1


# Mock command classes for testing
class MockCommandOne(PyToolBeltCommand):
    args = {("--foo",): {"help": "Option for MockCommandOne", "required": True, "type": str}}
    help = "Help for MockCommandOne"


class MockCommandTwo(PyToolBeltCommand):
    args = {("--flag",): {"help": "Flag for MockCommandTwo", "action": "store_true"}}
    help = "Help for MockCommandTwo"


# Mock modules for testing
class MockModuleOne:
    MockCommandOne = MockCommandOne


class MockModuleTwo:
    MockCommandTwo = MockCommandTwo


def test_parse_with_no_modules():
    with patch("sys.argv", ["cli_tool"]):
        with pytest.raises(SystemExit) as e:
            PyToolBeltCommand.parse("1.0")
        assert e.value.code == 2
        assert e.type == SystemExit


def test_parse_with_single_command_module():
    # Mock command line arguments for a specific command in MockModuleOne
    with patch("sys.argv", ["cli_tool", "mockcommandone", "--foo", "test_value"]):
        # Execute parse with a single command module
        parsed_args = PyToolBeltCommand.parse("1.0", MockModuleOne)

        # Assertions to verify correct parsing

        assert parsed_args.command.method() == "mockcommandone", "Failed to parse the command name correctly"
        assert hasattr(parsed_args, "foo"), "Parsed args should have 'option' attribute"
        assert parsed_args.foo == "test_value", "Failed to parse the command option correctly"
