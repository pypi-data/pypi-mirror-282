import os

ROOT_DIR = "/tmp/"
WORK_DIR = "/opt/dlami/nvme/"

# Prod / Dev 상태를 정의합니다.
ENV = os.environ["ENV"]


MODEL_MAP = {
    # 아무것도 하지 않고 일정시간 대기 후 입력을 그대로 전달
    "SleepAndPassProcessor": {},
    # Denoise model
    "DPIRProcessor": {
        "model_name": str(os.environ["DPIR_MODEL_NAME"]),
        "alias": str(os.environ["DPIR_MODEL_ALIAS"]),
        # "model_dir": "/tmp/DPIR",
    },
    "DRURBPNSRF3Processor": {
        "model_name": str(os.environ["DRU_RBPN_SR_F3_MODEL_NAME"]),
        "alias": str(os.environ["DRU_RBPN_SR_F3_MODEL_ALIAS"]),
        # "model_dir": "/tmp/DRU-RBPN-SR-F3",
    },
    "DRUASMSRF3Processor": {
        "model_name": str(os.environ["DRU_ASM_SR_F3_MODEL_NAME"]),
        "alias": str(os.environ["DRU_ASM_SR_F3_MODEL_ALIAS"]),
        # "model_dir": "/tmp/DRU-RBPN-SR-F3",
    },
    "DRURBPNSRF5Processor": {
        "model_name": str(os.environ["DRU_RBPN_SR_F5_MODEL_NAME"]),
        "alias": str(os.environ["DRU_RBPN_SR_F5_MODEL_ALIAS"]),
        # "model_dir": "/tmp/DRU-RBPN-SR-F5",
    },
}

# RayEncoder의 resource 사용량을 정의합니다.
RAY_ENCODER_ACTOR_OPTIONS = {
    "num_gpus": int(os.environ["WORKER_NUM_GPUS"]),
    "resources": {
        "WORKER": 1,
    },
}
