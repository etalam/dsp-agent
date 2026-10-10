from .executor import MockExecutor
from .models import Goal, IntentType, RunResult, WorldState
from .planner import RulePlanner


"""运行时同步观察、规划和执行循环。"""
class Agent:

    def __init__(self, planner: RulePlanner, executor: MockExecutor) -> None:
        self.planner = planner
        self.executor = executor

    def run(self, initial_state: WorldState, goal: Goal, max_actions: int = 10) -> RunResult:
        initial_state.validate()
        goal.validate()

        if max_actions <= 0:
            raise ValueError("max_actions必须大于0")

        state = initial_state
        actions_taken = 0

        while actions_taken < max_actions:
            print(
                f"观察：铜矿={state.Cu_count}，"
                f"能量={state.core_energy}，"
                f"写入状态={state.write_health}"
            )

            intent = self.planner.plan(state, goal)

            print(
                f"规划：{intent.intent_type.value}；"
                f"原因：{intent.reason}"
            )

            if intent.intent_type is IntentType.stop:
                return RunResult(
                    completed=goal.is_satisfied_by(state),
                    final_state=state,
                    actions_taken=actions_taken,
                    stop_reason=intent.reason
                )

            action_result = self.executor.execute(state, intent)
            print("执行：", action_result.message)

            if not action_result.success:
                return RunResult(
                    completed=False,
                    final_state=state,
                    actions_taken=actions_taken,
                    stop_reason=action_result.message
                )

            state = action_result.state
            actions_taken += 1

        completed = goal.is_satisfied_by(state)

        if completed:
            stop_reason = "铜矿目标已经完成"
        else:
            stop_reason = "达到最大动作数限制"

        return RunResult(
            completed=completed,
            final_state=state,
            actions_taken=actions_taken,
            stop_reason=stop_reason
        )