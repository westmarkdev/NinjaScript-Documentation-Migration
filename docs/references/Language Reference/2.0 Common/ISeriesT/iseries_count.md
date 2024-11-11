---
title: Count
pathName: iseries_count
parent: iseriest
section: references
status: changed
---

## Definition

Indicates the number total number of values in the **ISeries** array. This value should always be in sync with the [**CurrentBars**](currentbars) array for that series.

## Method Return Value

A int representing the total size of the series.

## Syntax

**Count**

## Examples

```csharp
protected override void OnBarUpdate()
{
    Print("Input count: " + Input.Count);
}
```
