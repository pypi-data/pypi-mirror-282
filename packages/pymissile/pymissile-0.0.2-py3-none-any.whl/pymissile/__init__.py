"""
Description for Package
"""
from pymissile.model import PlanarKin, PitchDyn, PlanarVehicle, PlanarMissile, PlanarMissileWithPitch, PlanarMovingTarget
from pymissile.engagement import Engagement2dim
from pymissile.guidance import Guidance2dim, PurePNG2dim, IACBPNG
from pymissile.control import ThreeLoopAP
from pymissile.util import RelKin2dim, CloseDistCond, miss_distance

__all__ = ['pymissile']