import importlib
import sys

import structlog

from ngs_pipeline_lib.cli import cli
from scripts import configure_logging
from scripts.run.models import RunSettings

logger = structlog.getLogger("ngs-run")


def run():
    settings = RunSettings()
    configure_logging(
        verbose=settings.verbose,
        json=settings.json_logger,
        log_file_path=settings.log_file,
    )
    sys.path.insert(0, ".")
    importlib.import_module(settings.process_package, package=".")

    try:
        cli()
    except ValueError as e:
        logger.error(
            "Specified module doesn't contain any @cli.command. Check your PROCESS_PACKAGE env var"
        )
        raise e
