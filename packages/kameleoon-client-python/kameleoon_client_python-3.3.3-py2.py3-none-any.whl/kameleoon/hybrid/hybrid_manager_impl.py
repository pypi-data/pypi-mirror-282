import time
from typing import Dict, Optional
from kameleoon.data.manager.assigned_variation import AssignedVariation
from kameleoon.hybrid.hybrid_manager import HybridManager


class HybridManagerImpl(HybridManager):
    TC_INIT = "window.kameleoonQueue=window.kameleoonQueue||[];"
    TC_ASSIGN_VARIATION_F = "window.kameleoonQueue.push(['Experiments.assignVariation',{0},{1}]);"
    TC_TRIGGER_F = "window.kameleoonQueue.push(['Experiments.trigger',{0},true]);"
    TC_ASSIGN_VARIATION_TRIGGER_F = TC_ASSIGN_VARIATION_F + TC_TRIGGER_F

    def __init__(self, expiration_period: float) -> None:
        super().__init__()
        self._expiration_period = expiration_period

    def get_engine_tracking_code(self, visitor_variations: Optional[Dict[int, AssignedVariation]]) -> str:
        lines = [self.TC_INIT]
        if visitor_variations:
            expiration_time = time.time() - self._expiration_period
            for variation in visitor_variations.values():
                if variation.assignment_time > expiration_time:
                    line = self.TC_ASSIGN_VARIATION_TRIGGER_F.format(variation.experiment_id, variation.variation_id)
                    lines.append(line)
        return "".join(lines)
