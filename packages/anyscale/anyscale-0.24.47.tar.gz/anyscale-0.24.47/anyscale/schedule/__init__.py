from typing import Optional

from anyscale._private.anyscale_client import AnyscaleClientInterface
from anyscale._private.sdk import sdk_docs
from anyscale._private.sdk.base_sdk import Timer
from anyscale.cli_logger import BlockLogger
from anyscale.schedule._private.schedule_sdk import PrivateScheduleSDK
from anyscale.schedule.commands import _APPLY_ARG_DOCSTRINGS, _APPLY_EXAMPLE, apply
from anyscale.schedule.models import ScheduleConfig, ScheduleState, ScheduleStatus


class ScheduleSDK:
    def __init__(
        self,
        *,
        client: Optional[AnyscaleClientInterface] = None,
        logger: Optional[BlockLogger] = None,
        timer: Optional[Timer] = None,
    ):
        self._private_sdk = PrivateScheduleSDK(
            client=client, logger=logger, timer=timer
        )

    @sdk_docs(
        doc_py_example=_APPLY_EXAMPLE, arg_docstrings=_APPLY_ARG_DOCSTRINGS,
    )
    def apply(self, config: ScheduleConfig,) -> str:  # noqa: F811
        """Apply or update a schedule.

        Returns the id of the schedule.
        """
        return self._private_sdk.apply(config=config)
