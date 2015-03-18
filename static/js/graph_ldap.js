$(function(){

   var visualizer;

   /*
    * Callbacks for the UI layer
    *
    */

   var buttons = [];

   // Little bit more complicated, toggle button for showing labels
   buttons.push({
      'label': 'Show labels',
      'default': 'on',
      'on': function(btn){
         visualizer.showLabels();
      },
      'off': function(btn){
         visualizer.hideLabels();
      },
   });

   buttons.push({
      'label': 'Never Logged In',
      'action': function(btn){
         /*
         type: member
         query: loggedin: 0
         */
         visualizer.filter();
      }
   });

   buttons.push({
      'label': 'Password never expires',
      'action': function(btn){
         /*
         type: member
         query: expires: false
         */
         visualizer.filter();
      }
   });

   buttons.push({
      'label': 'Highly connected members',
      'action': function(btn){
         /*
         type: member
         query: connections: gt 1
         style.size: sqrt(connections)
         */
      }
   });

   /*
    * Initialize the UI
    *
    */

   function onFilterGroupClicked(groupName, allGroups){
      // Here we want to do a 'where in' filter.  'where group in (list of active groups)'
      var activeGroups = [];
      for (groupName in allGroups) {
         if ( allGroups[groupName] === 1 ) activeGroups.push(groupName);
      }
      // Where 'cn' is in our list of activeGroups
      visualizer.filter({'cn': activeGroups});
   }

   var filterGroups = window.AVA.UI.FilterGroups({
      'filterGroupContainer': $('div.filters'),
      'onFilterGroupClicked': onFilterGroupClicked,
      'labelNameCallback': function friendlyLabel(input){ return input.replace(/(Ravencroft)|\-/g, ' '); },
   });

   var adhocButtons = window.AVA.UI.AdhocButtons({
      'buttonContainer': $('div.buttons'),
   });
   adhocButtons.add(buttons);

   // Construct the visualizer and load some initial data
   visualizer = window.AVA.Visualizer({
      'element': 'graph',
      'statsElementId': 'stats_meter',
      'dataCallback': filterGroups.onDataUpdated // Wire the data callback to the filter group so it can be built
   });

   // Load our initial data
   visualizer.load('data/');

});
