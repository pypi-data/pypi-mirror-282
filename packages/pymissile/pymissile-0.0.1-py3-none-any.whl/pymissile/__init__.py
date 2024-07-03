"""
Description for Package
"""
from model import PlanarKin, PitchDyn, PlanarVehicle, PlanarMissile, PlanarMissileWithPitch, PlanarMovingTarget
from engagement import Engagement2dim
from guidance import Guidance2dim, PurePNG2dim, IACBPNG
from control import ThreeLoopAP
from util import RelKin2dim, CloseDistCond, miss_distance

__all__ = ['pymissile']