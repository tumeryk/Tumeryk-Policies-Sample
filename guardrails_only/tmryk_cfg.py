from nemoguardrails.actions import action
from prometheus_registry import VIOLATION

@action()
def record_violation():
    VIOLATION.inc(1)
    print("Violation recorded")
    return 0
