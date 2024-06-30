===================================================================
Getting Config Values with :class:`~ciscoconfparse2.CiscoConfParse`
===================================================================

Now that we're familiar with parent / child relationships, let's tackle another
common problem.  How do you get specific values from a configuration?

For sure, you could use traditional Python techniques, such as Python's
:any:`re` module; however, the :any:`re` module is rather cumbersome when
you're retrieving a lot of config values.

:class:`~ciscoconfparse2.CiscoConfParse` introduces methods directly on
CiscoConfParse objects which simplify getting values from a configuration:

- :func:`~ciscoconfparse2.models_cisco.IOSCfgLine.re_match_typed()`
- :func:`~ciscoconfparse2.models_cisco.IOSCfgLine.re_match_iter_typed()`
- :func:`~ciscoconfparse2.models_cisco.IOSCfgLine.re_list_iter_typed()`

For the next examples, we will use this configuration...

.. code-block:: none

   ! Filename: short.conf
   !
   hostname IAHS1MDF-AR01A
   !
   vlan 10
    name 192.0.2.0_24_HoustonUsers_S1_Bldg_MDF
   vlan 20
    name 128.66.0.0_24_HoustonPrinters_S1_Bldg_MDF
   !
   interface Vlan10
    description Connection to Houston office LAN switches
    ip address 192.0.2.2 255.255.255.0
    ip helper-address 198.51.100.12
    ip helper-address 203.0.113.12
    standby 10 ip 192.0.2.1
    standby 10 priority 110
    arp timeout 240
    no ip proxy-arp
   !
   interface Vlan20
    description Connection to Houston printer subnet
    ip address 128.66.0.2 255.255.255.0
    standby 20 ip 128.66.01
    standby 20 priority 110
   !

:func:`~ciscoconfparse2.models_cisco.IOSCfgLine.re_match_typed()`: Get a value from an object
---------------------------------------------------------------------------------------------

Let's suppose we want the hostname of `short.conf` above.  One approach is to
use :func:`~ciscoconfparse2.CiscoConfParse.find_objects()` and then use
:func:`~ciscoconfparse2.models_cisco.IOSCfgLine.re_match_typed()` to get the
hostname:

.. code-block:: python
   :emphasize-lines: 4

   >>> from ciscoconfparse2 import CiscoConfParse
   >>> parse = CiscoConfParse('short.conf')
   >>> global_obj = parse.find_objects(r'^hostname')[0]
   >>> hostname = global_obj.re_match_typed(r'^hostname\s+(\S+)', default='')
   >>> hostname
   'IAHS1MDF-AR01A'
   >>>

Take note of the regex we used: ``r'hostname\s+(\S+)'``.  This regex has a
capture group (bounded by the parenthesis), which
:func:`~ciscoconfparse2.models_cisco.IOSCfgLine.re_match_typed()` requires.
:func:`~ciscoconfparse2.models_cisco.IOSCfgLine.re_match_typed()` uses the
contents of this capture group to return the value.

This technique is fine, but we have to tell Python to iterate over all config
objects with :func:`~ciscoconfparse2.CiscoConfParse.find_objects()` and then
we extract the hostname from that object.

What if there was a way to get the hostname without calling :func:`~ciscoconfparse2.CiscoConfParse.find_objects()`?  As it happens,
:func:`~ciscoconfparse.models_cisco.IOSCfgLine.re_match_iter_typed()` does
it for you.


:func:`~ciscoconfparse2.models_cisco.IOSCfgLine.re_match_iter_typed()`: Iterate over all children and get a value
-----------------------------------------------------------------------------------------------------------------

:func:`~ciscoconfparse2.models_cisco.IOSCfgLine.re_match_iter_typed()`
iterates over child objects and returns the *first* value it finds.  This is
very useful because
:func:`~ciscoconfparse2.models_cisco.IOSCfgLine.re_match_iter_typed()` does
all the iteration for us.

.. code-block:: python
   :emphasize-lines: 3

   >>> from ciscoconfparse2 import CiscoConfParse
   >>> parse = CiscoConfParse('short.conf')
   >>> hostname = parse.re_match_iter_typed(r'^hostname\s+(\S+)', default='')
   >>> hostname
   'IAHS1MDF-AR01A'
   >>>

Take note of the regex we used: ``r'hostname\s+(\S+)'``.  This regex has a
capture group (bounded by the parenthesis), which
:func:`~ciscoconfparse2.models_cisco.IOSCfgLine.re_match_iter_typed()` requires.
:func:`~ciscoconfparse2.models_cisco.IOSCfgLine.re_match_iter_typed()` uses the
contents of this capture group to return the value.

