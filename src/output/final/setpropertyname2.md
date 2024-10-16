---
title: "SetPropertyName()"
pathName: /docs/desktop/setpropertyname2
---

## Definition

Sets a default property name to a custom string to be displayed on the UI.

## Method Return Value

This method does not return a value.

## Syntax

```csharp
SetPropertyName(string propertyName, string displayName)
```

## Method Parameters

|  |  |
| --- | --- |
| propertyName | A string representing the property to be renamed. Possible values include: {% <br> %} &bull; UpBrush{% <br> %} &bull; DownBrush{% <br> %} &bull; BarWidth{% <br> %} &bull; Stroke{% <br> %} &bull; Stroke2{% <br> %} &bull; Value{% <br> %} &bull; Value2{% <br> %} &bull; BaseBarsPeriodType{% <br> %} &bull; BaseBarsPeriodValue{% <br> %} &bull; PointAndFigurePriceType{% <br> %} &bull; ReversalType |
| displayName | A string representing the desired property name |

## Example

```csharp
protected override void OnStateChange()
{
    if (State == State.Configure)
    {
        Properties.Remove(Properties.Find("Stroke", true));
        Properties.Remove(Properties.Find("Stroke2", true));
        SetPropertyName("UpBrush", "AdvanceBar");
        SetPropertyName("DownBrush", "DeclineBar");
    }
}
```

{% callout type="note" %}
If you do not wish to use specific properties accessible via SetPropertyName(), you will need to remove them from the list via Properties.Remove, as shown in the example above.
{% /callout %}