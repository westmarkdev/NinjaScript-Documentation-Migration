---
title: accountitemupdate
pathName: accountitemupdate
created: Thursday, October 3rd 2024, 11:50:25 am
updated: Thursday, October 3rd 2024, 12:16:55 pm
---

## Definition

AccountItemUpdate is used for subscribing to account item update events.

{% callout type="note" %}  
Remember to unsubscribe if you are no longer using the subscription.  
{% /callout %}

## Syntax

```csharp
// Subscribe to account item updates
account.AccountItemUpdate += OnAccountItemUpdate;
```

## Example

```csharp
/* Example of subscribing/unsubscribing to account item update events from an Add On. The concept can be carried over
to any NinjaScript object you may be working on. */
public class MyAddOnTab : NTTabPage
{
     private Account account;
     public MyAddOnTab()
     {
          // Find our Sim101 account
          lock (Account.All)
               account = Account.All.FirstOrDefault(a => a.Name == "Sim101");

          // Subscribe to account item updates
          if (account != null)
               account.AccountItemUpdate += OnAccountItemUpdate;
     }

     // This method is fired on any change of an account value
     private void OnAccountItemUpdate(object sender, AccountItemEventArgs e)
     {
          // Output the account item
          NinjaTrader.Code.Output.Process(string.Format("Account: {0} AccountItem: {1} Value: {2}",
               e.Account.Name, e.AccountItem, e.Value), PrintTo.OutputTab1);
     }

     // Called by TabControl when tab is being removed or window is closed
     public override void Cleanup()
     {
          // Make sure to unsubscribe to the account item subscription
          if (account != null)
               account.AccountItemUpdate -= OnAccountItemUpdate;
     }

     // Other required NTTabPage members left out for demonstration purposes. Be sure to add them in your own code.
}
```
