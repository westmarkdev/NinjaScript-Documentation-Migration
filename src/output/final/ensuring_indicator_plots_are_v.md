---
title: "Ensuring indicator plots are valid before programmatically accessing them"
pathName: /docs/desktop/ensuring_indicator_plots_are_valid
---

When accessing NinjaScript indicators in other scripts, it is important to check if the hosted indicator's plot values are already set prior to use in the hosting script. This check ensures that proper values are always used and that irrelevant values do not throw off the script logic. This reference sample demonstrates how to run these checks in a hosting indicator by checking another hosted indicator for set plot values.

Another example for when you would want to use this is if you were trying to access the Pivots indicator, but did not have enough days loaded to properly calculate those values yet. Basing logic on the Pivots in such a scenario would yield values that are not useful and can be detrimental if not handled correctly in your code.

## Key concepts in this example

- Checking indicator plots for valid values
- Handling logic for when the indicator plots are not valid

## Attached archive contains two indicator files

- SampleEveryNBarTest is the hosting indicator
- SampleEveryNBar is the hosted indicator

{% callout type="note" %}
When hosting an indicator in an Indicator column in the Market Analyzer, you will need to manually ensure enough bars back are loaded for the indicator to calculate correctly.
{% /callout %}

## Important related documentation

- [IsValidDataPoint()](/docs/desktop/isvaliddatapoint)
- [Series](/docs/desktop/series)

## Import instructions

1. Download the file contained in this Help Guide topic to your PC desktop.
2. From the Control Center window, select the menu Tools > Import > NinjaScript.
3. Select the downloaded file.

[SampleEveryNBarTest_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleEveryNBarTest_NT8.zip)