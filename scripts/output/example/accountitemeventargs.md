---
title: accountitemeventargs
path: accountitemeventargs
created: Thursday, October 3rd 2024, 11:50:40 am
updated: Thursday, October 3rd 2024, 12:16:55 pm
---

## Definition

AccountItemEventArgs contains [Account](account_class.htm)-related information to be passed as an argument to the [OnAccountItemUpdate()](onaccountitemupdate.htm) event.

{% callout type="note" %}  
For a complete, working example of this class in use, download the framework example located on our [Developing AddOns Overview](developing_add_ons.htm).  
{% /callout %}

The properties listed below are accessible from an instance of AccountItemEventArgs:

| Property       | Description                                                                       |
|----------------|-----------------------------------------------------------------------------------|
| Account        | The Account for which OnAccountItemUpdate() was called.                          |
| AccountItem    | The [AccountItem](accountitem.htm) which has updated, resulting in the call to OnAccountItemUpdate(). |
| Currency       | The currency of the Account in question.                                         |
| Time           | A DateTime object representing the time at which the change occurred.           |
| Value          | The new value of the updated AccountItems.                                       |

## Example

```csharp
// This method is fired on any change of an AccountItem
private void OnAccountItemUpdate(object sender, AccountItemEventArgs e)
{
    /* Dispatcher.InvokeAsync() is needed for multi-threading considerations. When processing events outside of the UI thread, 
    and we want to influence the UI .InvokeAsync() allows us to do so. It can also help prevent the UI thread from locking up on long operations. */
    Dispatcher.InvokeAsync(() =>
    {
        // Print which AccountItem changed, on which account, and the new value
        outputBox.AppendText(string.Format("{0}Account: {1}{0}AccountItem: {2}{0}Value: {3}",
            Environment.NewLine,
            e.Account.Name,
            e.AccountItem,
            e.Value));
    });
}
```

{% callout type="note" %}  
Ensure to handle threading considerations by using Dispatcher.InvokeAsync() when updating UI elements based on AccountItem changes.  
{% /callout %}