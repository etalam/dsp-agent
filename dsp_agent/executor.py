from dataclasses import replace

from .models import ActionResult, Intent, IntentType, WorldState


"""内存中模拟执行Agent意图。"""
class MockExecutor:

     harvest_energy_cost = 1.0

     def execute(self,state: WorldState,intent: Intent,) -> ActionResult:
         state.validate()

         if intent.intent_type is IntentType.stop:
             return ActionResult(
                 success=True,
                 state=state,
                 message="停止意图不改变世界状态",
             )


         if state.write_health != "healthy":
             return ActionResult(
                 success=False,
                 state=state,
                 message="写入状态异常，拒绝采集",
             )

         if state.core_energy < self.harvest_energy_cost:
             return ActionResult(
                 success=False,
                 state=state,
                 message="核心能量不足，无法完成采集",
             )

         next_state = replace(
             state,
             Cu_count=state.Cu_count + 1,
             core_energy=state.core_energy - self.harvest_energy_cost,
         )

         return ActionResult(
             success=True,
             state=next_state,
             message="模拟采集完成：铜矿 +1，能量 -1",
         )