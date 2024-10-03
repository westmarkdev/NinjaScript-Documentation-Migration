---

title: condition_builder2
pathName: condition-builder
created: Thursday, October 3rd 2024, 11:27:52 am
updated: Thursday, October 3rd 2024, 12:16:54 pm
---

## Overview

The Condition Builder is a powerful feature that allows you to define complex conditions for your automated trading systems without having to know how to program.

![tog_minus](tog_minus.gif) [Understanding the Condition Builder](javascript:HMToggle('toggle','UnderstandingTheConditionBuilder','UnderstandingTheConditionBuilder_ICON'))

## Functionality

Most automated trading system code wizards provide predefined expressions, limiting your ability to customize. The NinjaTrader Condition Builder allows for the development of advanced expressions without such limitations. It is crucial to understand its capabilities due to its power and flexibility.

The Condition Builder also serves as an aid for those learning NinjaScript or programming. You can build your conditions within the Condition Builder and instantly see the generated NinjaScript code by having the [NinjaScript Editor](editor.htm) open.

### Accessing Condition Builder

The Condition Builder can be accessed via the [Conditions and Actions](builder_screens.htm) screen in the NinjaTrader Strategy Builder.

## Basic Operation

The Condition Builder's primary purpose is to generate Boolean expressions (conditional expressions) that evaluate to TRUE or FALSE. For example, the expression:

```
2 < 7 (2 is less than 7)
```

is considered a Boolean expression resulting in TRUE. In NinjaTrader, boolean expressions or "Conditions" determine when to take specific actions, such as submitting an order or drawing on a chart.

## Visualization

The Condition Builder interface is set up like a Boolean expression. You select an item from the left window, compare it with a selected item from the right window, and then choose a relational operator.

1. Available items for comparison
2. List of relational operators applicable to your selected items

![Strategy_Builder_CB1](Path/to/image)

## Price Data Comparisons

You can compare a bar's price data, such as checking for a higher close. The following is an example:

1. Expand the Price category on the left side and select Close.
2. Expand the Price category on the right side and select Close.
3. Choose the greater relational operator.
4. Set the Bars ago parameter to "1".

![Strategy_Builder_CB2](Path/to/image)

Once the OK button is pressed, the created condition translates to:

"Current closing price is greater than the closing price of 1 bar ago."

## Offsetting an Item Value

You can offset the value of most items available in the Condition Builder. Offsets can be added, subtracted, multiplied, or divided from the item's actual value. Offset types include:

| Type       | Description                                                                 |
|------------|-----------------------------------------------------------------------------|
| Arithmetic | Offsets by an arithmetic equation (e.g., +, -, *, /).                     |
| Pips       | Offsets by a specified amount of pips.                                     |
| Percent    | Offsets a percentage of the item's value.                                   |
| Ticks      | Offsets by a specified amount of ticks.                                     |

Once the Offset type is selected, you must set the Offset value. Here’s an example:

1. Expand the Price category and select Close.
2. Expand the Price category and select High.
3. Choose the greater relational operator.
4. Set the Bars ago parameter to "1".
5. Set Offset type to Ticks.
6. Set Offset to "1".

![Strategy_Builder_CB3](Path/to/image)

The created condition translates to:

"Current closing price is greater than the high price of 1 bar ago + 1 tick."

## Indicator to Value Comparisons

You can compare an indicator's value to a numeric value. This is useful for various conditions (e.g., ADX compared to a value). Here's an example:

1. Expand the Indicator category and select the ADX indicator.
2. Set the parameters of the indicator.
3. Expand the Misc category and select Numeric value.
4. Choose the greater relational operator.
5. Enter the numeric value to compare (e.g., 30).

![Strategy_Builder_CB4](Path/to/image)

The condition translates to:

"Current value of a 14 period ADX is greater than 30."

## Additional Comparisons

### Comparing Plot Values of Multi-Plot Indicators

You can compare plots within the same indicator. Example steps would include selecting specific plots for comparison.

![Strategy_Builder_CB5](Path/to/image)

### User Inputs & Variables

User inputs allow for increased flexibility in your strategy by using variables instead of fixed values.

![Strategy_Builder_CB6](Path/to/image)

### Cross Over Conditions

Define conditions for either CrossAbove or CrossBelow using a defined look-back period. Example:

![Strategy_Builder_CB9](Path/to/image)

### Checking for Volume Expansion

Compare the current bar's volume against the previous bar's volume plus an offset.

![Strategy_Builder_CB13](Path/to/image)

### Creating Market Position Comparisons

Assess market position states, such as a strategy being flat.

![Strategy_Builder_CB14](Path/to/image)

### Creating Time Comparisons

Compare bar's time data against user-defined values.

![Strategy_Builder_CB15](Path/to/image)

### Negating a Condition

Negate conditions to enable certain filters or evaluations.

![Strategy_Builder_CB16](Path/to/image)

Once the OK button is pressed, the final condition translates to:

"The DEMA(14) indicator has not been crossed by the Close price within the last 10 bars."

## Conclusion

This guide provides an overview of the Condition Builder's functionalities and various comparisons you can make. By leveraging this powerful tool, you can enhance your automated trading strategies effectively.
