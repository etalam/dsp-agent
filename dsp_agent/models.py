from dataclasses import dataclass
from enum import Enum

"""异常，表示游戏状态和目标中不合法数据"""
class InvalidStateError(ValueError):
    pass

"""enum,agent选择下一步意图"""
class IntentType(Enum):
    harvest="harvest"
    stop="stop"

"""数据类，agent某一时刻观察到最小世界状态"""
@dataclass(frozen=True)
class WorldState:
    Cu_count:int
    core_energy:float
    write_health:str
    def validate(self) -> None :
        if self.Cu_count<0:
            raise InvalidStateError("铜矿数不能小于0")
        if self.core_energy<0:
            raise InvalidStateError("核心能量不能小于0")
        if not self.write_health:
            raise InvalidStateError("write_health不能为空")


"""表示Agent需要的目标铜矿数量"""
@dataclass(frozen=True)
class Goal:
    target_Cu:int
    def validate(self)->None:
        if self.target_Cu<0:
            raise InvalidStateError("目标铜矿不能小于0")
    def is_satisfied_by(self,state:WorldState)->bool:
        return state.Cu_count>=self.target_Cu


"""Planner选择下一步业务的企图"""
@dataclass(frozen=True)
class Intent:
    intent_type:IntentType
    reason:str