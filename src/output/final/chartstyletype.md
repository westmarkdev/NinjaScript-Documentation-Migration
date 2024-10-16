---
title: "ChartStyleType"
pathName: /docs/desktop/chartstyletype
---

## Definition

Defines a unique identifier value used to register a custom ChartStyle. There are 11 default ChartStyles which come with NinjaTrader that are reserved per the table on this page under the Parameters section of this page.

{% callout type="note" %}
The ChartStyle property can allow a large number of ChartStyles to be registered on a single user's installation (up to 2,147,483,647). However, it's important to note that it is still possible for two installed ChartStyles on a user's computer to conflict should they be registered to the same enumerator value. In this case, NinjaTrader will ignore the conflicting ChartStyle type and information pertaining to this conflict will be displayed on the [Log tab](/docs/desktop/log_tab2) of the NinjaTrader Control Center.  
Added 1/31/2018: We advise users to use values larger than 1023 when selecting an enum, as NinjaTrader may from time to time add a new enum value in that range which may cause conflicts.
{% /callout %}

## Property Value

An enum value representing the ChartStyle to be registered.

{% callout type="tip" %}
It is recommended to pick a high, unique enumeration value to avoid conflicts from other ChartStyles that may be used by a single installation.
{% /callout %}

## Syntax

You must cast ChartStyleType from an int using the following syntax:

```csharp
(ChartStyleType) 80;
```

## Parameters

Reserved enumeration values are listed below:

|  |  |
| --- | --- |
| 0 | Box |
| 1 | CandleStick |
| 2 | LineOnClose |
| 3 | OHLC |
| 4 | PointAndFigure |
| 5 | KagiLine |
| 6 | OpenClose |
| 7 | Mountain |
| 8 | Volumetric |
| 9 | HollowCandleStick |
| 10 | Equivolume |

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        Name = "Example ChartStyle";
        ChartStyleType = (ChartStyleType) 80;
        BarWidth = 1;
    }
}
```

