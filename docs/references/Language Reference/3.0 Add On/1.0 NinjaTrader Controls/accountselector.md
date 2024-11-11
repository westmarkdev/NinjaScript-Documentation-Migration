---
title: AccountSelector
pathName: accountselector
parent: controls
status: imported
order: 0
section: references
---

## Definition

AccountSelector can be used as an UI element users can interact with for selecting accounts.

## Events and Properties

{% table %}

* Method/Property
* Description

---

* Cleanup()
* Disposes of the AccountSelector (Note: calling the **NTTabPage base.Cleanup()** is sufficient to clean up this control)

---

* SelectedAccount
* Returns an **Account** representing the selected account

---

* SelectionChanged
* Event handler for when the selected account has changed
{% /table %}

## Examples

```csharp
/* Example of subscribing/unsubscribing to market data from an Add On. The concept can be carried over
to any NinjaScript object you may be working on. */
public class MyAddOnTab : NTTabPage
{
     private AccountSelector accountSelector

     public MyAddOnTab()
     {
         // Note: pageContent (not demonstrated in this example) is the page content of the XAML
         // Find account selector
         accountSelector = LogicalTreeHelper.FindLogicalNode(pageContent, "accountSelector") as AccountSelector;

         // When the account selector's selection changes, unsubscribe and resubscribe
         accountSelector.SelectionChanged += (o, args) =>
         {
             if (accountSelector.SelectedAccount != null)
             {
                 // Unsubscribe to any prior account subscriptions
                 accountSelector.SelectedAccount.AccountItemUpdate -= OnAccountItemUpdate;
                 accountSelector.SelectedAccount.ExecutionUpdate -= OnExecutionUpdate;
                 accountSelector.SelectedAccount.OrderUpdate -= OnOrderUpdate;
                 accountSelector.SelectedAccount.PositionUpdate -= OnPositionUpdate;

                 // Subscribe to new account subscriptions
                 accountSelector.SelectedAccount.AccountItemUpdate   += OnAccountItemUpdate;
                 accountSelector.SelectedAccount.ExecutionUpdate     += OnExecutionUpdate;
                 accountSelector.SelectedAccount.OrderUpdate         += OnOrderUpdate;
                 accountSelector.SelectedAccount.PositionUpdate      += OnPositionUpdate;
             }
         };
     }

     // Called by TabControl when tab is being removed or window is closed
     public override void Cleanup()
     {
         // Clean up our resources
         base.Cleanup();
     }

     // Other required NTTabPage members left out for demonstration purposes. Be sure to add them in your own code.
}
```

```xml
<page xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:accountdata="clr-namespace:NinjaTrader.Gui.AccountData;assembly=NinjaTrader.Gui" xmlns:accountperformance="clr-namespace:NinjaTrader.Gui.AccountPerformance;assembly=NinjaTrader.Gui" xmlns:atmstrategy="clr-namespace:NinjaTrader.Gui.NinjaScript.AtmStrategy;assembly=NinjaTrader.Gui" xmlns:tools="clr-namespace:NinjaTrader.Gui.Tools;assembly=NinjaTrader.Gui" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">

<grid>
     <tools:accountselector horizontalalignment="Left" verticalalignment="Top" x:name="accountSelector"></tools:accountselector>
</grid>
</page>
```
