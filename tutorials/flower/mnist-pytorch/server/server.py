import flwr as fl
from typing import List, Tuple, Optional
import numpy as np
import os



class SaveModelStrategy(fl.server.strategy.FedAvg):
    def aggregate_fit(
        self,
        rnd: int,
        results: List[Tuple[fl.server.client_proxy.ClientProxy, fl.common.FitRes]],
        failures: List[BaseException],
    ) -> Optional[fl.common.Weights]:
        aggregated_weights = super().aggregate_fit(rnd, results, failures)
        if aggregated_weights is not None:
            # Save aggregated_weights
            print(f"Saving round {rnd} aggregated_weights...")
            np.savez(f"round-{rnd}-weights.npz", *aggregated_weights)
        return aggregated_weights




if __name__ == "__main__":

    # Define strategy
    strategy = SaveModelStrategy(
        fraction_fit=0.5,
        fraction_eval=0.5,
        min_fit_clients=2,
        min_available_clients=2,
    )

    # Start server
    fl.server.start_server(
        config={"num_rounds": 2},
        strategy=strategy,
        force_final_distributed_eval = True,
    )
