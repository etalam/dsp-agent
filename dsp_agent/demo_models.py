from .models import Goal, Intent, IntentType, InvalidStateError, WorldState


state = WorldState(
    Cu_count=-0,
    core_energy=20.0,
    write_health="healthy"
)

state.validate()

print(state)
print("状态验证通过")

goal = Goal(target_Cu=3)
goal.validate()

print("目标：", goal)
print("当前状态是否完成目标：", goal.is_satisfied_by(state))


completed_state = WorldState(
    Cu_count=3,
    core_energy=17.0,
    write_health="healthy",
)

completed_state.validate()

print("完成后的状态：", completed_state)
print("完成后的状态是否达到目标：", goal.is_satisfied_by(completed_state))

try:
    invalid_state = WorldState(
        Cu_count=-1,
        core_energy=20.0,
        write_health="healthy",
    )

    invalid_state.validate()

except InvalidStateError as error:
    print("捕获到状态错误：", error)

intent = Intent(
    intent_type=IntentType.harvest,
    reason="铜矿目标尚未完成",
)

print("下一步意图：", intent)
print("意图类型：", intent.intent_type.value)
print("决策原因：", intent.reason)