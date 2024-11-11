---
section: guides
title: Set Up
pathName: set_up11
parent: developing_strategies
status: double_check
lg2m: true
---

Our first tutorial covered using the [Strategy Builder](strategy_builder) to create simple NinjaScript strategies or to build the framework needed for a more complex strategy.

This tutorial will cover another approach, using the NinjaScript [Editor](editor) and [New Strategy Wizard](ninjascript_wizard.md).

1. Within the NinjaTrader Control Center window select the New NinjaScript  Editor... menu item

![NSTutControlCenter](https://cdn.sanity.io/images/1hlwceal/production/8150193e4ec71f9a2bb38478c05a043e422718b4-789x233.png)

![NSTutControlCenter2](https://cdn.sanity.io/images/1hlwceal/production/48fc2ba8b3e79c7858048f1243b6795a5258f4e6-201x203.png)

2. Click the "+" tab in the lower left, and select New Strategy to open a New Strategy Wizard

![RSIwithStopAndTargetSetUp1](https://cdn.sanity.io/images/1hlwceal/production/cbebb0736cd4d31e6494e82e7590e7361c94d5f1-713x524.png)

3. Enter the information as shown below

4. Press the "Next >" button until we are at the Inputs and Parameters page

![RSIwithStopAndTargetSetUp2](https://cdn.sanity.io/images/1hlwceal/production/c4fdbaafd8ef6a12778a6d998832a01f1f2b59de-755x550.png)

## Defining Input Parameters

Below you will define your strategy's input parameters. These are any input parameters that can be changed by the user when running or backtesting a strategy. If your strategy does not require any parameters leave the "Name" fields blank.

5. Click the add button to create a User Input Parameter (See item 1 in the screenshot below)

6. Fill out the Input Parameters window and click OK to create the input parameter (See item 2 in the screenshot below)

![RSIwithStopAndTargetSetUp3](https://cdn.sanity.io/images/1hlwceal/production/5a3dc07a01f873fab1cb1a96376bb8d0b5d55dc6-756x550.png)

7. Add the inputs as per the image below

![RSIwithStopAndTargetSetUp4](https://cdn.sanity.io/images/1hlwceal/production/3b1ab9dcf45980dbe31d394741b8341c375e1515-755x550.png)

8. Press the "Generate" button to generate the code in the NinjaScript Editor.

You are now ready to continue to the [Entering Strategy Logic](entering_strategy_logic) page of this tutorial.
