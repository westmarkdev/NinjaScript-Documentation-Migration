---
status: double_check
pathName: update
title: Update()
parent: onbarupdate
section: references
lg2m: true
---

## Definition

Forces the OnBarUpdate() method to be called for all data series so that indicator values are updated to the current bar index.  If the values are already up to date, the Update() method will not be run.

{% callout type="note" %}

- This method is only relevant in specific use cases and should only used by advanced programmers

- The additional overload where a bar index and [BarsInProgress](barsinprogress) are specified should only be used when an indicator needs to be updated to a bar index that is not the [CurrentBar](source_files/currentbar.md) index. For example, updating an indicator's secondary 1 tick data series to indicator.BarsArray[1].Count - 1, which is not the [CurrentBar](source_files/currentbar.md) index. This is required for the proper function of [Order Flow Cumulative Delta](order_flow_cumulative_delta.md) and [Order Flow VWAP](order_flow_vwap.md)

{% /callout }

When indicators are embedded (called) within a NinjaScript strategy, they are optimized to calculate only when they are called upon in a historical backtest. Since the NinjaTrader indicator model is very flexible, it is possible to create public properties on a custom indicator that return values of internal user defined variables. If these properties require that the OnBarUpdate() method is called before returning a value, include a call to this Update() method in the property getter.

## Syntax

**Update()**

**Update(int idx, int bip)**

## Parameters

{% table %}

* Parameter

* Description

---

* idx

* The current bar index value to update to

---

* bip

* The [BarsInProgress](barsinprogress) to update

---

{% /table %}

## Examples

```csharp
private double tripleValue = 0;  
   
protected override void OnBarUpdate()  
{  
  if (CurrentBar < 20)  
      return;  
   
  tripleValue = SMA(20)[0] * 3;  
  Value[0] = SMA(20)[0];  
}  
   
public double TripleValue  
{  
    get  
    {  
      //call OnBarUpdate before returning tripleValue  
      Update();  
      return tripleValue;  
    }  
}
```
