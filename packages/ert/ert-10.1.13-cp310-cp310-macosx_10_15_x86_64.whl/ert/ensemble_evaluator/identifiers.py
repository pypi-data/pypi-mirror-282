from ert.event_type_constants import (
    EVTYPE_ENSEMBLE_CANCELLED,
    EVTYPE_ENSEMBLE_FAILED,
    EVTYPE_ENSEMBLE_STARTED,
    EVTYPE_ENSEMBLE_STOPPED,
    EVTYPE_REALIZATION_FAILURE,
    EVTYPE_REALIZATION_PENDING,
    EVTYPE_REALIZATION_RUNNING,
    EVTYPE_REALIZATION_SUCCESS,
    EVTYPE_REALIZATION_TIMEOUT,
    EVTYPE_REALIZATION_UNKNOWN,
    EVTYPE_REALIZATION_WAITING,
)

ACTIVE = "active"
CURRENT_MEMORY_USAGE = "current_memory_usage"
DATA = "data"
END_TIME = "end_time"
ERROR = "error"
ERROR_MSG = "error_msg"
ERROR_FILE = "error_file"
INDEX = "index"
JOBS = "jobs"
MAX_MEMORY_USAGE = "max_memory_usage"
METADATA = "metadata"
NAME = "name"
REALS = "reals"
START_TIME = "start_time"
STATUS = "status"
STDERR = "stderr"
STDOUT = "stdout"
STEPS = "steps"

EVTYPE_FORWARD_MODEL_START = "com.equinor.ert.forward_model_job.start"
EVTYPE_FORWARD_MODEL_RUNNING = "com.equinor.ert.forward_model_job.running"
EVTYPE_FORWARD_MODEL_SUCCESS = "com.equinor.ert.forward_model_job.success"
EVTYPE_FORWARD_MODEL_FAILURE = "com.equinor.ert.forward_model_job.failure"


EVGROUP_REALIZATION = {
    EVTYPE_REALIZATION_FAILURE,
    EVTYPE_REALIZATION_PENDING,
    EVTYPE_REALIZATION_RUNNING,
    EVTYPE_REALIZATION_SUCCESS,
    EVTYPE_REALIZATION_UNKNOWN,
    EVTYPE_REALIZATION_WAITING,
    EVTYPE_REALIZATION_TIMEOUT,
}

EVGROUP_FORWARD_MODEL = {
    EVTYPE_FORWARD_MODEL_START,
    EVTYPE_FORWARD_MODEL_RUNNING,
    EVTYPE_FORWARD_MODEL_SUCCESS,
    EVTYPE_FORWARD_MODEL_FAILURE,
}

EVGROUP_FM_ALL = EVGROUP_REALIZATION | EVGROUP_FORWARD_MODEL

EVTYPE_EE_SNAPSHOT = "com.equinor.ert.ee.snapshot"
EVTYPE_EE_SNAPSHOT_UPDATE = "com.equinor.ert.ee.snapshot_update"
EVTYPE_EE_TERMINATED = "com.equinor.ert.ee.terminated"
EVTYPE_EE_USER_CANCEL = "com.equinor.ert.ee.user_cancel"
EVTYPE_EE_USER_DONE = "com.equinor.ert.ee.user_done"


EVGROUP_ENSEMBLE = {
    EVTYPE_ENSEMBLE_STARTED,
    EVTYPE_ENSEMBLE_STOPPED,
    EVTYPE_ENSEMBLE_CANCELLED,
    EVTYPE_ENSEMBLE_FAILED,
}
