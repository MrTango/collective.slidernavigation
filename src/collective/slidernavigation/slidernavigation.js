$(document).ready(function(){
  $("ul#slidernav-tabs").tabs("#slidernav-panes > div",{
    effect: $("#slidernav #effect").attr('rel'),
    fadeInSpeed: $("#slidernav #fade-in-speed").attr('rel'),
    fadeOutSpeed: $("#slidernav #fade-out-speed").attr('rel'),
    event: 'dblclick',
    initialIndex: 0,
    rotate: true,
  }).slideshow({
    autoplay: Boolean(Number($("#slidernav #autoplay").attr('rel'))),
    interval: $("#slidernav #interval").attr('rel'),
    clickable: false,
  });

  var api = $("#slidernav-tabs").data("tabs");
  if(api != undefined){
    function load_pane_content(event, index){
      if(index == undefined){
        var index = api.getIndex();
      }
      // get the pane to be opened
      var pane = api.getPanes().eq(index);
      // only load once:
      if (!pane.hasClass("loaded")){
        // we use the rel tag to get the load url
        pane.load(api.getTabs().eq(index).attr("rel")).addClass("loaded");
      }
    }

    function pre_load_panes(){
      api.getPanes().each(function(tabindex, tab){
        var pane = api.getPanes().eq(tabindex)
        if(tabindex != 0){
          pane.load(api.getTabs().eq(tabindex).attr("rel")).addClass("loaded").hide();
        }
      });
    }


    // bind event handler to tabs
    $("ul#slidernav-tabs").bind("onBeforeClick load", load_pane_content);

    // load initial tab:
    var tabindex = 0;
    var default_tab = $("#slidernav-tabs > li a.default").parent();
    if(default_tab.length != 0){
      tabindex = default_tab.index();
    }
    api.click(tabindex);
    load_pane_content(0, tabindex);
    if(Number($("#slidernav #autoplay").attr('rel') == 1)){
      pre_load_panes();
    };
  }

});
