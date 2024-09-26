










 


PositionUpdate







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?positionupdate.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Account](account_class.htm) &gt;
PositionUpdate | [Previous page](positions_account.htm)
[Return to chapter overview](account_class.htm)










Definition
----------


PositionUpdate can be used for subscribing to position update events.


 


Note: Remember to unsubscribe if you are no longer using the subscription.


 


Syntax
------


PositionUpdate


 


 


Examples
--------




| ns |
| --- |
| /* Example of subscribing/unsubscribing to position update events from an Add On. The concept can be carried over
to any NinjaScript object you may be working on. */
public class MyAddOnTab : NTTabPage
{
     private Account account;
     public MyAddOnTab()
     {
         // Find our Sim101 account
         lock (Account.All)
               account = Account.All.FirstOrDefault(a =&gt; a.Name == "Sim101");
 
         // Subscribe to position updates
         if (account != null)
               account.PositionUpdate += OnPositionUpdate;
     }
 
     // This method is fired as a position changes
     private void OnPositionUpdate(object sender, PositionEventArgs e)
     {
         // Output the new position
         NinjaTrader.Code.Output.Process(string.Format("Instrument: {0} MarketPosition: {1} AveragePrice: {2} Quantity: {3}",
               e.Position.Instrument.FullName, e.MarketPosition, e.AveragePrice, e.Quantity), PrintTo.OutputTab1);
     }
 
     // Called by TabControl when tab is being removed or window is closed
     public override void Cleanup()
     {
         // Make sure to unsubscribe to the positions subscription
         if (account != null)
               account.PositionUpdate -= OnPositionUpdate;
     }
 
     // Other required NTTabPage members left out for demonstration purposes. Be sure to add them in your own code.
} |



 


 




|  |
| --- |
| Tip: The core MarketPosition e.Position is considered flat when Operation.Remove is seen, thus any related tracking in your logic you want to trigger or update should be aware. An Operation.Update would be seen if there was no flat state in between, i.e. on a reverse of the position. |






 
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
 
 
 



