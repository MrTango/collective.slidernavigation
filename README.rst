collective.slidernavigation
===========================

This distribution provides a jQuery slider navigation viewlet for Plone.

Usage
-----

Just enable the collective.slidernavigation in the Plone Add-on menu.
Now you have a new viewlet above the content area. Feel free to move the viewlet into other places true your own distribution.

You can set some properties over per /manage_propertiesForm on a context like the front-page or others. You can set one of the following properties to customize the slidernavigation.

- slidernavigation_source_path: /examplesite/subfolder/subsubfolder

- slidernavigation_autoplay: True

- slidernavigation_interval: 3000

There are also a slidernavigation_properties sheet unser /portal_properties/slidernavigation_properties.

Here you can set the bottom_level for slidernavigation. If you want to use the slidernavigation only for the front-page and the first level, you can set the buttom_level to 1. Then if you are front-page you will see the subfolders in the slidernavigation and if you are in one of this subfolders, you will see the subfolder of this folder. But if you go one level deeper the slidernavigation still shows the subfolders of the parent folder, which is the level-1-folder.


Credits
-------

- `Inqbus`_ for the first release of this distribution

.. _Inqbus: http://www.inqbus.de/
