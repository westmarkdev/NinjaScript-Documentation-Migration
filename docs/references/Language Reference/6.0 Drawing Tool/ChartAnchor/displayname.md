---
title: DisplayName
pathName: displayname
parent: chartanchor
status: imported
section: references
---

## Definition

Sets the display name prefix used for all properties for a chart anchor.

## Property Value

A **string** value that is used to identify the name for a corresponding anchor. Default value is null.

## Syntax

**`<chartanchor>`.DisplayName**

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        MyAnchor = new ChartAnchor();
        MyAnchor.DisplayName = "MyChartAnchor";
    }
}
```
