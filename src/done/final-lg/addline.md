---
title: "AddLine()"
pathName: addline
---

## Definition

Adds line objects on a chart.

{% callout type="note" %}
Lines are ONLY visible from the UI property grid when AddLine() is called from State.SetDefaults. If your indicator or strategy dynamically adds lines during State.Configure, you will NOT have an opportunity to select the line or to set the line configuration via the UI. Alternatively, you may use custom public [Brush](brushes), [Stroke](stroke_class) or value properties which are accessible in the State.SetDefaults and pass those values to AddLine() during State.Configure. Calling AddLine() in this manner should be reserved for special cases. Please see the examples below.
{% /callout %}

## Methods and Properties

|  |  |
| --- | --- |
| [AreLinesConfigurable](arelinesconfigurable) | Determines if the [line](addline)(s) used in an indicator are configurable from within the indicator dialog window. |
| [Line Class](line_class) | Objects derived from the Line class are used to characterize how an oscillator line is visually displayed (plotted) on a chart. |
| [Lines](lines) | A collection holding all of the Line objects that define the visualization characteristics oscillator lines of the indicator. |

## Syntax

```plaintext
AddLine(Brush brush, double value, string name)
AddLine(Stroke stroke, double value, string name)
```

{% callout type="warning" %}
This method should ONLY be called within the [OnStateChange()](onstatechange) method during State.SetDefaults or State.Configure.
{% /callout %}

## Parameters

|  |  |
| --- | --- |
| brush | A Brush object used to construct the line. |
| name | A string value representing the name of the line. |
| stroke | A Stroke object used to construct the line. |
| value | A double value representing the value the line will be drawn at. |

## Examples

### Defining a single UI configurable static line

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        Name = "Examples Indicator";  
        // Adds an oscillator line at a value of 30
        AddLine(Brushes.Gray, 30, "Lower");
    }
}
```

### Indicator which dynamically adds a line in State.Configure

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        Name = "Examples Indicator";
        // logical property which user can set
        UseSpecialMode = false;
        // Default brush selection pushed to the UI
        MyBrush = Brushes.Red;
    }
    else if (State == State.Configure)
    {
        // if user enables logical property
        if (UseSpecialMode)
        {
            // add line using default selected brush and special line name
            AddLine(MyBrush, 40, "My Special Line");
        }
        else
        {
            // otherwise use default selected brush and regular line name
            AddLine(MyBrush, 60, "My Regular Line");
        }
    }
}

[XmlIgnore]
public Brush MyBrush { get; set; }
public bool UseSpecialMode { get; set; }
```
