from .base_agent import BaseAgent

class OrchestratorAgent(BaseAgent):
    def __init__(self):
        super().__init__("Orchestrator")

    def run(self, context):
        return {"decision": "HOLD"}
