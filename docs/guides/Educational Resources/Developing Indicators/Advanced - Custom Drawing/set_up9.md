---
section: guides
title: Set Up
pathName: set_up9
parent: advanced_custom_drawing
status: double_check
lg2m: true
---

The first step in creating a custom indicator is to use the custom indicator wizard. The wizard will generate the required **NinjaScript** code that will serve as the foundation for your custom indicator.

1. Within the **NinjaTrader** [Control Center](control_center), select the New menu, then select the **NinjaScript Editor** menu item.

2. Right mouse click the "Indicators" folder in the **NinjaScript Explorer** section, then select the New Indicator menu item to open the New Indicator Wizard.

## Defining Indicator Properties and Name  

First you will define your indicator's name and several indicator properties. Begin by clicking the Next > button on the first page of the wizard to view the page shown below.

![NSTuts1](nstuts1.png)

3. Enter the information as shown above.

4. Click the Next > button.

## Setting Default Properties

The next page will allow you to set defaults for basic properties related to your indicator, including its **Calculate** and **Overlay** settings. Click the More Properties button to expose additional properties. For this tutorial, we will not change any basic properties' defaults, and instead will leave them all set to the values shown below:

![NSTutorialSetUpNoOverlayOnPrice](https://cdn.sanity.io/images/1hlwceal/production/1e993316eb5a0832cf5e6c12f15dcdb9734b34e6-615x550.png)

## Adding Additional Data

The next page will allow you to configure one or more additional **Bars** objects for use by the indicator. For our purposes, we will leave this page blank and move forward by clicking the Next > button.

![NSTutAdditionalDataBlank](https://cdn.sanity.io/images/1hlwceal/production/f38e15eb56590f779e9d6fb7538004dc41f8327e-615x550.png)

## Adding Event Methods

The next page will allow you to pre-populate certain event methods into the **NinjaScript** code generated by the wizard. For our purposes, we will leave all of the checkboxes corresponding to different event methods unchecked, and will move on by clicking the Next > button.

![NSTutAdditionalEventMethodsBlank](https://cdn.sanity.io/images/1hlwceal/production/0912948f7f3cb5158d298a14feb8607b0e8a4bb3-615x550.png)

## Defining Input Parameters

The next page will allow us to configure user input parameters for the indicator. For our custom **CCI** indicator, we will create a single input parameter which can be changed by users in the Indicators window when applying or editing the indicator. This input parameter will determine the **CCI**'s period. We will select **int** as the Type, since integers are the most efficient native data types to be used for positive whole numbers, like those used to specify a number of bars to look back (a period). We will enter a "Default" value of "14" for the period, and a "Min" value of 1, to ensure that users do not enter zero or lower.

![NSTuts5](https://cdn.sanity.io/images/1hlwceal/production/feacf0a3fc33941e938f45a35f899513088b6614-726x468.png)

1. Clicking the add button on the "Input Parameters" page brings up the Input Parameters dialogue.

2. The Input Parameters dialogue can be used to define user inputs.

## Defining Plots and Lines

The next page will allow us to define plots and static lines for the indicator. For the **CCI**, we will define a single plot, called "CCI," and define five lines to draw in the indicator panel. For each item, first click the add button, then use the Plots and Lines dialogue to configure each item as seen below.

![NSTuts6](https://cdn.sanity.io/images/1hlwceal/production/2c86a08f78f0fb6846506a9aa8077d5af6b79ccf-621x454.png)

1. The add button will allow you to configure plots and lines for the indicator.

After this, click the Finish button, and the Indicator Wizard will generate a basic code structure implementing the parameters that you have set. You are now ready to move on to [entering calculation logic](entering_calculation_logic6).
