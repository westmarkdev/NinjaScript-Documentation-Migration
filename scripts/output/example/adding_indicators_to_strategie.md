---
title: adding_indicators_to_strategie
path: adding_indicators_to_strategies
created: Thursday, October 3rd 2024, 11:50:32 am
updated: Thursday, October 3rd 2024, 12:16:55 pm
---

## Introduction

When backtesting strategies, it can be useful to add the indicators you use for calculations onto the chart to make it easier to check your strategy for accuracy. Instead of doing this step manually every time you run the strategy, you can program it to automatically load the indicators for you.

## Example Code Snippets

### Adding a Volume Indicator

To add a volume indicator to your charts, you need to add this code snippet into the [OnStateChange](onstatechange.htm) section of your code for the State: State.DataLoaded.

```csharp
protected override void OnStateChange()
{
    if (State == State.DataLoaded)
    {
        AddChartIndicator(VOL());
    }
}
```

### Choosing an Indicator Panel

To choose which panel you want your indicator plotted on, use this code snippet in the State.DataLoaded state:

```csharp
VOL().Panel = 2;
AddChartIndicator(VOL());
```

### Customizing Plot Colors

To customize plot colors:

```csharp
VOL().Plots[0].Brush = Brushes.Red; // Plots the VOL with a red plot
```

### Customizing Plot Width

To customize plot width:

```csharp
VOL().Plots[0].Width = 4; // Plots the VOL bars with a width of 4
```

### Customizing Plot Dash Style

To customize the plot dash style:

```csharp
VOL().Plots[0].DashStyleHelper = DashStyleHelper.Dash;
```

### Customizing Plot Style

To customize the plot style:

```csharp
VOL().Plots[0].PlotStyle = PlotStyle.Bar;
VOL().Plots[0].AutoWidth = true;
```

### Customizing Lines

To customize lines, use the same approach as above:

```csharp
RSI(14, 3).Lines[0].Value = 20;
RSI(14, 3).Lines[0].Brush = Brushes.Green;
```

## Important Note

Remember, you need to use the [AddChartIndicator()](addchartindicator.htm) method to add your indicator if you wish to use any of the plot/line indicator customization examples.

{% callout type="note" %}  
This method helps streamline your strategy implementation and visual representation on charts.  
{% /callout %}
