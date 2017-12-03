# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class DayList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, resource_type):
        """
        Initialize the DayList

        :param Version version: Version that contains the resource
        :param resource_type: The resource_type

        :returns: twilio.rest.preview.bulk_exports.export.day.DayList
        :rtype: twilio.rest.preview.bulk_exports.export.day.DayList
        """
        super(DayList, self).__init__(version)

        # Path Solution
        self._solution = {'resource_type': resource_type}
        self._uri = '/Exports/{resource_type}/Days'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams DayInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.bulk_exports.export.day.DayInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'])

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists DayInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.bulk_exports.export.day.DayInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of DayInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DayInstance
        :rtype: twilio.rest.preview.bulk_exports.export.day.DayPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size})

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return DayPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of DayInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DayInstance
        :rtype: twilio.rest.preview.bulk_exports.export.day.DayPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return DayPage(self._version, response, self._solution)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.BulkExports.DayList>'


class DayPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the DayPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param resource_type: The resource_type

        :returns: twilio.rest.preview.bulk_exports.export.day.DayPage
        :rtype: twilio.rest.preview.bulk_exports.export.day.DayPage
        """
        super(DayPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DayInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.bulk_exports.export.day.DayInstance
        :rtype: twilio.rest.preview.bulk_exports.export.day.DayInstance
        """
        return DayInstance(self._version, payload, resource_type=self._solution['resource_type'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.BulkExports.DayPage>'


class DayInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, resource_type):
        """
        Initialize the DayInstance

        :returns: twilio.rest.preview.bulk_exports.export.day.DayInstance
        :rtype: twilio.rest.preview.bulk_exports.export.day.DayInstance
        """
        super(DayInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'redirect_to': payload.get('redirect_to'),
            'day': payload.get('day'),
            'size': deserialize.integer(payload.get('size')),
            'resource_type': payload.get('resource_type'),
        }

        # Context
        self._context = None
        self._solution = {'resource_type': resource_type}

    @property
    def redirect_to(self):
        """
        :returns: The redirect_to
        :rtype: unicode
        """
        return self._properties['redirect_to']

    @property
    def day(self):
        """
        :returns: The day
        :rtype: unicode
        """
        return self._properties['day']

    @property
    def size(self):
        """
        :returns: The size
        :rtype: unicode
        """
        return self._properties['size']

    @property
    def resource_type(self):
        """
        :returns: The resource_type
        :rtype: unicode
        """
        return self._properties['resource_type']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.BulkExports.DayInstance>'