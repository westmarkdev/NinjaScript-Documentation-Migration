---
title: "Darvas"
pathName: /docs/desktop/darvas
---

## Description

A trading strategy that was developed in 1956 by former ballroom dancer Nicolas Darvas. Darvas' trading technique involved buying into stocks that were trading at new 52-week highs with correspondingly high volumes.

... Courtesy of [Investopedia](http://www.investopedia.com/terms/d/darvasboxtheory.asp)


## Syntax

```csharp
Darvas()
```

```csharp
Darvas(ISeries<double> input)
```

Returns the upper value:

```csharp
Darvas().Upper[int barsAgo]
```

```csharp
Darvas(ISeries<double> input).Upper[int barsAgo]
```

Returns the lower value:

```csharp
Darvas().Lower[int barsAgo]
```

```csharp
Darvas(ISeries<double> input).Lower[int barsAgo]
```


## Return Value

`double`; Accessing this method via an index value `[int barsAgo]` returns the indicator value of the referenced bar.


## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([Valid Input Data for Indicator](/docs/desktop/valid_input_data_for_indicator)) |


## Example

```csharp
// Prints the current upper Darvas value
double value = Darvas().Upper[0];
Print("The current upper Darvas value is " + value.ToString());
```


## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.

