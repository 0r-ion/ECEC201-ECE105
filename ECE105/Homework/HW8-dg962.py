# -*- coding: utf-8 -*-
"""
Graph-based simulation of spread of an infectious disease in a town against a vaccination campaign. 

Author: Naga Kandasamy
Date created: February 11. 2021
Date modified: May 23, 2023

Student name: Daniel Goulding
Date modified: 14511512

"""
import math
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import sys

def draw_graph(G, pos):
    """Draw the NetworkX graph along with node placement and a color map.
        Red: infected individuals
        Green: vaccinated individuals
        Yellow: unvaccinated healthy individuals
    """
    color_map = []
    for i in range(0, G.number_of_nodes()):
        if G.nodes[i]['infected'] == True:
            color_map.append('red')
            
        elif G.nodes[i]['infected'] == False and G.nodes[i]['vaccinated'] == True:
            color_map.append('green')
            
        else: 
            color_map.append('yellow')
    
    nx.draw(G, pos, node_color = color_map, with_labels = True)
    plt.show()

def print_nodes(G):
    """Print the dictionaries maintained by nodes in the graph"""
    for i in range(0, G.number_of_nodes()):
        print(G.nodes[i])

def initialize_graph(G, frac):  
    
    """Initialize nodes in graph"""
    for i in range(0, G.number_of_nodes()):
        G.nodes[i]['vaccinated'] = False                # Person is not vaccinated 
        G.nodes[i]['infected'] = False                  # Person is not infected
    
    num_v = math.ceil(G.number_of_nodes() * frac)       # Number of people who are vaccinated
    population = list(G.nodes)
    """Select at random from the overall population, a list, of size num_v, of people who are vaccinated."""
    vaccinated = np.random.choice(population, num_v, False)
    for i in vaccinated:
        G.nodes[i]['vaccinated'] = True
        
    """Select patient zero, that is, the first infected person"""
    un_vaccinated = []
    for i in range(0, G.number_of_nodes()):
        if G.nodes[i]['vaccinated'] == False:
            un_vaccinated.append(i)
    
    p_z = np.random.choice(un_vaccinated, 1, False)
    G.nodes[p_z[0]]['infected'] = True
    
    
def simulate(G, threshold, steps):
    # print(G)
    # print(threshold)
    # print(steps)
    """
    Simulation of graph dynamics for a number of steps.
    
    Simulation rules:
    
    For person P, from 1 to N:
        if P is already infected in the current time step (t):
            P will remain infected in the next time step (t+1)
		else (person P is healthy):
		   Find how many neighbors of person P are infected.
		   If number of infected neighbors >= threshold of person P:
				P becomes infected at the next time step (t+1).
			else
                P will remain healthy in the next time step.		
			end
		end
    """
    
    stats = [0] * steps                                      # Data structure to store statistics for each run
    
    t = 0                                           
    while t < steps:
        # FIXME: Simulate graph dynamics using the provided rules
        for i in range(0, G.number_of_nodes()):
            if G.nodes[i]['infected'] == False:
                infected_ns = sum([1 for n in G.adj[i] if G.nodes[n]['infected']])
                if G.nodes[i]['vaccinated'] == True:
                    if infected_ns >= threshold:
                        G.nodes[i]['infected'] == True
                        print("one")
                        stats[t] += 1
                elif infected_ns >= 1:
                    G.nodes[i]['infected'] == True
                    stats[t] += 1
                    print("one")
        t += 1
        print(stats)
        # FIXME: Update the infected status
        
        # FIXME: Calculate the infection rate for time step t and store statistics 
    return stats

def column_sum(lst):
    arr = np.array(lst)
    return (arr, 0).tolist()

def run(nodes, edges, frac, threshold, steps, runs):
    """nodes:       number of nodes in graph
       edges:       number of edges in graph
       frac:        number between 0 and 1 indicating the fraction of the population vaccinated
       threshold:   number of infected neighbors needed to infect a healthy individual
       steps:       time steps to simulate the graph dynamics
       runs:        number of simulation runs
       """
       
    """Run simulations using the Erdos-Renyi graph"""
    nr = 0                                                      # Initialize number of runs
    BAmasterstats = list()
    ERmasterstats = list()
    while nr < runs:    
        G = nx.gnm_random_graph(nodes, edges)                   # Generate the Erdos-Renyi graph 
        initialize_graph(G, frac)                               # Initialize graph
        
        """
        Position nodes in graph for visualization purposes and draw graph.
        Uncomment code if you wish to visualize small graphs.
        
        pos = nx.spring_layout(G)                               
        draw_graph(G, pos)
        """
        stats = simulate(G, threshold, steps)                   # Simulate graph
        # FIXME: store stats for the simulation run
        # print(stats)
        ERmasterstats.append(stats)
        # print(ERmasterstats)
        nr += 1
         
    # FIXME: calculate average infections for each time step, over all the simulation runs, for the ER graph model
    ERpercent_inf_per_turn = [sum(i)/runs for i in zip(*ERmasterstats)]
    # for i in range(len(ERpercent_inf_per_turn)):
    #     ERpercent_inf_per_turn[i] = ERpercent_inf_per_turn[i] / len(ERmasterstats[0])
    # ERpercent_inf_per_turn = [o for o in range(len(ERmasterstats[0]))]

    """Run simulations using the Barabasi-Albert graph"""
    nr = 0                                                      # Initialize number of runs
    while nr < runs:
        to_attach = edges // nodes                              # Number of edges to attach from a new node to existing nodes
        G = nx.barabasi_albert_graph(nodes, to_attach)          # Generate the Barabasi-Albert graph 
        initialize_graph(G, frac)                               # Initialize graph
        """
        pos = nx.spring_layout(G)                               
        draw_graph(G, pos)
        """
        stats = simulate(G, threshold, steps)                   # Simulate graph
        # FIXME: store stats for the simulation run
        BAmasterstats.append(stats)
        nr += 1
         
    # FIXME: Calculate average infections for each time step, over all the simulation runs, for the BA graph model
    BApercent_inf_per_turn = [sum(i)/runs for i in zip(*BAmasterstats)]
    # for i in range(len(ERpercent_inf_per_turn)):
    #     ERpercent_inf_per_turn[i] = ERpercent_inf_per_turn[i] / runs
    # FIXME: Plot results from the ER and BA models and save as PDF file 



    plt.figure()
    erplt = plt.subplot(121) 
    baplt = plt.subplot(122) 
    erplt.plot(list(range(int(runs/2))), column_sum(ERmasterstats))
    baplt.plot(list(range(int(runs/2))), column_sum(BAmasterstats))
    plt.savefig('HW8-figure')

# Main program
if __name__ == '__main__':
    
    if len(sys.argv) < 7:
        print('Usage: {} nodes edges frac thresh steps runs'.format(sys.argv[0]))
        print('nodes: number of nodes in graph')
        print('edges: number of edges in graph')
        print('frac: fraction of population that is vaccinated')
        print('thresh: number of infected neighbors needed to infect a healthy individual')
        print('steps: number of time steps to simulate')
        print('runs: number of simulation runs')
    else:
        nodes = int(sys.argv[1])
        edges = int(sys.argv[2])
        frac = float(sys.argv[3])
        thresh = int(sys.argv[4])
        steps = int(sys.argv[5])
        runs = int(sys.argv[6])
        
        # Run simulator 
        run(nodes, edges, frac, thresh, steps, runs)
        
        
        