---
title: "KeyReversalUp"
pathName: /docs/desktop/keyreversalup
---

## Description

Returns a value of 1 when the current close is greater than the prior close and the current low has penetrated the lowest low of the last n bars.

## Syntax

```csharp
KeyReversalUp(int period)
```

```csharp
KeyReversalUp(ISeries<double> input, int period)
```

```csharp
KeyReversalUp(int period)[int barsAgo]
```

```csharp
KeyReversalUp(ISeries<double> input, int period)[int barsAgo]
```

## Return Value

`double`; Accessing this method via an index value `[int barsAgo]` returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([Input Data for Indicators](/docs/desktop/valid_input_data_for_indicator)) |
| period | Number of bars used in the calculation |

## Example

```csharp
// If we get a reversal over the past 10 bars go long
if (KeyReversalUp(10)[0] == 1)
    EnterLong();
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
