










 


AccountSelector







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?accountselector.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [NinjaTrader Controls](controls.htm) &gt;
AccountSelector | [Previous page](controls.htm)
[Return to chapter overview](controls.htm)










Definition
----------


AccountSelector can be used as an UI element users can interact with for selecting accounts.


 


Events and Properties
---------------------




|  |  |
| --- | --- |
| Cleanup() | Disposes of the AccountSelector (Note: calling the [NTTabPage base.Cleanup()](nttabpage_cleanup.htm) is sufficient to clean up this control) |
| SelectedAccount | Returns an [Account](account_class.htm) representing the selected account |
| SelectionChanged | Event handler for when the selected account has changed |



 


 



Examples
--------




| C# |
| --- |
| /* Example of subscribing/unsubscribing to market data from an Add On. The concept can be carried over
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
          accountSelector.SelectionChanged += (o, args) =&gt;
          {
               if (accountSelector.SelectedAccount != null)
               {
                    // Unsubscribe to any prior account subscriptions
                   accountSelector.SelectedAccount.AccountItemUpdate -= OnAccountItemUpdate;
                    accountSelector.SelectedAccount.ExecutionUpdate -= OnExecutionUpdate;
                   accountSelector.SelectedAccount.OrderUpdate -= OnOrderUpdate;
                    accountSelector.SelectedAccount.PositionUpdate -= OnPositionUpdate;
 
                    // Subscribe to new account subscriptions
                   accountSelector.SelectedAccount.AccountItemUpdate   += OnAccountItemUpdate;
                    accountSelector.SelectedAccount.ExecutionUpdate     += OnExecutionUpdate;
                    accountSelector.SelectedAccount.OrderUpdate         += OnOrderUpdate;
                    accountSelector.SelectedAccount.PositionUpdate      += OnPositionUpdate;
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
} |






| XAML |
| --- |
| <page xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:accountdata="clr-namespace:NinjaTrader.Gui.AccountData;assembly=NinjaTrader.Gui" xmlns:accountperformance="clr-namespace:NinjaTrader.Gui.AccountPerformance;assembly=NinjaTrader.Gui" xmlns:atmstrategy="clr-namespace:NinjaTrader.Gui.NinjaScript.AtmStrategy;assembly=NinjaTrader.Gui" xmlns:tools="clr-namespace:NinjaTrader.Gui.Tools;assembly=NinjaTrader.Gui" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
 
<grid>
     <tools:accountselector horizontalalignment="Left" verticalalignment="Top" x:name="accountSelector"></tools:accountselector>
</grid> |






 
 var lastSlashPos = document.URL.lastIndexOf("/") &gt; document.URL.lastIndexOf("\\") ? document.URL.lastIndexOf("/") : document.URL.lastIndexOf("\\");
 if (document.URL.substring(lastSlashPos + 1, lastSlashPos + 4).toLowerCase() != "~hh") {
 if (document.all) setTimeout(function() {
 nsrInit();
 }, 20);
 else nsrInit();
 }
 
 
 $('.sync-toc').show();
 $('p.crumbs').hide();
 }
 
 
 



</page>