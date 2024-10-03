---

title: ischartonly
pathName: ischartonly
created: Thursday, October 3rd 2024, 11:24:32 am
updated: Thursday, October 3rd 2024, 12:16:54 pm
---

## Definition

If true, any indicator will be only available for charting usage - indicators with this property enabled would for example not be expected to show if called in a SuperDOM or MarketAnalyzer window.

## Property Value

This property returns true if the indicator can only be used on a chart; otherwise, false. Default set to false.

|  |
| --- |
| Warning: This property should ONLY be set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |

## Syntax

`IsChartOnly`

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        IsChartOnly = true; // Allow the indicator to work in charting environment only       
    }
}
```

```

### Notes
- Ensure that the IsChartOnly property is only set in the appropriate state to prevent unexpected behavior when the indicator is used in environments other than charts.
