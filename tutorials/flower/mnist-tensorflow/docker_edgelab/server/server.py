import flwr as fl

if __name__ == "__main__":
    # Start server
    fl.server.start_server(
        config={"num_rounds": 1},
        force_final_distributed_eval = True,
    )