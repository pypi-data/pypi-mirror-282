# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc, 2017 Nokia
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.




from .fetchers import NUScheduledtestsuiterunsFetcher


from .fetchers import NUTestsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUScheduledTestSuite(NURESTObject):
    """ Represents a ScheduledTestSuite in the VSD

        Notes:
            A Scheduled Test Suite is grouping of a number of ICMP Echo Tests that can be run at the specified schedule, consecutively from a given source (NSGateway or VPort) toward a specified destination.
    """

    __rest_name__ = "scheduledtestsuite"
    __resource_name__ = "scheduledtestsuites"

    
    ## Constants
    
    CONST_SCHEDULE_INTERVAL_UNITS_HOURS = "HOURS"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_SCHEDULE_INTERVAL_UNITS_MINUTES = "MINUTES"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_SCHEDULE_INTERVAL_UNITS_MONTHS = "MONTHS"
    
    CONST_SCHEDULE_INTERVAL_UNITS_DAYS = "DAYS"
    
    

    def __init__(self, **kwargs):
        """ Initializes a ScheduledTestSuite instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> scheduledtestsuite = NUScheduledTestSuite(id=u'xxxx-xxx-xxx-xxx', name=u'ScheduledTestSuite')
                >>> scheduledtestsuite = NUScheduledTestSuite(data=my_dict)
        """

        super(NUScheduledTestSuite, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._last_updated_date = None
        self._schedule_interval = None
        self._schedule_interval_units = None
        self._description = None
        self._embedded_metadata = None
        self._end_date_time = None
        self._entity_scope = None
        self._creation_date = None
        self._start_date_time = None
        self._owner = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_date", remote_name="lastUpdatedDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="schedule_interval", remote_name="scheduleInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="schedule_interval_units", remote_name="scheduleIntervalUnits", attribute_type=str, is_required=False, is_unique=False, choices=[u'DAYS', u'HOURS', u'MINUTES', u'MONTHS'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="end_date_time", remote_name="endDateTime", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="creation_date", remote_name="creationDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="start_date_time", remote_name="startDateTime", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="owner", remote_name="owner", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.scheduledtestsuiteruns = NUScheduledtestsuiterunsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.tests = NUTestsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the scheduled test suite instance.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the scheduled test suite instance.

                
        """
        self._name = value

    
    @property
    def last_updated_by(self):
        """ Get last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, value):
        """ Set last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        self._last_updated_by = value

    
    @property
    def last_updated_date(self):
        """ Get last_updated_date value.

            Notes:
                Time stamp when this object was last updated.

                
                This attribute is named `lastUpdatedDate` in VSD API.
                
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, value):
        """ Set last_updated_date value.

            Notes:
                Time stamp when this object was last updated.

                
                This attribute is named `lastUpdatedDate` in VSD API.
                
        """
        self._last_updated_date = value

    
    @property
    def schedule_interval(self):
        """ Get schedule_interval value.

            Notes:
                This is the interval between all test runs in this suite and the next run of tests in this suite.

                
                This attribute is named `scheduleInterval` in VSD API.
                
        """
        return self._schedule_interval

    @schedule_interval.setter
    def schedule_interval(self, value):
        """ Set schedule_interval value.

            Notes:
                This is the interval between all test runs in this suite and the next run of tests in this suite.

                
                This attribute is named `scheduleInterval` in VSD API.
                
        """
        self._schedule_interval = value

    
    @property
    def schedule_interval_units(self):
        """ Get schedule_interval_units value.

            Notes:
                The units for the specified interval. This can be minutes, hours or days.

                
                This attribute is named `scheduleIntervalUnits` in VSD API.
                
        """
        return self._schedule_interval_units

    @schedule_interval_units.setter
    def schedule_interval_units(self, value):
        """ Set schedule_interval_units value.

            Notes:
                The units for the specified interval. This can be minutes, hours or days.

                
                This attribute is named `scheduleIntervalUnits` in VSD API.
                
        """
        self._schedule_interval_units = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description for the scheduled test suite instance.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description for the scheduled test suite instance.

                
        """
        self._description = value

    
    @property
    def embedded_metadata(self):
        """ Get embedded_metadata value.

            Notes:
                Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

                
                This attribute is named `embeddedMetadata` in VSD API.
                
        """
        return self._embedded_metadata

    @embedded_metadata.setter
    def embedded_metadata(self, value):
        """ Set embedded_metadata value.

            Notes:
                Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

                
                This attribute is named `embeddedMetadata` in VSD API.
                
        """
        self._embedded_metadata = value

    
    @property
    def end_date_time(self):
        """ Get end_date_time value.

            Notes:
                The date and time by which this suite will be terminated. If this is not specified the tests will continue to run at the specified frequency.

                
                This attribute is named `endDateTime` in VSD API.
                
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, value):
        """ Set end_date_time value.

            Notes:
                The date and time by which this suite will be terminated. If this is not specified the tests will continue to run at the specified frequency.

                
                This attribute is named `endDateTime` in VSD API.
                
        """
        self._end_date_time = value

    
    @property
    def entity_scope(self):
        """ Get entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        return self._entity_scope

    @entity_scope.setter
    def entity_scope(self, value):
        """ Set entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        self._entity_scope = value

    
    @property
    def creation_date(self):
        """ Get creation_date value.

            Notes:
                Time stamp when this object was created.

                
                This attribute is named `creationDate` in VSD API.
                
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value):
        """ Set creation_date value.

            Notes:
                Time stamp when this object was created.

                
                This attribute is named `creationDate` in VSD API.
                
        """
        self._creation_date = value

    
    @property
    def start_date_time(self):
        """ Get start_date_time value.

            Notes:
                The date and time when this suite will start on the NSGateway.

                
                This attribute is named `startDateTime` in VSD API.
                
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, value):
        """ Set start_date_time value.

            Notes:
                The date and time when this suite will start on the NSGateway.

                
                This attribute is named `startDateTime` in VSD API.
                
        """
        self._start_date_time = value

    
    @property
    def owner(self):
        """ Get owner value.

            Notes:
                Identifies the user that has created this object.

                
        """
        return self._owner

    @owner.setter
    def owner(self, value):
        """ Set owner value.

            Notes:
                Identifies the user that has created this object.

                
        """
        self._owner = value

    
    @property
    def external_id(self):
        """ Get external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        """ Set external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        self._external_id = value

    

    