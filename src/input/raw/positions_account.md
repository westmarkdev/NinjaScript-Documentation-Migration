










 


Positions







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?positions_account.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Account](account_class.htm) &gt;
Positions | [Previous page](orderupdate.htm)
[Return to chapter overview](account_class.htm)










Definition
----------


A collection of Position objects generated for the specified account


 


Property Value
--------------


An [Collection](https://msdn.microsoft.com/en-us/library/ms132397(v=vs.110).aspx) of Position objects


 


Syntax
------


Account.Positions


<account>.Positions



Examples
--------




| ns |
| --- |
| private Account myAccount;
 
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
    {
       // Find our Sim101 account
       lock (Account.All)
            myAccount = Account.All.FirstOrDefault(a =&gt; a.Name == "Sim101");
    }
 
   if (State == State.DataLoaded)
    {
       lock (myAccount.Positions)
        {
            Print("Positions in State.DataLoaded:");
 
           foreach (Position position in myAccount.Positions)
            {
                Print(String.Format("Position: {0} at {1}", position.MarketPosition, position.AveragePrice));
            }
        }
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
 
 
 



</account>