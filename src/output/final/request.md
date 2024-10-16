---
title: "Request()"
pathName: /docs/desktop/request
---

## Definition

Performs the bars request for a [BarsRequest](/docs/desktop/barsrequest) object.

## Syntax

```csharp
BarsRequest.Request(Action<BarsRequest, ErrorCode, string> callback)
```

## Properties

| Property         | Description                                                         |
| ---------------- | ------------------------------------------------------------------- |
| BarsRequest      | A `BarsRequest` representing the bars                              |
| ErrorCode        | An `ErrorCode` representing error status                           |
| string           | A `string` representing error message                               |

## Example

```csharp
// Request the bars
barsRequest.Request(new Action<BarsRequest, ErrorCode, string>((bars, errorCode, errorMessage) =>
{
    if (errorCode != ErrorCode.NoError)
    {
        // Handle any errors in requesting bars here
        NinjaTrader.Code.Output.Process(string.Format("Error on requesting bars: {0}, {1}",
            errorCode, errorMessage), PrintTo.OutputTab1);
        return;
    }
    // Do something with the returned bars here.
    for (int i = 0; i < bars.Bars.Count; i++)
    {
        // Output the bars
        NinjaTrader.Code.Output.Process(string.Format("Time: {1} Open: {2} High: {3} Low: {4} Close: {5} Volume: {6}",
            bars.Bars.GetTime(i),
            bars.Bars.GetOpen(i),
            bars.Bars.GetHigh(i),
            bars.Bars.GetLow(i),
            bars.Bars.GetClose(i),
            bars.Bars.GetVolume(i)), PrintTo.OutputTab1);
    }
}));
```
