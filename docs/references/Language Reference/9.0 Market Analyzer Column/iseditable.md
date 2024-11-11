---
title: IsEditable
pathName: iseditable
parent: market_analyzer_column
status: imported
section: references
---

## Definition

Determines if a Market Analyzer Column is editable.

## Property Value

This property returns true if the Market Analyzer Column can be edited; otherwise, false.

## Syntax

**IsEditable**

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        DataType = typeof(string);
        IsEditable = true;
    }
}
```
