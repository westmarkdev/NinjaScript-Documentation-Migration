










 


Set Up







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?set_up10.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Developing Strategies](developing_strategies.htm) &gt; [Beginner - Simple MA Cross Over](beginner_-_simple_ma_cross_ove.htm) &gt;
Set Up | [Previous page](beginner_-_simple_ma_cross_ove.htm)
[Return to chapter overview](beginner_-_simple_ma_cross_ove.htm)










The first step in creating a custom strategy is to use the custom [Strategy Builder](strategy_builder.htm). The builder provides two options:


 


•Allow you to create a functional strategy without any programming

•Generate the required NinjaScript code that will serve as the foundation for your custom strategy for further coding 

 


1. Within the NinjaTrader Control Center window select the  New Strategy Builder... menu


2. Press the "Next &gt;" button


 


![SimpleMACrossoverSetUp1](simplemacrossoversetup1.png)


 


3. Enter the information as shown above


4. Press the "Next &gt;" button


 


Setting Default Properties
--------------------------


The next page will allow you to set defaults for basic properties related to your strategy, including it's [Calculate](calculate.htm) and [EntryHandling](entryhandling.htm) settings. Click the More Properties button to expose additional properties. For this tutorial, we will not change any basic properties' defaults, and instead will leave them all set to the values shown below:


 


![SimpleMACrossoverSetUp2](simplemacrossoversetup2.png)


 


Adding Additional Data
----------------------


The next page will allow you to configure one or more additional [Bars](bars.htm) objects for use by the strategy. For our purposes, we will leave this page blank and move forward by clicking the Next &gt; button.


 


![SimpleMACrossoverSetUp3](simplemacrossoversetup3.png)



Defining Input Parameters
-------------------------


Below you will define your strategy's input parameters. These are any input parameters that can be changed by the user when running or backtesting a strategy. If your strategy does not require any parameters leave the "Name" fields blank.


 


![SimpleMACrossoverSetUp4](simplemacrossoversetup4.png)


1.Click the add button to add a property

2.Add input parameters into the newly created Input Parameters window and click Ok once the input parameter is set up

 


![SimpleMACrossoverSetUp5](simplemacrossoversetup5.png)


 


5. Add the inputs as per the image above   

6. Press the "Next &gt;" button


 


Defining Conditions and Actions
-------------------------------


Below you can define conditions that trigger user defined actions such as placing orders, drawing on a chart or creating an alert.


 


Notice how there are two buttons on the screen below:


 


View Code... - Pressing this button loads the strategy code in the NinjaScript Editor for viewing purposes only. This is a great approach if you are new to programming or you want to see how the strategy wizard dynamically generates the correct script code on the fly.


 


Unlock Code - Pressing this button loads the strategy code in the NinjaScript editor for further manual editing. Once this button is pressed, you can NOT go back to the Wizard for strategy construction and editing.


 


![SimpleMACrossoverSetUp6](simplemacrossoversetup6.png)


 


If you want to proceed with this tutorial through [self programming continue here](creating_the_strategy_via_self.htm) after pressing the "Unlock Code" button.


If you want to proceed with this tutorial through [using the Strategy Builder please click here](creating_the_strategy_via_the_.htm).





 
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
 
 
 



