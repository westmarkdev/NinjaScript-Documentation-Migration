---
title: PanelUI
pathName: panelui
parent: common
section: references
status: imported
---

## Definition

The zero-based index of the chart panel in which the calling script is configured.

{% callout type="note" %}

The "Panel" property configured in the Indicators or Strategies window on a chart is non-zero-based, while **PanelUI** is zero-based. For example, if an indicator is configured in Panel # 1 in the Indicators window, **PanelUI** will return an index of 0. If the indicator were configured in Panel # 4 in the Indicators window, **PanelUI** would return an index of 3.

{% /callout %}

## Property Value

An **int** value representing the panel the object is configured. This property is read-only.

## Syntax

**PanelUI**

## Examples

```csharp
protected override void OnBarUpdate()
{
   // Print the zero-based panel index on which the script is configured
   Print("My object is on is on panel # " + **PanelUI**);
}
```
