---
title: "Format()"
pathName: /docs/desktop/format
---

## Definition

This method allows you to customize the rendering of the value in the Market Analyzer Column.

## Syntax

```csharp
public override string Format(double value)
{
}
```

## Examples

```csharp
public override string Format(double value)
{
    return (value == double.MinValue ? string.Empty : Instrument.MasterInstrument.FormatPrice(value));
}
```

