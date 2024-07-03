import os
from typing import Generator, Optional
import uuid

import click
from click.testing import CliRunner
import pytest

from anyscale._private.sdk import _LAZY_SDK_SINGLETONS
from anyscale.commands.schedule_commands import apply
from anyscale.job.models import JobConfig
from anyscale.schedule.commands import _SCHEDULE_SDK_SINGLETON_KEY
from anyscale.schedule.models import ScheduleConfig


def _get_test_file_path(subpath: str) -> str:
    return os.path.join(os.path.dirname(__file__), "test_files/", subpath)


EMPTY_CONFIG_PATH = _get_test_file_path("schedule_config_files/empty.yaml")
MINIMAL_CONFIG_PATH = _get_test_file_path("schedule_config_files/minimal.yaml")
FULL_CONFIG_PATH = _get_test_file_path("schedule_config_files/full.yaml")
UNRECOGNIZED_OPTION_CONFIG_PATH = _get_test_file_path(
    "schedule_config_files/unrecognized_option.yaml"
)


class FakeScheduleSDK:
    DEFAULT_SCHEDULE_NAME = "default-fake-schedule-name"

    def __init__(self):
        self.applied_config: Optional[ScheduleConfig] = None
        self.applied_id: Optional[str] = None
        self.applied_name: Optional[str] = None

    def apply(self, config: ScheduleConfig):
        assert isinstance(config, ScheduleConfig)
        self.applied_config = config
        self.applied_id = str(uuid.uuid4())

        job_config = self.applied_config.job_config
        assert isinstance(job_config, JobConfig)
        self.applied_name = (
            job_config.name
            if job_config.name is not None
            else self.DEFAULT_SCHEDULE_NAME
        )
        return self.applied_id


@pytest.fixture()
def fake_schedule_sdk() -> Generator[FakeScheduleSDK, None, None]:
    fake_schedule_sdk = FakeScheduleSDK()
    _LAZY_SDK_SINGLETONS[_SCHEDULE_SDK_SINGLETON_KEY] = fake_schedule_sdk
    try:
        yield fake_schedule_sdk
    finally:
        del _LAZY_SDK_SINGLETONS[_SCHEDULE_SDK_SINGLETON_KEY]


def _assert_error_message(result: click.testing.Result, *, message: str):
    assert result.exit_code != 0
    assert message in result.stdout


class TestApply:
    def test_missing_arg(self, fake_schedule_sdk):
        runner = CliRunner()
        result = runner.invoke(apply)
        _assert_error_message(
            result, message="Error: Missing option '--config-file' / '-f'."
        )

    def test_config_file_not_found(self, fake_schedule_sdk):
        runner = CliRunner()
        result = runner.invoke(apply, ["-f", "missing_config.yaml"])
        _assert_error_message(
            result, message="Schedule config file 'missing_config.yaml' not found.",
        )

    @pytest.mark.parametrize(
        "config_file_arg", [MINIMAL_CONFIG_PATH, FULL_CONFIG_PATH],
    )
    def test_basic(self, fake_schedule_sdk, config_file_arg):
        runner = CliRunner()
        result = runner.invoke(apply, ["-f", config_file_arg])
        assert result.exit_code == 0, result.stdout
        assert fake_schedule_sdk.applied_config is not None

    def test_override_name(self, fake_schedule_sdk):
        runner = CliRunner()
        name = "test-different-name"
        result = runner.invoke(apply, ["--name", name, "-f", FULL_CONFIG_PATH])
        assert result.exit_code == 0
        assert result.exit_code == 0, result.stdout
        assert fake_schedule_sdk.applied_config is not None
        assert fake_schedule_sdk.applied_name == name
