# intersection experiments

# Setup

[SUMO_setup.md](SUMO_setup.md) introduces how we set up the SUMO programs.

# 1st Experiments - repeat real world

Our first experiment just repeat and simualte the traffic flow in real world using our collected records. This traffic flow includes vehicles and pedestrians. 

The basic traffic lights information has been introduced in [../raw_data/README.md](../raw_data/README.md)

To run it, just run
```python
intersection_experiments$ python3 first_experiment.py > output/1stexperiment.runlog.timestamp.md
```

# 2nd Experiments - dynamic traffic lights 

Based on the first experiment, we changed the traffic lights control system to be dynamic. It changes the duration of green lights according to how many vehicles there are for each green light session (every two phases).

```
Duration of green light = MAX{ 
    # go straight vehicles / 4 lanes * avg 4 seconds per vehicle 
    + # turn left vehicles of opposite direction * avg 4 seconds per vehicle, 
    
    # go straight vehicles of opposite direction / 4 lanes * avg 4 seconds per vehicle 
    + # turn left vehicles * avg 4 seconds per vehicle
    }
```

This experiment will be the baseline. This experiment can be thought as having lowest vehicle waiting time.


To run it, just run
```python
intersection_experiments$ python3 second_experiment.py > output/2ndexperiment.runlog.timestamp.md
```

# 3rd Experiemnts - dynamic traffic lights with our pedestrians road-crossing simulator

Based on second one, take pedestrians road-crossing needed time into condiseration. 

```
Duration = Max  {
    Duration of green light of second experiment,

    pedestrians road-crossing needed time
}
```


To run it, just run
```python
intersection_experiments$ python3 third_experiment.py > output/3rdexperiment.runlog.timestamp.md
```

# Results 

See paper