This code is better than the previous example, because it eliminates the call
to :func:`~ciscoconfparse2.CiscoConfParse.find_objects()` that we used above.

However, there are still times when you need to call
:func:`~ciscoconfparse2.CiscoConfParse.find_objects()`; one example is when you
need to get the HSRP address from an interface.

.. code-block:: python
   :emphasize-lines: 4

   >>> from ciscoconfparse2 import CiscoConfParse
   >>> parse = CiscoConfParse('short.conf')
   >>> intf_obj = parse.find_objects(r'^interface\s+Vlan10$')[0]
   >>> hsrp_ip = intf_obj.re_match_iter_typed(r'standby\s10\sip\s(\S+)',
   ...     default='')
   >>> hsrp_ip
   '192.0.2.1'
   >>>

The reason we had to call :func:`~ciscoconfparse2.CiscoConfParse.find_objects()`
is so we can get the specific inteface object that contains the HSRP address
in question.

You may be wondering, "Why does this method have *typed* in its name?".  This
is because
:func:`~ciscoconfparse2.models_cisco.IOSCfgLine.re_match_iter_typed()`
can return the value cast as a python type.  By default, all return values are
cast as a Python `str`_.

The following example looks for the ARP timeout on interface Vlan10, and
returns it cast as a Python `int`_.

.. code-block:: python
   :emphasize-lines: 4,5

   >>> from ciscoconfparse2 import CiscoConfParse
   >>> parse = CiscoConfParse('short.conf')
   >>> intf_obj = parse.find_objects(r'^interface\s+Vlan10$')[0]
   >>> arp_timeout = intf_obj.re_match_iter_typed(r'arp\s+timeout\s+(\d+)',
   ...     result_type=int, default=4*3600)
   >>> arp_timeout
   240
   >>>

Finally, let's talk about two more
:func:`~ciscoconfparse2.models_cisco.IOSCfgLine.re_match_iter_typed()`
keywords: `default` and `untyped_default`.

:func:`~ciscoconfparse2.models_cisco.IOSCfgLine.re_match_iter_typed()`
has a `default` keyword, which specifies what the default value should be if
the regular expression doesn't match the configuration.  The value in
`default` is automatically cast as the `result_type`.

However, there may be times when you don't want `default`'s value to be cast
as `result_type`.  If you find yourself in that situation, you can call
:func:`~ciscoconfparse2.models_cisco.IOSCfgLine.re_match_iter_typed()` with
`untyped_default=True`.

.. code-block:: python
   :emphasize-lines: 6

   >>> from ciscoconfparse2 import CiscoConfParse
   >>> parse = CiscoConfParse('short.conf')
   >>> intf_obj = parse.find_objects(r'^interface\s+Vlan20$')[0]
   >>> arp_timeout = intf_obj.re_match_iter_typed(r'arp\s+timeout\s+(\d+)',
   ...     result_type=int,
           untyped_default=True, default='__no_explicit_value__')
   >>> arp_timeout
   '__no_explicit_value__'
   >>>


Getting multiple values from an interface with :func:`~ciscoconfparse2.models_cisco.IOSCfgLine.re_list_iter_typed()`
--------------------------------------------------------------------------------------------------------------------

:func:`~ciscoconfparse2.models_cisco.IOSCfgLine.re_match_typed()` and
:func:`~ciscoconfparse2.models_cisco.IOSCfgLine.re_match_iter_typed()` *do not`
return mutliple values*.

However, :func:`~ciscoconfparse2.models_cisco.IOSCfgLine.re_list_iter_typed()` will return
multiple values.

Suppose we want to get all the DHCP helper-addresses from an interface.  The
best way to do this is to manually iterate over the children and append
the values we want to a list.

This script will get all the DHCP helper-addresses from Vlan10:

.. code-block:: python
   :emphasize-lines: 11

   >>> from ciscoconfparse2 import CiscoConfParse
   >>> parse = CiscoConfParse('short.conf')
   >>>
   >>> # Iterate over matching interfaces
   >>> intf_obj = parse.find_objects(r'^interface\s+Vlan10$')[0]
   >>> retval = intf_obj.re_list_iter_typed("ip helper-address (\S.*)")
   >>> retval
   ['198.51.100.12', '203.0.113.12']
   >>>

.. _`str`: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
.. _`int`: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
