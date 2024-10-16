---
title: "Adding Indicators to Strategies"
pathName: /docs/desktop/adding_indicators_to_strategies
---

When backtesting strategies, it can be useful to add the indicators you use for calculations onto the chart to make it easier to check your strategy for accuracy. Instead of doing this step manually every time you run the strategy, you can program it to automatically load the indicators for you.

## Example

To add a volume indicator to your charts, you need to insert this code snippet into the [OnStateChange()](/docs/desktop/onstatechange) section of your code for the State: State.DataLoaded.

```csharp
protected override void OnStateChange()
{
    if (State == State.DataLoaded)
    {
        AddChartIndicator(VOL());
    }
}
```

To choose which panel you want your indicator plotted on, you can use this code snippet in the State.DataLoaded state:

```csharp
VOL().Panel = 2;
AddChartIndicator(VOL());
```

To customize plot colors:

```csharp
VOL().Plots[0].Brush = Brushes.Red; // Plots the VOL with a red plot
```

To customize plot width:

```csharp
VOL().Plots[0].Width = 4; // Plots the VOL bars with a width of 4
```

To customize the plot dash style:

```csharp
VOL().Plots[0].DashStyleHelper = DashStyleHelper.Dash;
```

To customize the plot style:

```csharp
VOL().Plots[0].PlotStyle = PlotStyle.Bar;
VOL().Plots[0].AutoWidth = true;
```

To customize lines, you can do it in the same way as above.

```csharp
RSI(14, 3).Lines[0].Value = 20;
RSI(14, 3).Lines[0].Brush = Brushes.Green;
```

Remember, you need to use the [AddChartIndicator()](/docs/desktop/addchartindicator) method to add your indicator if you wish to use any of the plot or line indicator customization examples.

{% callout type="note" %}
Ensure that all indicators and customizations reflect your intended use case and double-check their applicability within your strategy.
{% /callout %}
