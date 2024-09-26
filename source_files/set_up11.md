










 


Set Up







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?set_up11.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Developing Strategies](developing_strategies.htm) &gt; [Intermediate - RSI with Stop Loss &amp; Profit Target](intermediate_-_rsi_with_stop_l.htm) &gt;
Set Up | [Previous page](intermediate_-_rsi_with_stop_l.htm)
[Return to chapter overview](intermediate_-_rsi_with_stop_l.htm)










Our first tutorial covered using the [Strategy Builder](strategy_builder.htm) to create simple NinjaScript strategies or to build the framework needed for a more complex strategy.


 


This tutorial will cover another approach, using the NinjaScript [Editor](editor.htm) and [New Strategy Wizard](ns_wizard.htm).


 


1. Within the NinjaTrader Control Center window select the New NinjaScript  Editor... menu item


 


![NSTutControlCenter](nstutcontrolcenter.png)


 


![NSTutControlCenter2](nstutcontrolcenter2.png)


 


2. Click the "+" tab in the lower left, and select New Strategy to open a New Strategy Wizard


 


![RSIwithStopAndTargetSetUp1](rsiwithstopandtargetsetup1.png)


 


3. Enter the information as shown below


4. Press the "Next &gt;" button until we are at the Inputs and Parameters page


 


![RSIwithStopAndTargetSetUp2](rsiwithstopandtargetsetup2.png)


 


Defining Input Parameters
-------------------------


Below you will define your strategy's input parameters. These are any input parameters that can be changed by the user when running or backtesting a strategy. If your strategy does not require any parameters leave the "Name" fields blank.


 


5. Click the add button to create a User Input Parameter (See item 1 in the screenshot below)


6. Fill out the Input Parameters window and click OK to create the input parameter (See item 2 in the screenshot below)


 


![RSIwithStopAndTargetSetUp3](rsiwithstopandtargetsetup3.png)


 


7. Add the inputs as per the image below 


 


![RSIwithStopAndTargetSetUp4](rsiwithstopandtargetsetup4.png)


   

8. Press the "Generate" button to generate the code in the NinjaScript Editor.


 


You are now ready to continue to the [Entering Strategy Logic](entering_strategy_logic.htm) page of this tutorial.





 
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
 
 
 



