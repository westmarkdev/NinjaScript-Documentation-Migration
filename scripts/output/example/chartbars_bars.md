---

title: chartbars_bars
pathName: bars
created: Thursday, October 3rd 2024, 10:27:03 am
updated: Thursday, October 3rd 2024, 12:14:34 pm
---

## Definition

Represents the data returned from the historical data repository in relation to the primary [ChartBars](chartbars.htm) object configured on the chart. See also [Bars](bars.htm).

## Property Value

A [Bars](bars.htm) object.

## Syntax

`ChartBars.Bars`

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   if(ChartBars != null && ChartBars.Bars != null)
   {
     Print("The configured bars period type represented on the chart is " + ChartBars.Bars.BarsPeriod.BarsPeriodType);
   }
}
```

{% callout type="note" %}  
For more detailed information, refer to the [Click to Display Table of Contents](NT HelpGuide English.html?chartbars_bars.htm).  
{% /callout %}

```

This formats the document clearly, providing relevant sections, syntax, examples, and a note for additional resources, consistent with the schema you've provided.
