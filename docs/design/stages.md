## Stages
The application internally uses a directed acyclic graph to represent all of the stages it goes through as well as their dependencies. This process looks very similar to many classifiers (e.g. Email spam detector, handwriting recognition)

# Overview
The application passes through stages based on the dependency graph. Each stage defines how it is reached as well as its dependencies. Result represents the result generated for the user's consumption.
When a user enters data into the input form, each of the stages is sequentially traversed. This eventually results in the user being prompted for any missing information (e.g. Region)

Each stage is individually responsible for declaring its dependencies.

# Stage
A stage is the generic representation of work-item for the application that needs to be traversed through.
The stage would usually follow these steps to generate its output:
1. Fetch the input to it.
2. Process the stage

# Stage traversal
The application uses sequential traversal on the stages graph, starting at the inputs, passing through the subsequent stages. After the final stage, the application outputs the result on the screen.

## Example
```
S = (V,E)
V = {validation,model}
E = {<validation,model>}
```
When generating stages **validation and **model**
```
model: (validation)
    validation:
        validation.input(parameters)
        update validation
output model.output()
```