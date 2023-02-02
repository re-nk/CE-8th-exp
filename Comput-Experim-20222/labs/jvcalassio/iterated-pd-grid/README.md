# Iterated spatial prisoner's dilemma model

This model is an adaptation of [MESA's spatial prisoner's dilemma model](https://github.com/projectmesa/mesa/tree/v0.9.0/examples). The demographic variation of the classic prisoner's dilemma consists of multiple agents that interact with it's neighbors and choose to either cooperate or defect. The strategy adopted by these agents is based on the stategy taken by the neighbor with the highest score.

It demonstrates how the widespread cooperation emerges by such simple rules.

### Changes from original model

This version changes the original model in order to enable the manipulation of some variables. Specifically, the **ratio between cooperating and defecting agents** in the beginning of the simulation, and the **defection bonus** payoff to defecting agents. It's been also added a graph to track how many cooperating/defecting agents exists at any given time in the simulation, in order to better quantify the resulting choices of those agents.

With this changes, it's possible to verify how the independent variables interfere with the results of the simulation.

The payoff matrix is the same as the one present in the original model and is represented in the table below. The only difference is that *D* is now a dynamic value, settable in the interface.

The payoff matrix used by the model is defined as below

|               | Cooperate | Defect|
|:-------------:|:---------:|:-----:|
| **Cooperate** | 1, 1      | 0, D  |
| **Defect**    | D, 0      | 0, 0  |

Where *D* is the defection award.

### Causal hyphotesis studied

This adapted model was built in order to study if **the increase in the number of cooperating agents reflects in higher scores for cooperating agents**. In other words, in the long term cooperation generates more value to system than defection. The more cooperating agents you have, more value will be generated for the system overall.

### How to run it

You'll need Python 3.8 and pip in order to setup and run the simulation. 

There are two modes of operation: web UI and batch runner. For both of them, you'll need to setup the environment:

1. Clone the repository

```
git clone git@github.com:jvcalassio/iterated-pd-grid.git
```

2. Get into the folder and install the requirements

```
cd iterated-pd-grid && pip3 install -r requirements.txt
```

#### Web UI

To execute the web UI, follow the steps below:


3. Run the simulation;

```
python3 main.py
```

4. Access the simulation at `http://127.0.0.1:8521`;

5. You can then set the parameters as you want, and click the "Start" button at the top right corner of the page navigation bar.

#### Batch runner

To execute the batch runner, follow the steps below:

3. Set the parameters of your simulation inside the `params` object in the `batch_runner.py` file;

4. Run the batch runner;

```
python3 batch_runner.py
```

5. The results of the simulation will be outputed to a CSV file at the `results` folder.

### Parameters description

- **Scheduler type**: defines how the simulation will progress it's steps. The available options are
  - Sequential: The agents are going to be updated one are a time, sequentially from the top left corner of the grid. The actions taken by a specific agent in the current round ("round" as a single step in the model until all of the cells are updated) will affect neighboring agents.
  - Random: A random agent is chosen to take an action (without replacement), and it will be done until all the agents take an action in the current round. As it's done in the "sequential" type, the actions from agents in the current round influence actions from other agents.
  - Simultaneous: All the agents will choose their movement based on the current state of the grid, and then all of them are going to update simultenously. This way, the actions taken by a specific agent will only affect the next round from it's neighbors.
- **Initial coopearation (%)**: defines the percentage of cooperating agents in the initial grid. Default value is 50%.
- **Defection award**: defines the award for the agent that chooses to defect interacting with an agent that chose to cooperate. Default value is 1.6, and the range goes from 0 to 10.