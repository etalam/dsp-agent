from .models import Goal,Intent,IntentType,WorldState


"""根据世界状态和目标选择下一步意图"""
class RulePlanner:
    min_harvest_energy=5.0
    def plan(self, state: WorldState, goal: Goal) -> Intent:
        state.validate()
        goal.validate()

        if state.write_health != "healthy":
            return Intent(
                intent_type=IntentType.stop,
                reason="写入状态异常",
            )

        if goal.is_satisfied_by(state):
            return Intent(
                intent_type=IntentType.stop,
                reason="铜矿目标已经完成",
            )

        if state.core_energy < self.min_harvest_energy:
            return Intent(
                intent_type=IntentType.stop,
                reason="核心能量不足",
            )

        return Intent(
            intent_type=IntentType.harvest,
            reason="目标未完成且当前状态允许采集",
        )