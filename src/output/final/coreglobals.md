---
title: "Globals"
pathName: /docs/core/globals
---

## Globals from NinjaTrader Core

Geben Sie hier den Text ein.

{% callout type="note" %}
This section may include additional details about the global variables and their usage within NinjaTrader Core, ensuring developers understand how to effectively utilize them in their scripts and strategies.
{% /callout %}

## Additional Information

- Please consult the [NinjaTrader documentation](/docs/) for more insights on globals.
- Ensure to review environment setups that might affect globals.

{% callout type="tip" %}
When using globals, it's crucial to understand the scope of each variable, particularly in multi-threaded scenarios.
{% /callout %}

## Example Usage

```csharp
// Example of using a global variable
public class MyStrategy : Strategy
{
    private double myGlobalVariable;

    protected override void OnStartUp()
    {
        myGlobalVariable = Globals.MyGlobalValue; 
    }
}
```

Ensure to replace `Globals.MyGlobalValue` with the actual global variable you intend to use.