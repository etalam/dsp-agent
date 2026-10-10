from .agent import Agent
from .executor import MockExecutor
from .models import Goal, WorldState
from .planner import RulePlanner

planner = RulePlanner()
executor = MockExecutor()
agent = Agent(planner, executor)

initial_state = WorldState(
    Cu_count=0,
    core_energy=20.0,
    write_health="healthy",
)

goal = Goal(target_Cu=3)

result = agent.run(initial_state, goal)

print("\n--- Agent运行结果 ---")
print("是否完成目标：", result.completed)
print("最终状态：", result.final_state)
print("执行动作数：", result.actions_taken)
print("停止原因：", result.stop_reason)