from .executor import MockExecutor
from .models import Intent, IntentType, WorldState


executor = MockExecutor()

state = WorldState(
    Cu_count=0,
    core_energy=20.0,
    write_health="healthy",
)

intent = Intent(
    intent_type=IntentType.harvest,
    reason="目标尚未完成且允许采集",
)

result = executor.execute(state, intent)

print("执行前状态：", state)
print("动作是否成功：", result.success)
print("执行结果说明：", result.message)
print("执行后状态：", result.state)

print("\n--- 停止意图 ---")

stop_intent = Intent(
    intent_type=IntentType.stop,
    reason="目标已经完成",
)

stop_result = executor.execute(state, stop_intent)

print("动作是否成功：", stop_result.success)
print("执行结果说明：", stop_result.message)
print("执行后状态：", stop_result.state)

print("\n--- 停止意图 ---")

stop_intent = Intent(
    intent_type=IntentType.stop,
    reason="目标已经完成",
)

stop_result = executor.execute(state, stop_intent)

print("动作是否成功：", stop_result.success)
print("执行结果说明：", stop_result.message)
print("执行后状态：", stop_result.state)

print("\n--- 写入状态异常 ---")

unhealthy_state = WorldState(
    Cu_count=0,
    core_energy=20.0,
    write_health="quarantined",
)

harvest_intent = Intent(
    intent_type=IntentType.harvest,
    reason="尝试采集",
)

unhealthy_result = executor.execute(
    unhealthy_state,
    harvest_intent,
)

print("动作是否成功：", unhealthy_result.success)
print("执行结果说明：", unhealthy_result.message)
print("执行后状态：", unhealthy_result.state)