---
title: OnBarsChanged()
pathName: onbarschanged
parent: drawing_tools
status: imported
section: references
---

## Definition

An event driven method which is called any time the underlying bar series have changed for the chart where the drawing tool resides. For example if a user has changed the primary instrument or the time frame of the bars used on the chart.

## Method Return Value

This method does not return a value.

## Syntax

You must override this method using the following syntax:

**public override void OnBarsChanged()**  

## Method Parameters

This method does not accept any parameters.

## Examples

```csharp

public override void OnBarsChanged()
{
    //bars have change, do something
}
```
