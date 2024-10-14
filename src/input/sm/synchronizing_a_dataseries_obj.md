


Synchronizing a DataSeries object to a secondary time frame









 


Synchronizing a DataSeries object to a secondary time frame















Series objects are useful for storing interim calculations to your strategy. Sometimes you will want to store calculations based on another time frame that is not the primary bar series in a strategy.


 


Key concepts in this example
----------------------------


•Creating Series objects

•Storing and retrieving values from Series objects

 


Important related documentation
-------------------------------


•[AddDataSeries()](adddataseries.htm)

•[Series Class](seriest.htm)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleSyncSecondarySeries\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleSyncSecondarySeries_NT8.zip)





 
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
 
 
 



