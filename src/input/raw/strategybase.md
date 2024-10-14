










 


StrategyBase







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?strategybase.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt;
StrategyBase | [Previous page](startatmstrategy.htm)
[Return to chapter overview](add_on.htm)










StrategyBase contains properties and methods for managing a [Strategy](strategy.htm) object, and is the base class from which [AtmStrategy](atmstrategy.htm) derives. 


 




|  |
| --- |
| Note:  For a complete, working example of this class in use, download framework example located on our [Developing AddOns Overview](developing_add_ons.htm) |



 



Example
-------




| ns |
| --- |
| // A button called acctStratButton in an NTTabPage displays all ATM and NinjaScript strategies configured on a selected Account when clicked
private void OnButtonClick(object sender, RoutedEventArgs e)
{
   Button button = sender as Button;
    
   if (button != null &amp;&amp; ReferenceEquals(button, acctStratButton))
   {
       // When the button is pressed, iterate through all ATM and NinjaScript strategies
       // This comprises all which are active, recovered upon last connect, or deactived since last connect
       // First, lock the Strategies collection to avoid in-flight changes to the collection affecting our output
       lock (accountSelector.SelectedAccount.Strategies)
           // Iterate through the Strategies collection in the selected Account
           foreach (StrategyBase strategy in accountSelector.SelectedAccount.Strategies)
               outputBox.AppendText(string.Format("{0}Name: {1}{0}ATM Template Name: {2}{0}Instrument: {3}{0}State: {4}{0}Category: {5}{0}",
                   Environment.NewLine,
                   strategy.Name,
                   strategy.Template,
                   strategy.Instruments[0].FullName,      
                   strategy.State,
                   strategy.Category));
   }
} |






 
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
 
 
 



