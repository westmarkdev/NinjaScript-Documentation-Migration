---
title: Flatten()
pathName: flatten
parent: account
section: references
status: imported
---

## Definition

Flattens the account on an instrument.

## Syntax

**Flatten(ICollection<`instrument`> instruments)**

## Parameters

{% table %}

* instruments
* A collection of Instruments for orders to be cancelled and positions closed
{% /table %}

## Examples

### Flatten a single instrument

```csharp
Account.Flatten(new [] { Instrument.GetInstrument("ES 12-15") });
```

### Flatten a list of instruments

```csharp
// Please note that your 'Using declarations' section needs to have
//
// using System.Collections.ObjectModel;
//
//added in order for this example to compile correctly

// instantiate a list of instruments
Collection<cbi.instrument> instrumentsToClose = new Collection<instrument>();

// add instruments to the collection
instrumentsToClose.Add(Instrument.GetInstrument("AAPL"));
instrumentsToClose.Add(Instrument.GetInstrument("MSFT"));

// pass the instrument collection to the Flatten() method to be flattened
Account.Flatten(instrumentsToClose);

```
