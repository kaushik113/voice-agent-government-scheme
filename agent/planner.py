from agent.state_machine import AgentState

def plan_next_state(state, memory):
    if state == AgentState.START:
        return AgentState.COLLECT_INFO

    if state == AgentState.COLLECT_INFO:
        if memory.is_complete():
            return AgentState.VALIDATE_INFO
        return AgentState.COLLECT_INFO

    if state == AgentState.VALIDATE_INFO:
        return AgentState.CHECK_ELIGIBILITY

    if state == AgentState.CHECK_ELIGIBILITY:
        return AgentState.RECOMMEND_SCHEME

    if state == AgentState.RECOMMEND_SCHEME:
        return AgentState.END

    return AgentState.END
