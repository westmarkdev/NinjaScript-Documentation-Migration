---
title: "AccountItemEventArgs"
pathName: /docs/desktop/accountitemeventargs
---

## Definition

AccountItemEventArgs contains [Account](/docs/desktop/account_class)-related information to be passed as an argument to the [OnAccountItemUpdate()](/docs/desktop/onaccountitemupdate) event.

{% callout type="note" %}
For a complete, working example of this class in use, download the framework example located on our [Developing AddOns Overview](/docs/desktop/developing_add_ons).
{% /callout %}

The properties listed below are accessible from an instance of AccountItemEventArgs:

|  |  |
| --- | --- |
| Account | The Account for which OnAccountItemUpdate() was called |
| AccountItem | The [AccountItem](/docs/desktop/accountitem) which has updated, resulting in the call to OnAccountItemUpdate() |
| Currency | The currency of the Account in question |
| Time | A DateTime object representing the time at which the change occurred |
| Value | The new value of the updated AccountItems |

## Example

```csharp
// This method is fired on any change of an AccountItem
private void OnAccountItemUpdate(object sender, AccountItemEventArgs e)
{
    /* Dispatcher.InvokeAsync() is needed for multi-threading considerations. When processing events outside of the UI thread, and we want to
    influence the UI .InvokeAsync() allows us to do so. It can also help prevent the UI thread from locking up on long operations. */
    Dispatcher.InvokeAsync(() =>
    {
        // Print which AccountItem changed, on which account, and the new value, using
        outputBox.AppendText(string.Format("{0}Account: {1}{0}AccountItem: {2}{0}Value: {3}",
            Environment.NewLine,
            e.Account.Name,
            e.AccountItem,
            e.Value));
    });
}
```
