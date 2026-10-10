from .models import Goal, WorldState
from .planner import RulePlanner


planner = RulePlanner()

state = WorldState(
    Cu_count=0,
    core_energy=20.0,
    write_health="healthy",
)

goal = Goal(target_Cu=3)

intent = planner.plan(state, goal)

print("当前状态：", state)
print("当前目标：", goal)
print("Planner决定：", intent.intent_type.value)
print("决定原因：", intent.reason)

print("\n--- 目标已经完成 ---")

completed_state = WorldState(
    Cu_count=3,
    core_energy=20.0,
    write_health="healthy",
)

completed_intent = planner.plan(completed_state, goal)

print("Planner决定：", completed_intent.intent_type.value)
print("决定原因：", completed_intent.reason)


print("\n--- 核心能量不足 ---")

low_energy_state = WorldState(
    Cu_count=0,
    core_energy=4.0,
    write_health="healthy",
)

low_energy_intent = planner.plan(low_energy_state, goal)

print("Planner决定：", low_energy_intent.intent_type.value)
print("决定原因：", low_energy_intent.reason)


print("\n--- 写入状态异常 ---")

unhealthy_state = WorldState(
    Cu_count=0,
    core_energy=20.0,
    write_health="quarantined",
)

unhealthy_intent = planner.plan(unhealthy_state, goal)

print("Planner决定：", unhealthy_intent.intent_type.value)
print("决定原因：", unhealthy_intent.reason)