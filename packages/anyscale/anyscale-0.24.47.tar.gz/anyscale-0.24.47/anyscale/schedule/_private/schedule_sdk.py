from typing import Optional

from anyscale._private.anyscale_client.common import AnyscaleClientInterface
from anyscale._private.sdk.base_sdk import BaseSDK, Timer
from anyscale.cli_logger import BlockLogger
from anyscale.client.openapi_client.models.create_schedule import CreateSchedule
from anyscale.client.openapi_client.models.decorated_schedule import DecoratedSchedule
from anyscale.client.openapi_client.models.schedule_config import (
    ScheduleConfig as BackendScheduleConfig,
)
from anyscale.job._private.job_sdk import PrivateJobSDK
from anyscale.job.models import JobConfig
from anyscale.schedule.models import ScheduleConfig


logger = BlockLogger()


class PrivateScheduleSDK(BaseSDK):
    def __init__(
        self,
        *,
        logger: Optional[BlockLogger] = None,
        client: Optional[AnyscaleClientInterface] = None,
        timer: Optional[Timer] = None,
    ):
        super().__init__(logger=logger, client=client, timer=timer)
        self._job_sdk = PrivateJobSDK(logger=self.logger, client=self.client)

    def apply(self, config: ScheduleConfig) -> str:
        job_config = config.job_config
        assert isinstance(job_config, JobConfig)
        name = job_config.name or self._job_sdk.get_default_name()

        compute_config_id, cloud_id = self._job_sdk.resolve_compute_config_and_cloud_id(
            compute_config=job_config.compute_config, cloud=job_config.cloud
        )

        project_id = self.client.get_project_id(
            parent_cloud_id=cloud_id, name=job_config.project
        )

        schedule: DecoratedSchedule = self.client.apply_schedule(
            CreateSchedule(
                name=name,
                project_id=project_id,
                config=self._job_sdk.job_config_to_internal_prod_job_conf(
                    config=job_config,
                    name=name,
                    cloud_id=cloud_id,
                    compute_config_id=compute_config_id,
                ),
                schedule=BackendScheduleConfig(
                    cron_expression=config.cron_expression, timezone=config.timezone,
                ),
            )
        )

        self.logger.info(f"Schedule '{name}' submitted, ID: '{schedule.id}'.")

        return schedule.id
