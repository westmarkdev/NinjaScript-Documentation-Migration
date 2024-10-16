---
title: "KeyReversalDown"
pathName: /docs/desktop/keyreversaldown
---

## Description

Returns a value of 1 when the current close is less than the prior close and the current high has penetrated the highest high of the last n bars.

## Syntax

```csharp
KeyReversalDown(int period)

KeyReversalDown(ISeries<double> input, int period)

KeyReversalDown(int period)[int barsAgo]

KeyReversalDown(ISeries<double> input, int period)[int barsAgo]
```

## Return Value

`double`; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([Valid Input Data for Indicator](/docs/desktop/valid_input_data_for_indicator)) |
| period | Number of bars used in the calculation |

## Example

```csharp
// If we get a reversal over the past 10 bars go short
if (KeyReversalDown(10)[0] == 1)
    EnterShort();
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
