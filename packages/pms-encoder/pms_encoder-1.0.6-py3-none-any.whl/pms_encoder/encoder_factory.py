import uvloop
import cv2
import asyncio
import ray

import os

from loguru import logger
from .encoder._video_encoder import VideoEncoder
from .encoder._image_encoder import ImageEncoder
from pms_inference_engine import SleepAndPassProcessor, register, EngineIOData, Engine, EngineIOData, is_wrapped_ray, get_local_processor_type
from ._config import *

@register
class RzSleepAndPassProcessor(SleepAndPassProcessor):
    def __init__(self, concurrency: int, index: int, scale:float, sleep_time: float = 0.1) -> None:
        super().__init__(concurrency, index, sleep_time)
        self.scale = scale
        
    async def _run(self, input_data: EngineIOData) -> EngineIOData:
        await asyncio.sleep(self._sleep_time)
        frame = input_data.frame
        h, w, c = frame.shape
        resize_width = int(w*self.scale)
        resize_height = int(h*self.scale)
        frame_rz = cv2.resize(frame[:,:,:3], (resize_width, resize_height))
        return EngineIOData(input_data.frame_id, frame_rz)


class EncoderFactory:
    @staticmethod
    def create_encoder(
        redis_data: dict,
        number_of_processors: int,
        processor_kwargs: dict,
    ):
        processor_type_map = {
            "M001": "Ray_DPIRProcessor",
            "M002": "Ray_DRURBPNSRF3Processor",
            "M003": "Ray_DRURBPNSRF5Processor"
        }
        processor_type = processor_type_map.get(redis_data.get("model"), "Ray_SleepAndPassProcessor")

        if redis_data.get("contentType") == "image":
            logger.debug("image encoder")
            return ImageEncoder(
                processor_type=processor_type,  # processor_key,
                number_of_processors=number_of_processors,
                processor_kwargs=processor_kwargs
            )
        else:
            logger.debug("video encoder")
            return VideoEncoder(
                processor_type=processor_type,  # processor_key,
                number_of_processors=number_of_processors,
                processor_kwargs=processor_kwargs
            )
        
        logger.debug("encoder init end")
    

@ray.remote(**RAY_ENCODER_ACTOR_OPTIONS)
class RayEncoderFactory:
    def __init__(
        self, 
        redis_data: dict,
        number_of_processors: int,
        processor_type: str,
        processor_kwargs: dict,
    ) -> None:
        import pms_model_manager as mml
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        model_manager = mml.ModelManager(ROOT_DIR)
        model_key = (
            get_local_processor_type(processor_type)
            if is_wrapped_ray(processor_type)
            else processor_type
        )
        
        logger.debug(f"Processor kwargs : {processor_kwargs}")
        if redis_data["contentType"] == "video":
            self.encoder = VideoEncoder(
                processor_type=processor_type,  # processor_key,
                number_of_processors=number_of_processors,
                processor_kwargs=processor_kwargs
            )
        else:
            self.encoder = ImageEncoder(
                processor_type=processor_type,  # processor_key,
                number_of_processors=number_of_processors,
                processor_kwargs=processor_kwargs
            )
            
    async def run(self, *args, **kwrags) -> None:
        encoder = self.encoder
        await encoder(*args, **kwrags)
