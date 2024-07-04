from tagra.analysis import plot_community_composition
import pickle

graph_path = 'results/moons.graphml'
G = pickle.load(open(graph_path, 'rb'))
plot_community_composition(G, 'class', './community_composition.png')