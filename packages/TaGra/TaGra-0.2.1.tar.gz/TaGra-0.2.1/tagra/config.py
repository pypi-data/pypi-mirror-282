import json
import os

default_config = {
    "output_directory": "results/", 
    "preprocessed_filename": None,
    "graph_filename": None,
    "numeric_columns": [],
    "categorical_columns": [],
    "target_columns": None,
    "ignore_columns": [],
    "unknown_column_action": "infer",
    "numeric_threshold": 0.05,
    "numeric_scaling": "standard",
    "categorical_encoding": "one-hot",
    "nan_action": "infer",
    "nan_threshold": 0,
    "verbose": True,
    "manifold_method": None,
    "manifold_dimension": None,
    "method": "knn",
    "k": 5,
    "distance_threshold": 0.75,
    "similarity_threshold": 0.95,
    "clustering_method": "hierarchical",
    "inconsistency_threshold": 0.1,
    "neigh_prob_path": "neigh_prob.txt",
    "degree_distribution_filename": "degree.png",
    "betweenness_distribution_filename": "betweeness.png",
    "community_composition_filename": "communities.png",
    "graph_visualization_filename": "graph.png",
    "prob_heatmap_filename": "neigh_prob_heatmap.png",
    "overwrite": False
}

def load_config(config_path="config.json"):
    
    if type(config_path) is str:
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = json.load(f)
            if config.get("verbose", None) is None:
                config['verbose'] = default_config['verbose']
                print(f"Using default value for 'verbose': {default_config['verbose']}")
            for key in default_config:
                if key not in config:
                    config[key] = default_config[key]
                    if config['verbose']:
                        print(f"Using default value for {key}: {default_config[key]}")
            if config["verbose"]:
                print(f"Loaded configuration from {config_path}.")
            return config
    else:
        config = default_config
        if config["verbose"]:
            print("Using default configuration.")
    return config

def save_config(config, config_path="config.json"):
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)
    if config["verbose"]:
        print(f"Configuration saved to {config_path}.")
