---
title: "InstrumentType"
pathName: /docs/desktop/instrumenttype
---

## Definition

Returns the type of instrument.

## Property Value

An `InstrumentType` representing the type of an instrument.

Possible values are:

- `InstrumentType.Future`
- `InstrumentType.Stock`
- `InstrumentType.Index`
- `InstrumentType.Forex`
- `InstrumentType.Cfd`
- `InstrumentType.Cryptocurrency`

## Syntax

```csharp
Instrument.MasterInstrument.InstrumentType
```

## Examples

```csharp
if (Instrument.MasterInstrument.InstrumentType == InstrumentType.Future)
{
    // Do something
}
else
{
    // Do something else
}
```

{% callout type="note" %}
This property can be accessed without a null reference check in the `OnBarUpdate()` event handler. When the `OnBarUpdate()` event is triggered, there will always be an Instrument object. Should you wish to access this property elsewhere, check for null reference first. e.g. `if (Instrument != null)`
{% /callout %}

