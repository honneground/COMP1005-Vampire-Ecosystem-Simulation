from collections import Counter
from Entities import *
import matplotlib.pyplot as plt
import sys
import os

def initialization():
    for i in range(initial_no_of_human):
        creatures_list.append(Creatures("human", XMAX, YMAX, exact_or_upto_steps))
    for i in range(initial_no_of_vampire):
        creatures_list.append(Creatures("vampire",XMAX, YMAX, exact_or_upto_steps))
    for i in range(initial_no_of_food):
        ingestibles_list.append(Ingestibles("food",XMAX, YMAX))
    for i in range(initial_no_of_water):
        ingestibles_list.append(Ingestibles("water",XMAX, YMAX))
    for i in range(initial_no_of_garlic):
        ingestibles_list.append(Ingestibles("garlic",XMAX, YMAX))
    return [creatures_list,ingestibles_list]

def plotting(timestep,file_path):
    if timestep <= no_of_timesteps:
        print("\n ### TIMESTEP ",timestep, "###")
    if(plot_or_not):
        for entities in creatures_list+ingestibles_list:
            if entities.state == "remaining":
                plt.scatter(entities.position[0],entities.position[1], marker=entities.getShape(), c=entities.getColor(), s=entities.getSize())
        plt.xlim(0,XMAX)
        plt.ylim(0,YMAX)
        plt.suptitle(f"Experiment: {initial_no_of_human}-{initial_no_of_vampire}")
        plt.title(f'Steps {timestep}')
        plt.pause(1)
        if timestep == 0:
            plt.savefig(os.path.join(file_path, f"Experiment_{initial_no_of_human}-{initial_no_of_vampire}_initial.png"))
        if timestep == no_of_timesteps:
            plt.savefig(os.path.join(file_path, f"Experiment_{initial_no_of_human}-{initial_no_of_vampire}_final.png"))
        plt.clf()
        
def move(creatures_list, exact_or_upto_steps):
    log = []
    for creatures in creatures_list:
            log.append(creatures.step_change(exact_or_upto_steps))
    # print(log)
    return log

def main():
    plt.rcParams.update({'axes.spines.top':False, 'axes.spines.bottom':False,'axes.spines.left':False,'axes.spines.right':False})
    file_path = os.path.join(os.getcwd(), "Graphs")
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    [creatures_list, ingestibles_list]= initialization()
    plotting(0,file_path)
    print("Simulation initialized successfully.")
    for step in range(no_of_timesteps):
        counter = Counter(move(creatures_list, exact_or_upto_steps))
        counter.update(interaction(creatures_list, ingestibles_list))
        # print(counter)
        plotting(step+1,file_path)
        terminal_print(counter)
    pop_counter()

def interaction(creatures_list, ingestibles_list):
    handshake_log = []
    log = []
    for subject in creatures_list:
        if subject.state == "remaining":
            for objects in ingestibles_list+creatures_list:
                if objects != subject and objects.state == "remaining":
                        if (objects.classification != "vampire" and subject.classification != "vampire") or ([id(objects),id(subject)] not in handshake_log):
                            if objects.position[0] in range(subject.position[0]-4, subject.position[0]+5) and objects.position[1] in range(subject.position[1]-4, subject.position[1]+5):
                                if objects.classification != "vampire" and subject.classification != "vampire":
                                     handshake_log.append([id(subject),id(objects)])
                                log.append(subject.interact(objects))
    # print(log)
    return log

def pop_counter():
    print("\n### End of Simulation ###")
    print("|Human Population|Vampire Population|")
    print("|Initial|Finanl|Initial|Finanl|")
    hum_pop = 0
    vam_pop = 0
    for pops in creatures_list:
        if pops.state == "remaining":
            if pops.classification == "human":
                hum_pop += 1
            if pops.classification == "vampire":
                vam_pop += 1
    print(f"{initial_no_of_human},{hum_pop},{initial_no_of_vampire},{vam_pop}")
                

def terminal_print(event_counter):
    event_counter[2] = event_counter.get(2,0) + event_counter.get(3,0)
    event_counter[7] = event_counter.get(7,0) + event_counter.get(8,0) + event_counter.get(9,0)
    event_counter[8] = event_counter.get(8,0) + event_counter.get(9,0)*2
    text_map ={11:"human just ate food",12:"human just drank water",13:"human just took garlic",1:"human died in their journey for aging or hunger",
                4:"pairs of human helped each other",
                2:"human plunder from others",
                3:"human was killed by other human",
                5:"human was infected by vampire virus",
                6:"vampires was killed by human",
                7:"pairs of vampires bite each other",
                8:"vampires was killed by other vampire"}
    counter = 0
    for i in event_counter:
        if i != 0 and i!=9:
            if event_counter[i] > 0:
                print(f"{event_counter[i]} {text_map[i]}.")
                counter +=1
    # print(counter)
    if counter == 0:
        print("Nothing happend.")

initial_no_of_human = int(sys.argv[1]) if len(sys.argv) >1 else 100
initial_no_of_vampire = int(sys.argv[2]) if len(sys.argv) >2 else 10
no_of_timesteps = int(sys.argv[3]) if len(sys.argv) >3 else 50
plot_or_not = False if len(sys.argv) >4 and sys.argv[4].upper() == "N" else True #True for plot, False for not plot
exact_or_upto_steps = False if len(sys.argv) >5 and sys.argv[5].upper() == "N" else True #True for exact n steps, False for upto n steps

initial_no_of_food =  20
initial_no_of_water = 5
initial_no_of_garlic = 10

XMAX = 75
YMAX = 125

creatures_list=[]
ingestibles_list=[]

main()