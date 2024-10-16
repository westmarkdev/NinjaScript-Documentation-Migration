---
title: "Checking for Null References"
pathName: /checking_for_null_references
---

## Overview

A common object-oriented programming error is not checking for null references on your object variables. This will cause an "Object reference not set to an instance of an object" error.

## Example

You create a variable that holds an Order object:

```csharp
private Order entryOrder = null;
```

But in the `OnBarUpdate()` method, you do not check if this variable has been assigned an Order object. Thus, when trying to access object properties, it fails and yields the "Object reference not set" error since the variable is null.

```csharp
protected override void OnBarUpdate()
{
    if (entryOrder.Filled > 0)
        // Do something
}
```

This will generate an error because you cannot access the object or any of its properties yet. You must always check if an object variable is null before attempting to access the object.

```csharp
protected override void OnBarUpdate()
{
    if (entryOrder == null)
    {
        entryOrder = EnterLong();
    }
    else if (entryOrder != null)
    {
        if (entryOrder.Filled > 0)
            // Do something
    }
}
```

{% callout type="note" %}
Always ensure to implement null checks on your object variables to prevent runtime exceptions and maintain the stability of your application.
{% /callout %}

{# Ensure to include a blank line at the end #}
