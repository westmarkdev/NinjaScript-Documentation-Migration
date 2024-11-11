---
title: DataType
pathName: datatype
parent: market_analyzer_column
status: imported
section: references
---

## Definition

Determines the data type displayed in a Market Analyzer Column.

## Syntax

**DataType**

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
