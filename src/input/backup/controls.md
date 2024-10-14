










 


NinjaTrader Controls







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?controls.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt;
NinjaTrader Controls | [Previous page](add_on.htm)
[Return to chapter overview](add_on.htm)










The following section contains controls that are native NinjaTrader controls. To fully integrate your Add On within NinjaTrader it is recommended to use these controls as opposed to building your own when possible.


 




|  |
| --- |
| Note:  For cleaning up these resources, please see the [NTTabPage.Cleanup()](nttabpage_cleanup.htm) method |



 


 




|  |  |
| --- | --- |
| [AccountSelector](accountselector.htm) | AccountSelector can be used as an UI element users can interact with for selecting accounts. |
| [AtmStrategySelector](atmstrategyselector.htm) | AtmStrategySelector is an UI element users can interact with for selecting ATM Strategies. |
| [InstrumentSelector](instrumentselector.htm) | InstrumentSelector is a UI element users can interact with for selecting instruments. This can be used with instrument linking between windows.  |
| [IntervalSelector](intervalselector.htm) | IntervalSelector is as a UI element users can interact with for selecting intervals. This can be used with interval linking between windows. |
| [TifSelector](tifselector.htm) | TifSelector can be used as an UI element users can interact with for selecting TIF. |
| [QuantityUpDown](quantityupdown.htm) | QuantityUpDown can be used as an UI element users can interact with for selecting quantity. |






 
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
 
 
 



