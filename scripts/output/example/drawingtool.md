---

title: drawingtool
pathName: drawingtool
created: Thursday, October 3rd 2024, 11:24:26 am
updated: Thursday, October 3rd 2024, 12:16:54 pm
---

## Definition

The DrawingTool object which owns a chart anchor.

## Property Value

A IDrawingTool object representing the owner of the chart anchor.

## Syntax

```csharp
<chartanchor>.DrawingTool
```

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {   
        Name = "SampleDrawingTool";       
        MyAnchor = new ChartAnchor();
        MyAnchor.DrawingTool = this; // NinjaTrader.NinjaScript.DrawingTools.SampleDrawingTool
    }
    else if (State == State.Configure)
    {
        // Configuration code here
    }
}
```

{% callout type="note" %}  
Make sure to correctly initialize and configure your drawing tools within the OnStateChange method.  
{% /callout %}
