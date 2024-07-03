from anyscale._private.sdk import sdk_command
from anyscale.cli_logger import BlockLogger
from anyscale.schedule._private.schedule_sdk import PrivateScheduleSDK
from anyscale.schedule.models import ScheduleConfig


logger = BlockLogger()

_SCHEDULE_SDK_SINGLETON_KEY = "schedule_sdk"

_APPLY_EXAMPLE = """
import anyscale
from anyscale.job.models import JobConfig
from anyscale.schedule.models import ScheduleConfig

anyscale.schedule.apply(
    ScheduleConfig(
        cron_expression="0 0 * * * *",
        job_config=JobConfig(
            name="my-job",
            entrypoint="python main.py",
            working_dir=".",
        )
    )
)
"""

_APPLY_ARG_DOCSTRINGS = {"config": "The config options defining the schedule."}


@sdk_command(
    _SCHEDULE_SDK_SINGLETON_KEY,
    PrivateScheduleSDK,
    doc_py_example=_APPLY_EXAMPLE,
    arg_docstrings=_APPLY_ARG_DOCSTRINGS,
)
def apply(config: ScheduleConfig, *, _sdk: PrivateScheduleSDK) -> str:
    """Apply or update a schedule.

    Returns the id of the schedule.
    """
    return _sdk.apply(config)
