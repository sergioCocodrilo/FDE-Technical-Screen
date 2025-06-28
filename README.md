# FDE-Technical-Screen
Thoughtful FDE Technical Screen

Problem description: https://thoughtfulautomation.notion.site/FDE-Technical-Screen-12af43a78fa480af8d97c2fc9478cb18

### Objective

Imagine you work in Thoughtful’s robotic automation factory, and your objective is to write a function for one of its robotic arms that will dispatch the packages to the correct stack according to their volume and mass.

### Rules

Sort the packages using the following criteria:

- A package is bulky if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
- A package is heavy when its mass is greater or equal to 20 kg.

You must dispatch the packages in the following stacks:

- STANDARD: standard packages (those that are not bulky or heavy) can be handled normally.
- SPECIAL: packages that are either heavy or bulky can't be handled automatically.
- REJECTED: packages that are both heavy and bulky are rejected.


# Implementation

It is assumed that all measurements should be positive and different from zero. Thus, if a negative linear measurement is found, it is turned into a positive one.

All inputs must be numbers, else a ValueError is going to be reported.

Test are done on the same file with pytest.


## Dependencies:
1. pytest
