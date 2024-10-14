










 


Flatten()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?flatten.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Account](account_class.htm) &gt;
Flatten() | [Previous page](executionupdate.htm)
[Return to chapter overview](account_class.htm)










Definition
----------


Flattens the account on an instrument.


 


Syntax
------


Flatten(ICollection<instrument> instruments)


 


Parameters
----------




|  |  |
| --- | --- |
| instruments | A collection of Instruments for orders to be cancelled and positions closed |



 



Examples
--------




| ns Flatten a single instrument |
| --- |
| Account.Flatten(new [] { Instrument.GetInstrument("ES 12-15") }); |



 





| ns Flatten a list of instruments |
| --- |
| // Please note that your 'Using declarations' section needs to have 
//
// using System.Collections.ObjectModel;
//
// added in order for this example to compile correctly
 
// instantiate a list of instruments
Collection<cbi.instrument> instrumentsToClose = new Collection<instrument>();         
 
// add instruments to the collection
instrumentsToClose.Add(Instrument.GetInstrument("AAPL"));         
instrumentsToClose.Add(Instrument.GetInstrument("MSFT"));
 
// pass the instrument collection to the Flatten() method to be flattened
Account.Flatten(instrumentsToClose); |






 
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
 
 
 



</instrument></cbi.instrument></instrument>