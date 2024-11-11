---
title: Removing and Custom Formatting an Indicator’s Chart Label
pathName: removing_and_custom_formatting_an_indicators_chart_label
parent: reference_samples
section: guides
status: imported
---

## Removing and Custom Formatting an Indicator’s Chart Label

If you create a **NinjaScript** indicator or strategy with many customizable parameters, you will have a long label when you load the **NinjaScript** onto your chart. This may be visually cumbersome so you may want to trim the displayed label to a more manageable size that only contains the most important parameters.

### Key concepts in this example

* Creating a custom string for the label of the **NinjaScript** item.

### Important related documentation

* [Draw.TextFixed()](draw_textfixed)
* [Draw.Text()](draw_text)
* [Override DisplayName()](indicator_displayname)

{% callout type="note" %}

Tip: When adding an indicator onto a chart you can also completely remove any labeling on the chart of the indicator name. You can do this by clearing the "Label" field under the "General" category when you add the indicator onto the chart.
{% /callout %}

### Import instructions

1. Download the file contained in this Help Guide topic to your PC desktop.
2. From the Control Center window, select the menu Tools > Import > NinjaScript.
3. Select the downloaded file.

[SampleDisplayName_NT8.zip](samples/SampleDisplayName_NT8.zip)
