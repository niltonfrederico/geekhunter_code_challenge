from logging import INFO

from abundantia_api.celery_app import app


class TaskLogger:
    def __init__(self, task, logger, level=None):
        self.task = task
        self.logger = logger
        self.level = level or INFO

    @property
    def task_name(self):
        return self.task.name.split(".")[-1]

    @property
    def request_id(self):
        return self.task.request.id

    def __enter__(self):
        self.logger.log(self.level, f"[{self.request_id}] start of {self.task_name}.")

    def __exit__(self, *exc):
        self.logger.log(self.level, f"[{self.request_id}] end of {self.task_name}.")


class AutologTask(app.Task):
    abstract = True

    def apply_async(self, *args, **kwargs):
        with TaskLogger(self, self.logger):
            super(app.Task, self).apply_async(*args, **kwargs)
